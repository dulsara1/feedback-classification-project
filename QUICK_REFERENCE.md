# ⚡ QUICK REFERENCE CARD

## 🚀 FASTEST START (Copy & Paste)

### Windows PowerShell:
```powershell
cd "c:\research component\feedback-response-project\frontend"
python api.py
```
Then open: `frontend/index.html` in browser

### Linux/Mac Terminal:
```bash
cd "c:/research component/feedback-response-project/frontend"
python3 api.py
```
Then open: `frontend/index.html` in browser

---

## 📁 KEY FILES AT A GLANCE

| File | What It Does | When to Use |
|------|--------------|-------------|
| `frontend/index.html` | Web interface | Open in browser to test model |
| `frontend/api.py` | Backend server | Run with `python api.py` |
| `START_HERE.md` | Quick guide | Read this first |
| `verify_setup.py` | Verify everything | Check before starting |
| `data/sentiment_model.pkl` | Trained model | Loaded automatically by API |

---

## 🎯 THREE COMMAND LINES

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start server
python frontend/api.py

# 3. Open browser, double-click: frontend/index.html
# DONE! Model is running.
```

---

## ✅ SUCCESS INDICATORS

| Indicator | Status |
|-----------|--------|
| Terminal shows "Running on http://127.0.0.1:5000" | ✓ Good |
| Browser shows purple gradient interface | ✓ Good |
| Clicking "Analyze" shows results in 1-2 seconds | ✓ Good |
| Results show sentiment emoji + confidence % | ✓ Good |

---

## 🧪 TEST WITH THESE PHRASES

Copy & paste into the frontend:

```
Happy:    "This is amazing and I love it!"
Sad:      "I'm very disappointed with this"
Angry:    "This is absolutely terrible!"
Fear:     "I'm worried about the safety"
Surprise: "I didn't expect this at all!"
Disgust:  "This is disgusting and awful"
```

---

## 🔧 TROUBLESHOOTING (Quick Fixes)

| Problem | Solution |
|---------|----------|
| "Module not found" | `pip install -r requirements.txt` |
| "Port 5000 in use" | Change port in `api.py` line: `port=5001` |
| "Model not found" | Check `data/sentiment_model.pkl` exists |
| "Can't connect" | Check terminal shows server running |
| "No results" | Press F12, check browser console for errors |

---

## 🎨 WHAT YOU'RE TESTING

```
Your Trained Model:
  INPUT:  "Customer feedback text"
    ↓
  PROCESS: TF-IDF vectorization + Logistic Regression
    ↓
  OUTPUT: Sentiment (happiness/sadness/anger/disgust/fear/surprise)
          + Confidence (0-100%)
          + Response message
```

---

## 📊 API ENDPOINTS

### Analyze Feedback:
```
POST /predict
{
  "feedback": "user text"
}

Response:
{
  "sentiment": "happiness",
  "confidence": 0.95,
  "response": "message"
}
```

### Check Server:
```
GET /health

Response:
{
  "status": "healthy",
  "model_loaded": true
}
```

---

## 🚨 ERROR MESSAGES & FIXES

| Error | Cause | Fix |
|-------|-------|-----|
| "Cannot connect to server" | Server not running | `python api.py` |
| "Model not loaded" | File missing | Check `data/*.pkl` exists |
| "Address already in use" | Port taken | Change port in `api.py` |
| "No module named 'flask'" | Dependencies missing | `pip install -r requirements.txt` |
| "No such file or directory" | Wrong folder | `cd frontend` first |

---

## 💾 FILE LOCATIONS

```
Model:       c:\...\feedback-response-project\data\sentiment_model.pkl
Vectorizer:  c:\...\feedback-response-project\data\vectorizer.pkl
Frontend:    c:\...\feedback-response-project\frontend\index.html
API:         c:\...\feedback-response-project\frontend\api.py
```

---

## 🎯 6 SENTIMENTS YOUR MODEL RECOGNIZES

1. **😊 Happiness** - Positive, satisfied, loves it
2. **😢 Sadness** - Disappointed, unhappy, sad
3. **😠 Anger** - Angry, frustrated, mad
4. **🤢 Disgust** - Disgusted, repulsed, awful
5. **😨 Fear** - Worried, concerned, scared
6. **😲 Surprise** - Surprised, unexpected, shocked

---

## 🔑 KEYBOARD SHORTCUTS

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Analyze feedback (in text box) |
| `F5` | Refresh page |
| `F12` | Open browser console (for debugging) |

---

## 📈 CHECK MODEL METRICS

```bash
# See accuracy and classification report
python scripts/train_model.py

# Evaluate on test samples
python evaluate_automated.py

# Run API tests
python frontend/test_api.py
```

---

## 🎮 INTERACTIVE MODE

```bash
cd frontend
python test_api.py
# Choose interactive mode when prompted
# Type feedback for real-time analysis
```

---

## 📱 MOBILE TESTING

1. Start API: `python api.py`
2. Find your computer IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
3. On phone, visit: `http://YOUR_IP:5000`
4. Test on mobile browser!

---

## 🔒 PRODUCTION DEPLOYMENT

```bash
# When ready to deploy:
pip install gunicorn
gunicorn -w 4 api:app
```

---

## 💡 USEFUL COMMANDS

```bash
# Check if Python installed
python --version

# Check if pip works
pip --version

# Install single package
pip install flask

# List installed packages
pip list

# Stop running server
Ctrl+C (in terminal)

# Kill port 5000 (if stuck)
# Windows: netstat -ano | findstr :5000
# Mac/Linux: lsof -i :5000
```

---

## 🎯 PROJECT STATUS

- ✅ Model Trained
- ✅ Vectorizer Fitted
- ✅ Frontend Created
- ✅ API Server Built
- ✅ Documentation Complete
- ✅ Tests Included
- ✅ Ready to Deploy

---

## 🚀 ONE-LINER COMMANDS

```bash
# Everything at once (Windows):
cd "c:\research component\feedback-response-project\frontend" && python api.py

# Test in one go:
python frontend/test_api.py

# Verify setup:
python frontend/verify_setup.py

# Install and run (clean start):
pip install -r requirements.txt && python api.py
```

---

## 📚 DOCUMENTATION

| File | Read When | Time |
|------|-----------|------|
| START_HERE.md | First | 5 min |
| QUICKSTART.md | Before setup | 3 min |
| README.md | Need API info | 10 min |
| ARCHITECTURE.md | Want to understand | 15 min |

---

## ✨ FEATURES AT YOUR FINGERTIPS

✓ Real-time sentiment analysis
✓ Emoji sentiment indicators  
✓ Confidence scoring
✓ Personalized responses
✓ Mobile responsive
✓ Dark mode support
✓ Error handling
✓ Health monitoring
✓ Keyboard shortcuts
✓ Fast response (< 2 sec)

---

## 🎉 YOU'RE ALL SET!

Run these 3 commands:
```bash
cd frontend
pip install -r requirements.txt
python api.py
```

Then:
1. Open browser
2. Double-click index.html
3. Test your model!

---

**Questions?** See START_HERE.md

**Problems?** Run verify_setup.py

**Ready?** Let's go! 🚀

---

Quick Reference v1.0
Last Updated: Jan 6, 2026
