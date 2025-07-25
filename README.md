# AI Agent với Calculator

Một dự án AI agent sử dụng Google Gemini API với tích hợp tính năng calculator.

## Tính năng

- 🤖 AI Agent sử dụng Google Gemini API
- 🔢 Calculator module với các phép toán cơ bản
- ✅ Unit tests cho calculator
- 🐍 Python 3.12+

## Cài đặt

1. Clone repository:
```bash
git clone <your-repo-url>
cd ai_agent
```

2. Cài đặt dependencies sử dụng uv:
```bash
uv sync
```

3. Tạo file `.env` và thêm Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Sử dụng

### AI Agent
```bash
uv run main.py "Your prompt here"
```

### Calculator
Calculator hỗ trợ các phép toán cơ bản với ưu tiên operator:
- Cộng (+)
- Trừ (-)
- Nhân (*)
- Chia (/)

```python
from calculator.pkg.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 5 * 2")  # Kết quả: 13
```

## Cấu trúc dự án

```
ai_agent/
├── calculator/
│   ├── pkg/
│   │   └── calculator.py    # Calculator class
│   ├── main.py             # Calculator demo
│   └── tests.py            # Unit tests
├── main.py                 # AI agent entry point
├── pyproject.toml          # Project configuration
└── README.md               # Documentation
```

## Chạy tests

```bash
cd calculator
python -m unittest tests.py
```

## Requirements

- Python 3.12+
- Google Gemini API key
- Dependencies được quản lý bởi uv

## Dependencies

- `google-genai`: Google Gemini AI API
- `python-dotenv`: Environment variables management
- `typing-extensions`: Type annotations support

