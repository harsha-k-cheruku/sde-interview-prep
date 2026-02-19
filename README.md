# 🎯 SDE Interview Prep Tracker

Complete, clean, production-ready interview preparation platform.

## Quick Start

### macOS/Linux:
```bash
./run.sh
```

### Windows:
```bash
run.bat
```

Then visit: **http://localhost:8000/tools/sde-prep**

## What's Included

- 📊 Dashboard with analytics
- 💻 60+ LeetCode problems tracker
- 📅 12-week study curriculum
- 🏗️ 15 system design topics
- 🎭 Behavioral interview prep
- 📈 Progress tracking & visualizations

## Directory Structure

```
sde-prep/
├── sde_prep/              # Main Python package
│   ├── main.py           # FastAPI app
│   ├── config.py         # Settings
│   ├── database/         # Database setup
│   ├── models/           # SQLAlchemy models
│   ├── routes/           # API routes
│   ├── services/         # Business logic
│   ├── templates/        # Jinja2 templates
│   ├── static/           # CSS, JS, images
│   └── seed_sde.py      # Database seeding
├── requirements.txt      # Dependencies
├── run.sh               # macOS/Linux runner
├── run.bat              # Windows runner
└── README.md
```

## Development

1. **Make changes** in `sde_prep/`
2. **Server auto-reloads** (watch terminal)
3. **Refresh browser** to see changes
4. **Commit when happy**: `git add . && git commit -m "message"`
5. **Push**: `git push origin main`

## Deployment

See Render, Heroku, or AWS documentation for deployment.

## License

MIT
