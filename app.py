from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marie | Containerized App</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #0a0a0f;
            --surface: #111118;
            --accent: #00f5c4;
            --accent2: #ff3e6c;
            --text: #e8e8f0;
            --muted: #5a5a7a;
            --border: #1e1e2e;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'Space Mono', monospace;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Animated grid background */
        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(0,245,196,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0,245,196,0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            z-index: 0;
            animation: gridPulse 8s ease-in-out infinite;
        }

        @keyframes gridPulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .container {
            position: relative;
            z-index: 1;
            max-width: 900px;
            margin: 0 auto;
            padding: 60px 24px;
        }

        /* Top bar */
        .topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 80px;
            opacity: 0;
            animation: fadeUp 0.6s ease forwards;
        }

        .logo {
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
            color: var(--accent);
            letter-spacing: 0.05em;
        }

        .badge {
            display: flex;
            align-items: center;
            gap: 8px;
            background: var(--surface);
            border: 1px solid var(--border);
            padding: 6px 14px;
            border-radius: 100px;
            font-size: 0.7rem;
            color: var(--muted);
        }

        .dot {
            width: 6px; height: 6px;
            border-radius: 50%;
            background: var(--accent);
            animation: blink 2s ease-in-out infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.2; }
        }

        /* Hero */
        .hero {
            margin-bottom: 80px;
        }

        .eyebrow {
            font-size: 0.7rem;
            letter-spacing: 0.3em;
            color: var(--accent);
            text-transform: uppercase;
            margin-bottom: 24px;
            opacity: 0;
            animation: fadeUp 0.6s ease 0.2s forwards;
        }

        h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.8rem, 7vw, 5rem);
            line-height: 1.05;
            margin-bottom: 32px;
            opacity: 0;
            animation: fadeUp 0.6s ease 0.35s forwards;
        }

        h1 em {
            font-style: italic;
            color: var(--accent2);
        }

        .description {
            font-size: 0.85rem;
            line-height: 1.9;
            color: var(--muted);
            max-width: 520px;
            opacity: 0;
            animation: fadeUp 0.6s ease 0.5s forwards;
        }

        /* Cards grid */
        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1px;
            background: var(--border);
            border: 1px solid var(--border);
            margin-bottom: 60px;
            opacity: 0;
            animation: fadeUp 0.6s ease 0.65s forwards;
        }

        .card {
            background: var(--surface);
            padding: 32px 24px;
            transition: background 0.3s ease;
        }

        .card:hover { background: #16161f; }

        .card-icon {
            font-size: 1.6rem;
            margin-bottom: 12px;
            display: block;
        }

        .card-title {
            font-size: 0.7rem;
            letter-spacing: 0.15em;
            color: var(--accent);
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .card-text {
            font-size: 0.75rem;
            color: var(--muted);
            line-height: 1.7;
        }

        /* Terminal block */
        .terminal {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 4px;
            overflow: hidden;
            opacity: 0;
            animation: fadeUp 0.6s ease 0.8s forwards;
        }

        .terminal-bar {
            background: var(--border);
            padding: 10px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .terminal-bar span {
            width: 10px; height: 10px;
            border-radius: 50%;
        }

        .t-red { background: #ff5f57; }
        .t-yellow { background: #febc2e; }
        .t-green { background: #28c840; }

        .terminal-label {
            margin-left: auto;
            font-size: 0.65rem;
            color: var(--muted);
        }

        .terminal-body {
            padding: 24px;
            font-size: 0.8rem;
            line-height: 2;
        }

        .cmd { color: var(--accent); }
        .comment { color: var(--muted); }
        .output { color: #a0a0c0; }

        /* Footer */
        .footer {
            margin-top: 60px;
            padding-top: 24px;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.7rem;
            color: var(--muted);
            opacity: 0;
            animation: fadeUp 0.6s ease 1s forwards;
        }

        .footer-accent { color: var(--accent2); }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 640px) {
            .cards { grid-template-columns: 1fr; }
            .topbar { flex-direction: column; gap: 12px; align-items: flex-start; }
        }
    </style>
</head>
<body>
    <div class="container">

        <div class="topbar">
            <div class="logo">Marie.</div>
            <div class="badge">
                <span class="dot"></span>
                Conteneur actif · Port 5000
            </div>
        </div>

        <div class="hero">
            <p class="eyebrow">Bonjour à tous</p>
            <h1>Application <em>conteneurisée</em><br>avec Docker</h1>
            <p class="description">
                Ceci est une simple application Flask déployée dans un conteneur Docker,
                construite par <strong style="color:var(--text)">Marie</strong> dans le cadre
                du TP Conduite de Projet · Keyce Informatique & IA · 2026.
            </p>
        </div>

        <div class="cards">
            <div class="card">
                <span class="card-icon">🐳</span>
                <div class="card-title">Docker</div>
                <div class="card-text">Image construite à partir de python:3.9, optimisée pour la production.</div>
            </div>
            <div class="card">
                <span class="card-icon">🐍</span>
                <div class="card-title">Flask</div>
                <div class="card-text">Framework web Python léger, exposé sur le port 5000 via 0.0.0.0.</div>
            </div>
            <div class="card">
                <span class="card-icon">🚀</span>
                <div class="card-title">CI/CD</div>
                <div class="card-text">Pipeline Jenkins pour build automatique et push vers DockerHub.</div>
            </div>
        </div>

        <div class="terminal">
            <div class="terminal-bar">
                <span class="t-red"></span>
                <span class="t-yellow"></span>
                <span class="t-green"></span>
                <span class="terminal-label">bash — marie-flask-app</span>
            </div>
            <div class="terminal-body">
                <div><span class="comment"># Construction de l'image</span></div>
                <div><span class="cmd">$ docker build -t marie-flask-app .</span></div>
                <div><span class="output">Successfully built ✓</span></div>
                <div>&nbsp;</div>
                <div><span class="comment"># Lancement du conteneur</span></div>
                <div><span class="cmd">$ docker run -d -p 5000:5000 marie-flask-app</span></div>
                <div><span class="output">Container running on http://localhost:5000 ✓</span></div>
            </div>
        </div>

        <div class="footer">
            <span>Keyce Informatique &amp; IA · Yaoundé · 2026</span>
            <span>Master 1 Cybersécurité · <span class="footer-accent">Marie</span></span>
        </div>

    </div>
</body>
</html>"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
