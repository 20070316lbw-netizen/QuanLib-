<div align="center">
  <h1>🚀 QuanLib：量化代码素材库</h1>
  <p>专为量化研究员与实盘开发者打造的<b>高复用代码组件库</b>。</p>
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</div>

---

## 📖 项目简介
QuanLib 并非臃肿的端到端框架，而是一个**「开箱即用」的高质量代码素材库**。它包含了一系列量化投研日常必需的核心模块，每个模块均为独立运行的设计，并内建有模拟数据。如果你不想受限并束缚于重型框架，只想摘取核心的预处理逻辑、大类因子计算方案或是基础模型，这里就是你的弹药库。

### 📌 我们的核心原则
- ✅ **开箱即用**：每个模块独立运行，自带测试数据与 `example_usage.py`。
- ✅ **白盒易读**：摒弃多层继承与抽象，只为你提供带有详尽中文 Docstring 注释的基础实现。
- ✅ **即拔即插**：不设复杂的 `setup.py`，你只需找到所需的 `.py` 文件，复制进自己的系统即可。

## 🧩 模块全景图

| 📁 模块目录 | 🛠️ 覆盖功能 | 🚀 核心资产提取 |
| :--- | :--- | :--- |
| `01_data_quality/` | **数据健康扫描** | OHLCV 列完整性、缺失值侦测、价格暴涨暴跌与成交量剧变监控的通用基类 |
| `02_neutralization/` | **因子正交中性化** | 基于回归的行业中性化代理、市值残差剥离、底层 OLS 高并发矩阵推导 |
| `03_models/` | **核心模型与算子** | 手写梯度提升树 (GBDT) 等自研模型的无三方依赖版及其二阶导逻辑 |
| `04_factors/` | **经典因子加工** | 动量衍生 (12-1 等)、跨期反转、多窗口波动率统计、财务价值 (BP/EP) 因子 |
| `05_evaluation/` | **评估与回滚测试** | 因子信息系数 (IC, RankIC, ICIR) 分析引擎、轻量化向量积回测模块 |
| `06_utils/` | **公共支撑组件** | 日历边界与补齐、ST与异动停牌股票过滤、标准 Loguru 统一日志模板 |

## 🕹️ 快速起步指南

通过以下几行脚本将素材库下载至本地：

```bash
# 1. 克隆素材库
git clone https://github.com/20070316lbw-netizen/QuanLib-.git
cd QuanLib-

# 2. 准备虚拟运行环境
python -m venv .venv
source .venv/Scripts/activate  # Windows 用户可通过: .venv\Scripts\activate

# 3. 安装依赖包
pip install -r requirements.txt

# 4. 试运行一个模块（以数据质检为例）
cd 01_data_quality
python example_usage.py
```

## 🛠️ 正确的使用姿势

1. **查阅总览**：通过本文档的「模块全景图」定位你的目标。
2. **直达明细**：深入对应模块并阅读其专属的 `README.md`。
3. **验证演示**：通过 `python example_usage.py`，你可借助生成的“假数据”直接看到代码运行的成效。
4. **据为己有**：复制所需的 `.py` 文件，重组进你自己的策略工程体系！

---

## 📦 极简依赖项
我们极力克制了对厚重第三方库的引用：
```text
numpy>=1.21.0
pandas>=1.3.0
loguru>=0.6.0
scipy>=1.7.0
```

*如果觉得本项目节省了造轮子的时间，欢迎分享与反馈。基于 MIT 协议，你可以自由修改甚至商用。*
