# jacksonlowder — Personal Portfolio Website

Live at **[jacksonlowder.com](https://jacksonlowder.com)** · Hosted via GitHub Pages

A fully custom, single-page professional portfolio and multi-page project showcase. Built with vanilla HTML, CSS, and JavaScript — no frameworks, no jQuery, no Bootstrap. Every dependency in the old site was removed and replaced from scratch.

---

## Site Structure

| File | Description |
|---|---|
| `index.html` | Main single-page portfolio (Hero, About, Skills, Experience, Projects, Contact) |
| `OpenArchive.html` | Dedicated project page — Open Archive document management system |
| `BEZNext.html` | Dedicated project page — BEZNext Query Performance Dashboard |
| `CSITools.html` | Dedicated project page — CSI Office Automation Suite |
| `MetaDataRemover.html` | Live interactive tool — client-side EXIF metadata remover |
| `css/style.css` | Complete design system — CSS custom properties, no external CSS framework |
| `js/main.js` | Vanilla JS — mobile nav, IntersectionObserver animations, active nav tracking, email copy |
| `images/favicon.svg` | JL monogram SVG favicon |
| `Jackson Lowder Resume 2026.pdf` | Public resume (personal contact info redacted via PyMuPDF) |

---

## Design System

All styling is defined through CSS custom properties in `css/style.css`.

```css
--bg: #0d1117;           /* Page background */
--bg-surface: #161b22;   /* Cards, sections */
--bg-elevated: #21262d;  /* Elevated cards */
--accent: #58a6ff;       /* Links, highlights */
--text: #e6edf3;         /* Primary text */
--text-muted: #8b949e;   /* Secondary text */
--border: #30363d;       /* Borders */
--font-sans: 'Inter';    /* Body font */
--font-mono: 'JetBrains Mono'; /* Code/nav font */
```

**Features:**
- Fully responsive — CSS Grid + Flexbox, mobile hamburger nav
- Scroll fade-in animations via `IntersectionObserver` (no scroll jank)
- Active nav link tracking via `IntersectionObserver` with `rootMargin`
- Frosted glass navbar using `backdrop-filter: blur()`
- Hero section entrance animations using CSS `@keyframes`

---

## Pages

### `index.html` — Main Portfolio

Single-page layout with smooth-scroll anchor navigation. Sections:

1. **Hero** — Name, title, tagline, two CTAs (View My Work, Download Resume)
2. **About** — Bio + quick-facts card (education, location, email, GitHub, status)
3. **Skills** — 6 grouped tag categories (see below)
4. **Experience** — Vertical timeline with 4 real work entries
5. **Projects** — Responsive card grid (8 cards) with FERPA badges, tech tags, and View Project / GitHub / Live Tool links
6. **Contact** — Click-to-copy email, GitHub + LinkedIn social links

**Skills categories:** Languages · Web & Development · Databases & Cloud · Data & Analytics · Automation & Tooling · Compliance & Security

**Experience:**
- Assistant Registrar — Computer Systems Institute (Jun 2024 – Present)
- Software Engineer Intern — BEZNext (Summer 2023)
- Quality Control Intern — Culligan (Summer 2022)
- IT Tech Support — Computer Systems Institute (2015, 2020, 2021)

**Projects grid order:**
1. CSI Office Automation Suite → `CSITools.html`
2. Open Archive → `OpenArchive.html`
3. BEZNext Query Performance Dashboard → `BEZNext.html`
4. Metadata Remover → `MetaDataRemover.html` (live tool)
5. Math Problem Generator → GitHub
6. Business Analytics CIS — CS 475 → GitHub
7. PKI Certificate Hierarchy — CS 415 → GitHub

---

### `OpenArchive.html` — Open Archive Project Page

Full dedicated showcase for the Open Archive Django document management system. Includes:
- Hero with tech tags and fake-data disclaimer banner (FERPA)
- 7 overview cards (Document Management, Student Tracking, RBAC, External Data Sync, Automated Backups, AI Document Classification, Theme Customizer)
- 9 alternating screenshot sections:
  - Dashboard, Students, Student Files (Folder View), Student Files (List View), Bulk Upload, AI Document Analysis, System Activity Log, Task Management, Theme Customizer
- "How it works" 5-step workflow section
- Tech stack: Backend · Database · Frontend · AI & Analysis · Security & Ops

**FERPA notice:** All student data shown is entirely fictional, generated for demonstration only.

**Tech:** Django 4.x · Python · PostgreSQL · SQLite · MySQL · HTML/CSS/JS · RBAC · CSRF Protection · Audit Logging · Filename Pattern Matching · Content Analysis · Confidence Scoring

---

### `BEZNext.html` — BEZNext Query Performance Dashboard

Dedicated page for the internship project built at BEZNext (Summer 2023). Includes:
- Hero labeled as Software Engineer Internship
- 6 overview cards (Multi-Database Connectivity, Query Performance Analysis, Statistical Metrics, Oracle Workload Integration, Query Filtering & Controls, Query Text Popup)
- 2 screenshot sections — Snowflake tab and Teradata tab
- 5-step end-to-end workflow (form submit → Oracle pre-query → DB execution → pandas → HTML render)
- Tech stack: Python 3.11 · Django 3.2 · pandas · Snowflake · Teradata · Oracle · snowflake-connector-python · teradatasql · cx_Oracle · AJAX · Rotating File Logging

---

### `CSITools.html` — CSI Office Automation Suite

Dedicated page for internal Python desktop tools built at the Computer Systems Institute. Includes:
- Hero with FERPA notice (details redacted)
- 6 overview cards (Multi-Mode OCR Pipeline, Regex Extraction & Validation, Excel Auto-Fill Integration, Multi-Quarter Enrollment Processing, Windows COM Outlook Integration, FERPA-Compliant Design)
- 2 screenshot sections:
  - **Attendance Sheet Tracker** — PyMuPDF + multi-PSM Tesseract OCR (PSM 3/6/11 at 5x zoom), 11 regex patterns, normalization, validation, `FillAttendanceSheetTracker` auto-filler
  - **Seat Counts Processor** — pandas + openpyxl multi-quarter processing, TermID auto-split, CF_HDROP clipboard, `win32com` Outlook draft creation, `config.json` settings modal, column validation
- Tech stack: Python · Tkinter · pandas · openpyxl · PyMuPDF (fitz) · pytesseract · Pillow · pywin32 (win32com) · Multi-PSM OCR · Regex Extraction · Outlook Automation · SQL · Microsoft Access

**FERPA notice:** Specific workflow logic, data structures, and internal identifiers are intentionally redacted.

---

### `MetaDataRemover.html` — Metadata Remover Tool

Live browser-based tool. Strips EXIF and other metadata from images entirely client-side using the HTML5 Canvas API — no server upload. Supports drag-and-drop or click-to-browse. Preserves PNG format; defaults to JPEG for all other types.

---

## What Changed From the Original Site

The original site used Bootstrap 3 (2013-era), jQuery 1.11.3, and a terminal-gimmick theme spread across 4 separate pages with no work history.

| Before | After |
|---|---|
| Bootstrap 3 + jQuery 1.11.3 | Zero external dependencies |
| 4 separate HTML pages | Single-page portfolio + dedicated project pages |
| Terminal ASCII theme | Clean dark design system with CSS custom properties |
| No work experience | Full 4-entry timeline from resume |
| No real contact info | Real email, GitHub (JL2102), LinkedIn |
| Old GitHub username (Siter123) | Corrected to JL2102 throughout |
| Placeholder Lorem-style bio | Real bio grounded in actual experience |
| 4 skill boxes | 6 categorized skill groups (30+ skills) |
| No project detail pages | 3 full dedicated project pages |
| `JL_New_Logo_Trans.png` favicon | Custom JL SVG favicon matching site brand |
| `resume2.pdf` | `Jackson Lowder Resume 2026.pdf` (redacted via PyMuPDF) |

**Deleted files:** `css/terminaltheme.css`, `css/Project_metadata.css`, `css/bootstrap.min.css`, `js/jquery-1.11.3.min.js`, `js/bootstrap.min.js`, `js/jquery.easing.min.js`, `js/custom.js`, `js/ie10-viewport-bug-workaround.js`, `Profile.html`, `Projects.html`, `contact.html`

---

## Resume Privacy

The publicly hosted resume (`Jackson Lowder Resume 2026.pdf`) had personal contact information (phone number and personal email) permanently redacted using Python + PyMuPDF before being committed:

```python
import fitz
doc = fitz.open("Jackson Lowder Resume 2026.pdf")
for page in doc:
    for text in ["(312) 659-4628", "Jacksonlowder2102@gmail.com"]:
        for inst in page.search_for(text):
            page.add_redact_annot(inst, fill=(1, 1, 1))
    page.apply_redactions()
doc.save("output.pdf")
```

Public contact: **Contact@jacksonlowder.com**

---

## FERPA Compliance

Three project showcases involve tools built for academic institutions governed by FERPA:

- **CSI Office Automation Suite** (`CSITools.html`) — details redacted; UI screenshots only
- **Open Archive** (`OpenArchive.html`) — all student data is entirely fictional/generated
- **CSI project card** on `index.html` — labeled with amber FERPA badge

No real student names, IDs, academic records, or institutional identifiers appear anywhere on this site.

---

## Local Development

No build step required. Open any HTML file directly in a browser, or serve with any static file server:

```powershell
# Python
python -m http.server 8000

# Node
npx serve .
```

The site is deployed automatically via GitHub Pages on push to `master`.
