import numpy as np

class TreeNode:
    """定义树节点"""
    def __init__(self):
        self.left = None
        self.right = None
        self.feature = None
        self.threshold = None
        self.weight = None


class SimpleGBDT:
    def __init__(self, n_trees=100, max_depth=5, lr=0.1, min_samples=2):
        """
        参数:
            n_trees: 树的数量
            max_depth: 最大深度
            lr: 学习率
            min_samples: 最小样本数
        """
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.lr = lr
        self.trees = []
        self.min_samples = min_samples

    def _grad(self, y, y_pred):
        """计算一阶梯度 (MSE 损失)"""
        return y_pred - y   # 这是 g_i
    
    def _hess(self, y, y_pred):
        """计算二阶梯度 (MSE 损失的二阶导)"""
        return np.ones_like(y)   # h_i = 1
    
    def _gain(self, G_L, H_L, G_R, H_R):
        """计算分裂收益 Gain"""
        # 防止除以0
        if H_L == 0 or H_R == 0:
            return 0

        Gain = 0.5 * (G_L**2/H_L + G_R**2/H_R - (G_L+G_R)**2/(H_L+H_R))
        return Gain
    
    def _best_split(self, X, g, h):
        """枚举所有特征和阈值, 找出最大 Gain 的分裂点"""
        best_gain = -np.inf   # 记录目前为止最好的增益
        best_feature = None
        best_threshold = None

        n_features = X.shape[1]

        for feature_idx in range(n_features):
            # 取出这一列的值, 排序去重
            thresholds = np.unique(X[:, feature_idx])

            for threshold in thresholds:
                # 分布左右两组
                left_mask = X[:, feature_idx] <= threshold
                right_mask = ~left_mask

                # 计算左右节点的梯度和与二阶梯度和
                G_L, H_L = g[left_mask].sum(), h[left_mask].sum()
                G_R, H_R = g[right_mask].sum(), h[right_mask].sum()

                gain = self._gain(G_L, H_L, G_R, H_R)
                if gain > best_gain:
                    best_gain = gain    # 更新最大gain
                    best_feature = feature_idx    # 记录特征索引
                    best_threshold = threshold    # 记录阈值

        return best_feature, best_threshold, best_gain

    def _build_tree(self, X, g, h, depth):
        """递归建树"""
        # 1. 如果样本太少，创建叶节点
        if len(g) < self.min_samples:
            node = TreeNode()
            node.weight = -g.sum() / h.sum()
            return node

        # 2. 如果深度达到上限，创建叶节点
        if depth >= self.max_depth:
            node = TreeNode()
            node.weight = -g.sum() / h.sum()
            return node

        # 3. 找最优分裂点
        feature, threshold, best_gain = self._best_split(X, g, h)

        # 4. 如果没带来正收益，创建叶节点
        if best_gain <= 0:
            node = TreeNode()
            node.weight = -g.sum() / h.sum()
            return node

        # 5. 根据特征和阈值分裂样本
        left_mask = X[:, feature] <= threshold
        right_mask = ~left_mask

        X_left, X_right = X[left_mask], X[right_mask]
        g_left, g_right = g[left_mask], g[right_mask]
        h_left, h_right = h[left_mask], h[right_mask]

        # 6. 建左右子树
        node = TreeNode()
        node.feature = feature
        node.threshold = threshold
        node.left = self._build_tree(X_left, g_left, h_left, depth+1)
        node.right = self._build_tree(X_right, g_right, h_right, depth+1)
        return node

    def fit(self, X, y):
        """训练模型"""
        y_pred = np.zeros_like(y)
        
        for _ in range(self.n_trees):
            g = self._grad(y, y_pred)
            h = self._hess(y, y_pred)
            tree = self._build_tree(X, g, h, depth=0)
            self.trees.append(tree)
            
            # 使用新生成的树更新预测值
            tree_pred = np.array([self._predict_single(tree, x) for x in X])
            y_pred += self.lr * tree_pred

    def predict(self, X):
        """预测"""
        y_pred = np.zeros(X.shape[0])
        for tree in self.trees:
            for i, x in enumerate(X):
                y_pred[i] += self.lr * self._predict_single(tree, x)
        return y_pred 
    
    def _predict_single(self, node, x):
        """单样本预测"""
        if node.weight is not None:
            return node.weight
        else:
            if x[node.feature] <= node.threshold:
                return self._predict_single(node.left, x)
            else:
                return self._predict_single(node.right, x)
