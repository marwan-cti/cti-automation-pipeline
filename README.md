# 🛰️ CTI Automation Pipeline

> ⚠️ **Projet en cours de construction**  
> Le développement débutera début juillet 2025. Le dépôt est déjà structuré pour documenter les cas d’usage, les playbooks et l’architecture cible.

> A hybrid threat detection engine combining OSINT, technical indicators (IOC), and automated playbook activation for Cyber Threat Intelligence (CTI) use cases.

---

## 📌 Features

- 📰 RSS ingestion (e.g. failed bond auctions)
- 🖼️ Malicious SVG scanner
- 💬 Narrative signal simulation (Telegram/X)
- ⚙️ Risk scoring & correlation engine
- 🚨 Automated response via YAML playbooks
- 📂 IOC extraction and enrichment (future: MISP, VT)

---

## 🚀 Getting Started

```bash
git clone https://github.com/youruser/cti-automation-pipeline.git
cd cti-automation-pipeline
pip install -r requirements.txt
python main.py
```

---

## 📦 Use Cases

- [VIP targeted by phishing + disinfo](usecases/usecase_vip_disinfo_phishing.md)
- [Ransomware + SIEM + HR reaction](usecases/usecase_ransomware_siem_alert.yaml)
- [→ Template for future use cases](usecases/template_usecase_blank.md)

---

## 🛠️ Technologies

- Python 3.10+
- feedparser / requests
- YAML / bash
- Modular playbook engine

---

## 📄 License

MIT License
