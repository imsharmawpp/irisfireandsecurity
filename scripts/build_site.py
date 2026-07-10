#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IRIS Fire & Security — static site generator.
Every emitted page is 100% self-contained: ALL CSS inlined, vanilla JS only,
Google Fonts + Google Maps iframe as the only externals. No frameworks.
Run:  python scripts/build_site.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = "assets"

# ----------------------------------------------------------------------------
#  SHARED DESIGN SYSTEM (inlined into every page)
# ----------------------------------------------------------------------------
CSS = r"""
:root{
  --ink:#0A1426; --ink-2:#10203B;
  --blue:#0B5FCC; --blue-dark:#08489E; --azure:#38BDF8; --amber:#F59E0B;
  --cloud:#F5F7FA; --cloud-2:#ECF1F7; --white:#FFFFFF;
  --slate:#5A6B82; --slate-light:#8A99AD; --line:#E2E8F0;
  --shadow-sm:0 1px 3px rgba(10,20,38,.06),0 1px 2px rgba(10,20,38,.04);
  --shadow-md:0 8px 24px rgba(10,20,38,.08);
  --shadow-lg:0 24px 60px rgba(11,95,204,.14);
  --radius:18px; --radius-lg:26px; --maxw:1240px;
  --font-display:'Space Grotesk',system-ui,sans-serif;
  --font-body:'Inter',system-ui,sans-serif;
  --font-mono:'JetBrains Mono',ui-monospace,monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:var(--font-body);color:var(--ink);background:var(--white);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;display:block}
a{text-decoration:none;color:inherit}
ul{list-style:none}
.container{max-width:var(--maxw);margin:0 auto;padding:0 28px}
.section{padding:110px 0}
.eyebrow{font-family:var(--font-mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);font-weight:500;display:inline-flex;align-items:center;gap:9px;margin-bottom:18px}
.eyebrow::before{content:"";width:26px;height:2px;background:var(--blue);border-radius:2px}
h1,h2,h3,h4{font-family:var(--font-display);font-weight:700;letter-spacing:-.02em;line-height:1.08}
h2{font-size:clamp(30px,4vw,48px);margin-bottom:18px}
.section-head{max-width:700px;margin:0 auto 64px;text-align:center}
.section-head p{color:var(--slate);font-size:18px}
.btn{display:inline-flex;align-items:center;gap:10px;font-family:var(--font-body);font-weight:600;font-size:15px;padding:14px 26px;border-radius:12px;transition:.25s cubic-bezier(.2,.7,.3,1);cursor:pointer;border:1px solid transparent}
.btn-primary{background:var(--blue);color:#fff;box-shadow:0 8px 20px rgba(11,95,204,.28)}
.btn-primary:hover{background:var(--blue-dark);transform:translateY(-2px);box-shadow:0 14px 30px rgba(11,95,204,.34)}
.btn-ghost{background:#fff;color:var(--ink);border-color:var(--line)}
.btn-ghost:hover{border-color:var(--blue);color:var(--blue);transform:translateY(-2px)}
.btn-amber{background:var(--amber);color:#1c1300}
.btn-amber:hover{transform:translateY(-2px);box-shadow:0 12px 26px rgba(245,158,11,.34)}
.btn svg{width:18px;height:18px}
header{position:fixed;top:0;left:0;right:0;z-index:100;transition:.3s}
.nav{display:flex;align-items:center;justify-content:space-between;height:78px}
.brand{display:flex;align-items:center;gap:12px}
.brand img.logo{height:38px}
.brand .mono{height:34px;width:34px;border-radius:9px;background:var(--cloud);padding:5px;display:none}
.nav-links{display:flex;align-items:center;gap:34px}
.nav-links a{font-weight:500;font-size:15px;color:var(--ink-2);position:relative;transition:.2s}
.nav-links a::after{content:"";position:absolute;left:0;bottom:-6px;width:0;height:2px;background:var(--blue);transition:.25s}
.nav-links a:hover,.nav-links a.active{color:var(--blue)}
.nav-links a.active::after,.nav-links a:hover::after{width:100%}
.nav-links.on-dark a{color:rgba(255,255,255,.88)}
.nav-links.on-dark a:hover,.nav-links.on-dark a.active{color:#fff}
header:not(.header-solid) .nav-cta .btn-ghost{background:rgba(10,20,38,.28);border-color:rgba(255,255,255,.4);color:#fff}
header:not(.header-solid) .nav-cta .btn-ghost:hover{background:rgba(10,20,38,.42);border-color:var(--azure);color:#fff}
header:not(.header-solid) .brand .logo{filter:brightness(0) invert(1)}
header:not(.header-solid) .menu-btn span{background:#fff}
.nav-cta{display:flex;align-items:center;gap:14px}
.header-solid{background:rgba(255,255,255,.86);backdrop-filter:blur(14px);box-shadow:var(--shadow-sm);border-bottom:1px solid var(--line)}
.header-solid .brand .mono{display:block}
.menu-btn{display:none;background:none;border:none;cursor:pointer;padding:8px}
.menu-btn span{display:block;width:24px;height:2px;background:var(--ink);margin:5px 0;transition:.3s}
.hero{padding:170px 0 90px;background:
  radial-gradient(1200px 600px at 85% -10%,rgba(56,189,248,.16),transparent 60%),
  radial-gradient(900px 500px at 0% 10%,rgba(11,95,204,.10),transparent 55%),
  linear-gradient(180deg,#fff 0%,var(--cloud) 100%)}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:60px;align-items:center}
.hero-badge{display:inline-flex;align-items:center;gap:10px;background:#fff;border:1px solid var(--line);border-radius:100px;padding:8px 16px;font-size:13.5px;font-weight:500;color:var(--ink-2);box-shadow:var(--shadow-sm);margin-bottom:26px}
.hero-badge .dot{width:9px;height:9px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 4px rgba(34,197,94,.18);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 4px rgba(34,197,94,.18)}50%{box-shadow:0 0 0 7px rgba(34,197,94,.06)}}
.hero h1{font-size:clamp(40px,5.4vw,68px);margin-bottom:22px}
.hero h1 .accent{color:var(--blue)}
.hero p.lead{font-size:19px;color:var(--slate);max-width:520px;margin-bottom:34px}
.hero-actions{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:40px}
.hero-stats{display:flex;gap:36px;flex-wrap:wrap}
.hero-stats .s{display:flex;flex-direction:column}
.hero-stats .s b{font-family:var(--font-display);font-size:30px;color:var(--ink)}
.hero-stats .s span{font-size:13.5px;color:var(--slate)}
.hero-visual{position:relative}
.hero-visual .frame{border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-lg);border:1px solid var(--line);position:relative;background:#fff}
.hero-visual img{width:100%;height:460px;object-fit:cover}
.hud{position:absolute;inset:0;pointer-events:none}
.corner{position:absolute;width:30px;height:30px;border:2px solid var(--azure);opacity:.7}
.corner.tl{top:16px;left:16px;border-right:0;border-bottom:0}
.corner.tr{top:16px;right:16px;border-left:0;border-bottom:0}
.corner.bl{bottom:16px;left:16px;border-right:0;border-top:0}
.corner.br{bottom:16px;right:16px;border-left:0;border-top:0}
.hero-float{position:absolute;background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px 16px;box-shadow:var(--shadow-md);display:flex;align-items:center;gap:11px;font-size:14px;font-weight:600}
.hero-float .ic{width:34px;height:34px;border-radius:9px;background:rgba(11,95,204,.1);color:var(--blue);display:grid;place-items:center}
.hero-float.f1{bottom:34px;left:-26px;animation:floaty 5s ease-in-out infinite}
.hero-float.f2{top:30px;right:-22px;animation:floaty 5s ease-in-out infinite .8s}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.strip{background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:30px 0}
.strip .container{display:flex;align-items:center;justify-content:space-between;gap:30px;flex-wrap:wrap}
.strip span{font-family:var(--font-mono);font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--slate-light)}
.strip .items{display:flex;gap:42px;flex-wrap:wrap;align-items:center;color:var(--slate);font-family:var(--font-display);font-weight:600;font-size:16px;opacity:.7}
.services{background:var(--cloud)}
.svc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.svc{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:30px 26px;transition:.3s;position:relative;overflow:hidden}
.svc::before{content:"";position:absolute;inset:0;background:linear-gradient(160deg,rgba(11,95,204,.05),transparent 55%);opacity:0;transition:.3s}
.svc:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);border-color:rgba(11,95,204,.3)}
.svc:hover::before{opacity:1}
.svc .ic{width:54px;height:54px;border-radius:14px;background:linear-gradient(150deg,rgba(11,95,204,.12),rgba(56,189,248,.12));color:var(--blue);display:grid;place-items:center;margin-bottom:20px;position:relative;z-index:1}
.svc .ic svg{width:28px;height:28px}
.svc h3{font-size:19px;margin-bottom:10px;position:relative;z-index:1}
.svc p{font-size:14.5px;color:var(--slate);position:relative;z-index:1}
.svc .more{margin-top:16px;font-size:13.5px;font-weight:600;color:var(--blue);display:inline-flex;align-items:center;gap:6px;position:relative;z-index:1}
.why-grid{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.why-list{display:grid;gap:22px;margin-top:34px}
.why-item{display:flex;gap:18px}
.why-item .num{font-family:var(--font-mono);font-size:14px;color:var(--blue);font-weight:500;padding-top:4px;min-width:34px}
.why-item h4{font-family:var(--font-display);font-size:18px;margin-bottom:5px}
.why-item p{color:var(--slate);font-size:15px}
.why-visual{border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-lg);border:1px solid var(--line)}
.why-visual img{width:100%;height:520px;object-fit:cover}
.process{background:var(--ink);color:#fff;position:relative;overflow:hidden}
.process::before{content:"";position:absolute;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(11,95,204,.35),transparent 70%);top:-200px;right:-150px}
.process .eyebrow{color:var(--azure)}
.process .eyebrow::before{background:var(--azure)}
.process .section-head h2{color:#fff}
.process .section-head p{color:rgba(255,255,255,.7)}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;position:relative;z-index:1}
.step{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:var(--radius);padding:30px 26px;transition:.3s}
.step:hover{background:rgba(255,255,255,.08);transform:translateY(-5px)}
.step .n{font-family:var(--font-display);font-size:42px;font-weight:700;color:transparent;-webkit-text-stroke:1.5px var(--azure);margin-bottom:14px}
.step h4{font-family:var(--font-display);font-size:19px;margin-bottom:9px}
.step p{font-size:14.5px;color:rgba(255,255,255,.66)}
.ind-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.ind{position:relative;border-radius:var(--radius);overflow:hidden;border:1px solid var(--line);min-height:260px;display:flex;align-items:flex-end;transition:.3s}
.ind img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:.5s}
.ind::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 35%,rgba(10,20,38,.82))}
.ind:hover img{transform:scale(1.07)}
.ind .cap{position:relative;z-index:1;padding:24px;color:#fff;width:100%}
.ind .cap h4{font-family:var(--font-display);font-size:21px;margin-bottom:4px}
.ind .cap span{font-size:13.5px;color:rgba(255,255,255,.78)}
.cta-band{background:linear-gradient(120deg,var(--blue),var(--blue-dark));position:relative;overflow:hidden}
.cta-band::before{content:"";position:absolute;inset:0;background:radial-gradient(500px 300px at 90% 20%,rgba(56,189,248,.4),transparent)}
.cta-inner{position:relative;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:40px;padding:64px 0;flex-wrap:wrap}
.cta-inner h2{color:#fff;margin-bottom:8px;font-size:clamp(26px,3.4vw,40px)}
.cta-inner p{color:rgba(255,255,255,.85);font-size:17px;max-width:520px}
footer{background:var(--ink);color:rgba(255,255,255,.75);padding:70px 0 0}
.foot-grid{display:grid;grid-template-columns:1.6fr 1fr 1fr 1.2fr;gap:40px;padding-bottom:50px}
.foot-brand img{height:40px;margin-bottom:18px}
.foot-brand p{font-size:14.5px;max-width:300px;color:rgba(255,255,255,.6)}
.foot-col h5{font-family:var(--font-display);color:#fff;font-size:15px;letter-spacing:.04em;margin-bottom:18px;text-transform:uppercase}
.foot-col a{display:block;font-size:14.5px;color:rgba(255,255,255,.7);padding:6px 0;transition:.2s}
.foot-col a:hover{color:var(--azure);padding-left:5px}
.foot-contact .row{display:flex;gap:12px;align-items:flex-start;font-size:14.5px;margin-bottom:14px;color:rgba(255,255,255,.78)}
.foot-contact .row svg{width:18px;height:18px;color:var(--azure);flex-shrink:0;margin-top:3px}
.foot-bottom{border-top:1px solid rgba(255,255,255,.1);padding:22px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;font-size:13.5px;color:rgba(255,255,255,.55)}
.status{display:inline-flex;align-items:center;gap:9px;font-family:var(--font-mono);font-size:12.5px}
.status .live{width:9px;height:9px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 4px rgba(34,197,94,.2);animation:pulse 2s infinite}
.foot-social{display:flex;gap:12px}
.foot-social a{width:38px;height:38px;border-radius:10px;background:rgba(255,255,255,.06);display:grid;place-items:center;transition:.25s}
.foot-social a:hover{background:var(--blue);transform:translateY(-3px)}
.foot-news{display:flex;gap:10px;margin-top:16px}
.foot-news input{flex:1;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:11px 14px;color:#fff;font-family:var(--font-body);font-size:14px}
.foot-news input::placeholder{color:rgba(255,255,255,.45)}
.foot-news button{background:var(--azure);color:#06283d;border:0;border-radius:10px;padding:0 18px;font-weight:700;cursor:pointer;font-family:var(--font-body);font-size:14px}
/* ===== Cinematic hero slider ===== */
.hero-slider{position:relative;min-height:760px;display:flex;align-items:center;overflow:hidden;color:#fff}
.hero-slide{position:absolute;inset:0;opacity:0;transition:opacity 1.1s ease;background-size:cover;background-position:center}
.hero-slide.active{opacity:1}
.hero-slide::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(7,16,31,.93) 0%,rgba(7,16,31,.74) 44%,rgba(7,16,31,.25) 100%)}
.hero-slider .container{position:relative;z-index:2;width:100%}
.hs-copy{position:relative;z-index:2;max-width:680px}
.hs-badge{display:inline-flex;align-items:center;gap:10px;background:rgba(56,189,248,.14);border:1px solid rgba(56,189,248,.3);border-radius:100px;padding:8px 16px;font-size:13.5px;font-weight:500;margin-bottom:26px;backdrop-filter:blur(6px)}
.hs-badge .dot{width:9px;height:9px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 4px rgba(34,197,94,.18);animation:pulse 2s infinite}
.hero-slider h1{font-size:clamp(40px,5.6vw,72px);margin-bottom:22px;color:#fff;line-height:1.05}
.hero-slider h1 .accent{color:var(--azure)}
.hero-slider p.lead{font-size:19px;color:rgba(255,255,255,.86);max-width:560px;margin-bottom:34px}
.hero-stats{display:flex;gap:36px;flex-wrap:wrap;margin-top:14px}
.hero-stats .s b{font-family:var(--font-display);font-size:32px;color:#fff}
.hero-stats .s span{font-size:13.5px;color:rgba(255,255,255,.7)}
.hs-dots{position:absolute;bottom:34px;left:0;right:0;z-index:3;display:flex;gap:12px;justify-content:center}
.hs-dots button{width:40px;height:5px;border-radius:5px;border:0;background:rgba(255,255,255,.3);cursor:pointer;transition:.3s;padding:0}
.hs-dots button.active{background:var(--azure);width:56px}
.hs-scroll{position:absolute;bottom:34px;right:34px;z-index:3;color:rgba(255,255,255,.55);font-size:11.5px;font-family:var(--font-mono);letter-spacing:.12em;writing-mode:vertical-rl;display:flex;align-items:center;gap:10px}
.hs-scroll::after{content:"";width:1px;height:44px;background:rgba(255,255,255,.4)}
/* ===== Rating strip ===== */
.rating-strip{display:flex;align-items:center;justify-content:center;gap:44px;flex-wrap:wrap;padding:38px 0;background:var(--cloud-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.rating-strip .rs{display:flex;align-items:center;gap:12px;font-family:var(--font-display);font-weight:600;color:var(--ink-2)}
.rating-strip .rs .stars{color:var(--amber);letter-spacing:2px;font-size:18px;line-height:1}
.rating-strip .rs small{display:block;font-family:var(--font-body);font-weight:400;font-size:12.5px;color:var(--slate)}
/* ===== Testimonials ===== */
.testi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.testi-card{background:var(--cloud);border:1px solid var(--line);border-radius:var(--radius);padding:32px 30px;display:flex;flex-direction:column;gap:18px;transition:.3s}
.testi-card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.testi-card .mark{font-family:var(--font-display);font-size:46px;line-height:.6;color:var(--azure);opacity:.5}
.testi-card .quote{color:var(--slate);font-size:15px;line-height:1.7}
.testi-card .who{display:flex;align-items:center;gap:14px;margin-top:auto}
.testi-card .av{width:46px;height:46px;border-radius:50%;background:linear-gradient(150deg,var(--blue),var(--azure));color:#fff;display:grid;place-items:center;font-family:var(--font-display);font-weight:700;font-size:16px;flex-shrink:0}
.testi-card .who b{font-family:var(--font-display);font-size:15px;display:block;color:var(--ink)}
.testi-card .who span{font-size:13px;color:var(--slate)}
.foot-social svg{width:18px;height:18px;color:#fff}
/* sub-page hero */
.page-hero{padding:160px 0 70px;background:
  radial-gradient(900px 500px at 90% -10%,rgba(56,189,248,.14),transparent 60%),
  radial-gradient(800px 500px at 0% 0%,rgba(11,95,204,.10),transparent 55%),
  linear-gradient(180deg,#fff 0%,var(--cloud) 100%)}
.page-hero h1{font-size:clamp(38px,5vw,60px);margin-bottom:18px;max-width:760px}
.page-hero p{font-size:19px;color:var(--slate);max-width:620px}
.breadcrumb{font-family:var(--font-mono);font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--slate-light);margin-bottom:20px}
.breadcrumb a{color:var(--blue)}
/* solution detail */
.sol{display:grid;grid-template-columns:.9fr 1.1fr;gap:60px;align-items:center;padding:80px 0;border-bottom:1px solid var(--line)}
.sol:nth-child(even){background:var(--cloud)}
.sol-rev{grid-template-columns:1.1fr .9fr}
.sol-rev .visual{order:2}
.sol-rev .copy{order:1}
.sol .copy .ic{width:60px;height:60px;border-radius:15px;background:linear-gradient(150deg,rgba(11,95,204,.12),rgba(56,189,248,.12));color:var(--blue);display:grid;place-items:center;margin-bottom:22px}
.sol .copy .ic svg{width:30px;height:30px}
.sol .copy h2{font-size:clamp(26px,3vw,38px)}
.sol .copy p.lead{color:var(--slate);font-size:17px;margin-bottom:22px}
.feat{display:grid;gap:14px}
.feat li{display:flex;gap:13px;font-size:15.5px;color:var(--ink-2)}
.feat li svg{width:20px;height:20px;color:var(--blue);flex-shrink:0;margin-top:3px}
.sol .visual{border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-lg);border:1px solid var(--line)}
.sol .visual img{width:100%;height:380px;object-fit:cover}
.sol-index{font-family:var(--font-mono);font-size:14px;color:var(--blue);font-weight:500;margin-bottom:12px;display:block}
/* stats band */
.stats-band{background:var(--ink);color:#fff;position:relative;overflow:hidden}
.stats-band::before{content:"";position:absolute;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(11,95,204,.4),transparent 70%);bottom:-200px;left:-120px}
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:30px;position:relative;z-index:1;text-align:center}
.stat b{font-family:var(--font-display);font-size:clamp(40px,5vw,58px);display:block;background:linear-gradient(120deg,#fff,var(--azure));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat span{font-size:14.5px;color:rgba(255,255,255,.75);font-family:var(--font-mono);letter-spacing:.05em}
/* projects */
.proj-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:26px}
.proj{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);transition:.3s}
.proj:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.proj .ph{height:230px;overflow:hidden;position:relative}
.proj .ph img{width:100%;height:100%;object-fit:cover;transition:.5s}
.proj:hover .ph img{transform:scale(1.05)}
.proj .ph .tag{position:absolute;top:16px;left:16px;background:rgba(10,20,38,.8);color:#fff;font-family:var(--font-mono);font-size:11.5px;letter-spacing:.05em;padding:6px 12px;border-radius:100px}
.proj .pb{padding:26px 28px 30px}
.proj .pb .meta{font-family:var(--font-mono);font-size:12.5px;color:var(--blue);margin-bottom:10px}
.proj .pb h3{font-size:21px;margin-bottom:10px}
.proj .pb p{font-size:14.5px;color:var(--slate);margin-bottom:16px}
.proj .pb .chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{font-size:12px;font-weight:500;color:var(--ink-2);background:var(--cloud-2);padding:5px 12px;border-radius:100px}
/* values */
.val-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.val{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:30px 28px;transition:.3s}
.val:hover{border-color:rgba(11,95,204,.3);transform:translateY(-5px);box-shadow:var(--shadow-md)}
.val .ic{width:50px;height:50px;border-radius:13px;background:rgba(11,95,204,.1);color:var(--blue);display:grid;place-items:center;margin-bottom:18px}
.val .ic svg{width:26px;height:26px}
.val h4{font-family:var(--font-display);font-size:19px;margin-bottom:9px}
.val p{font-size:14.5px;color:var(--slate)}
/* contact */
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:start}
.form-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:38px;box-shadow:var(--shadow-md)}
.field{margin-bottom:18px}
.field label{display:block;font-size:13.5px;font-weight:600;color:var(--ink-2);margin-bottom:7px}
.field input,.field textarea,.field select{width:100%;padding:13px 15px;border:1px solid var(--line);border-radius:11px;font-family:var(--font-body);font-size:15px;color:var(--ink);background:var(--cloud);transition:.2s}
.field input:focus,.field textarea:focus,.field select:focus{outline:none;border-color:var(--blue);background:#fff;box-shadow:0 0 0 4px rgba(11,95,204,.1)}
.field textarea{resize:vertical;min-height:120px}
.half{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.info-card{background:var(--ink);color:#fff;border-radius:var(--radius-lg);padding:38px;box-shadow:var(--shadow-lg)}
.info-card h3{font-size:24px;margin-bottom:8px}
.info-card p{color:rgba(255,255,255,.7);font-size:15px;margin-bottom:26px}
.info-row{display:flex;gap:14px;align-items:flex-start;padding:16px 0;border-top:1px solid rgba(255,255,255,.1)}
.info-row .ic{width:42px;height:42px;border-radius:11px;background:rgba(56,189,248,.15);color:var(--azure);display:grid;place-items:center;flex-shrink:0}
.info-row .ic svg{width:20px;height:20px}
.info-row b{font-family:var(--font-display);font-size:15.5px;display:block;margin-bottom:2px}
.info-row span{font-size:14px;color:rgba(255,255,255,.7)}
.map-wrap{border-radius:var(--radius-lg);overflow:hidden;border:1px solid var(--line);box-shadow:var(--shadow-md);margin-top:30px;height:340px}
.map-wrap iframe{width:100%;height:100%;border:0;display:block}
/* blog */
.blog-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.post{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);transition:.3s;display:flex;flex-direction:column}
.post:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.post .ph{height:200px;overflow:hidden}
.post .ph img{width:100%;height:100%;object-fit:cover}
.post .pb{padding:24px 26px 28px;display:flex;flex-direction:column;flex:1}
.post .meta{font-family:var(--font-mono);font-size:12.5px;color:var(--blue);margin-bottom:10px}
.post h3{font-size:20px;margin-bottom:10px;line-height:1.2}
.post p{font-size:14.5px;color:var(--slate);margin-bottom:16px;flex:1}
.post .more{font-size:13.5px;font-weight:600;color:var(--blue);display:inline-flex;align-items:center;gap:6px}
/* reveal */
.reveal{opacity:0;transform:translateY(28px);transition:.7s cubic-bezier(.2,.7,.3,1)}
.reveal.in{opacity:1;transform:none}
.reveal.d1{transition-delay:.08s}.reveal.d2{transition-delay:.16s}.reveal.d3{transition-delay:.24s}.reveal.d4{transition-delay:.32s}
@media(max-width:1024px){
  .svc-grid{grid-template-columns:repeat(2,1fr)}
  .steps{grid-template-columns:repeat(2,1fr)}
  .ind-grid{grid-template-columns:repeat(2,1fr)}
  .foot-grid{grid-template-columns:1fr 1fr}
  .stats-grid{grid-template-columns:repeat(2,1fr);gap:40px}
  .val-grid{grid-template-columns:repeat(2,1fr)}
  .blog-grid{grid-template-columns:repeat(2,1fr)}
  .sol,.sol-rev{grid-template-columns:1fr}
  .sol .visual img{height:300px}
}
@media(max-width:768px){
  .nav-links,.nav-cta .btn-ghost{display:none}
  .menu-btn{display:block}
  .hero-grid{grid-template-columns:1fr;gap:48px}
  .hero-visual img{height:340px}
  .why-grid{grid-template-columns:1fr;gap:40px}
  .why-visual img{height:340px}
  .section{padding:78px 0}
  .hero{padding:130px 0 60px}
  .page-hero{padding:130px 0 50px}
  .contact-grid{grid-template-columns:1fr;gap:30px}
  .proj-grid{grid-template-columns:1fr}
  .mobile-menu{display:flex}
}
.mobile-menu{display:none;flex-direction:column;background:#fff;border-bottom:1px solid var(--line);padding:14px 28px 22px;gap:6px;position:absolute;top:78px;left:0;right:0;box-shadow:var(--shadow-md);z-index:99}
.mobile-menu a{padding:11px 0;font-weight:500;border-bottom:1px solid var(--line)}
.mobile-menu a.active{color:var(--blue)}
.mobile-menu.open{display:flex}
@media(max-width:560px){
  .svc-grid,.steps,.ind-grid,.val-grid,.blog-grid{grid-template-columns:1fr}
  .hero-stats{gap:24px}
  .container{padding:0 20px}
  .half{grid-template-columns:1fr}
}
"""

# SVG icon snippets ---------------------------------------------------------
I = {
 "eye":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>',
 "flame":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2s5 5 5 10a5 5 0 0 1-10 0c0-5 5-10 5-10z"/></svg>',
 "lock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
 "home":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>',
 "speaker":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M19 5a9 9 0 0 1 0 14"/></svg>',
 "av":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
 "net":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><circle cx="5" cy="5" r="2"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><path d="M7 6.5l3 4M17 6.5l-3 4M7 17.5l3-4M17 17.5l-3-4"/></svg>',
 "wrench":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2-2 2.6-2.6z"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/></svg>',
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6L9 17l-5-5"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.81.36 1.6.7 2.34a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.74-1.27a2 2 0 0 1 2.11-.45c.74.34 1.53.57 2.34.7A2 2 0 0 1 22 16.92z"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "chat":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
 "bulb":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12c1 1 1 2 1 3h6c0-1 0-2 1-3a7 7 0 0 0-4-12z"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "handshake":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 17l2 2a1 1 0 0 0 3-3l-3-3M8 14l-2 2a1 1 0 0 0 3 3l2-2M3 11l4-4 4 4 4-4 4 4"/></svg>',
}

# ----------------------------------------------------------------------------
#  SHARED CHROME
# ----------------------------------------------------------------------------
def header(active="", transparent=False):
    links = [
        ("Home","index.html"),("About","about.html"),("Solutions","solutions.html"),
        ("Industries","industries.html"),("Projects","projects.html"),
        ("Contact","contact.html"),("Blog","blog.html"),
    ]
    def navlink(t, u):
        cls = ' class="active"' if u == active else ''
        return f'<a href="{u}"{cls}>{t}</a>'
    nav = "".join(navlink(t, u) for t, u in links)
    mm = nav
    solid_cls = "" if transparent else " header-solid"
    nav_cls = "nav-links on-dark" if transparent else "nav-links"
    return f"""
<header id="hdr" class="{solid_cls.strip()}">
  <div class="container nav">
    <a href="index.html" class="brand">
      <img class="logo" src="{ASSETS}/logo.png" alt="IRIS Fire & Security" />
      <img class="mono" src="{ASSETS}/monogram.png" alt="" />
    </a>
    <nav class="{nav_cls}">{nav}</nav>
    <div class="nav-cta">
      <a href="tel:+919996444222" class="btn btn-ghost">
        {I['phone']} +91 99964 44222
      </a>
      <a href="contact.html" class="btn btn-primary">Get a Quote</a>
      <button class="menu-btn" id="menuBtn" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="mobile-menu" id="mobileMenu">{mm}</div>
</header>"""

def footer():
    return f"""
<footer>
  <div class="container foot-grid">
    <div class="foot-brand">
      <img src="{ASSETS}/logo.png" alt="IRIS Fire & Security" />
      <p>A leading system integrator in electronic safety &amp; security, delivering best-value, reliable and service-backed protection across Delhi NCR for 14+ years.</p>
    </div>
    <div class="foot-col">
      <h5>Solutions</h5>
      <a href="solutions.html">Video Surveillance</a>
      <a href="solutions.html">Fire Alarm Systems</a>
      <a href="solutions.html">Access Control</a>
      <a href="solutions.html">Home Automation</a>
      <a href="solutions.html">AMC &amp; Maintenance</a>
    </div>
    <div class="foot-col">
      <h5>Company</h5>
      <a href="about.html">About IRIS</a>
      <a href="solutions.html">Solutions</a>
      <a href="industries.html">Industries</a>
      <a href="projects.html">Projects</a>
      <a href="blog.html">Blog</a>
    </div>
    <div class="foot-col foot-contact">
      <h5>Get in touch</h5>
      <div class="row">{I['phone']}<span>+91 99964 44222</span></div>
      <div class="row">{I['mail']}<span>iris.gurgaon@gmail.com</span></div>
      <div class="row">{I['pin']}<span>Gurgaon, Haryana — serving Delhi NCR</span></div>
      <form class="foot-news" onsubmit="event.preventDefault();this.innerHTML='<p style=&quot;color:var(--azure);font-size:14px&quot;>Thanks — we\\'ll be in touch.</p>'">
        <input type="email" placeholder="Your email" required aria-label="Email" />
        <button type="submit">Subscribe</button>
      </form>
    </div>
  </div>
  <div class="container foot-bottom">
    <span>&copy; 2026 IRIS Fire &amp; Security. All rights reserved.</span>
    <span class="status"><span class="live"></span> All monitored systems operational</span>
    <div class="foot-social">
      <a href="https://wa.me/919996444222" aria-label="WhatsApp">{I['phone']}</a>
      <a href="tel:+919996444222" aria-label="Call">{I['phone']}</a>
    </div>
  </div>
</footer>"""

JS = """
<script>
const hdr=document.getElementById('hdr');
const onScroll=()=>{hdr.classList.toggle('header-solid',window.scrollY>30)};
onScroll();window.addEventListener('scroll',onScroll,{passive:true});
const mb=document.getElementById('menuBtn'),mm=document.getElementById('mobileMenu');
if(mb){mb.addEventListener('click',()=>mm.classList.toggle('open'));
mm.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>mm.classList.remove('open')));}
const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.14});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
// hero slider
const slides=document.querySelectorAll('.hero-slide'),dots=document.querySelectorAll('#hsDots button');
if(slides.length){let i=0,timer;
const go=n=>{slides.forEach(s=>s.classList.remove('active'));dots.forEach(d=>d.classList.remove('active'));i=(n+slides.length)%slides.length;slides[i].classList.add('active');dots[i].classList.add('active')};
const next=()=>go(i+1);const play=()=>timer=setInterval(next,5500);
dots.forEach(d=>d.addEventListener('click',()=>{go(+d.dataset.i);clearInterval(timer);play()}));
play();}
</script>"""

def page(title, desc, body, active="", transparent=False):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" href="{ASSETS}/favicon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet" />
<style>{CSS}</style>
</head>
<body>
{header(active, transparent)}
{body}
{footer()}
{JS}
</body>
</html>"""

# ----------------------------------------------------------------------------
#  PAGE CONTENT
# ----------------------------------------------------------------------------

def home():
    body = f"""
<section class="hero-slider" id="top">
  <div class="hero-slide active" style="background-image:url('{ASSETS}/hero-tower.png')"></div>
  <div class="hero-slide" style="background-image:url('{ASSETS}/hero-soc.png')"></div>
  <div class="hero-slide" style="background-image:url('{ASSETS}/tech-cctv.png')"></div>
  <div class="container">
    <div class="hs-copy">
      <div class="hs-badge"><span class="dot"></span> 14+ years protecting Delhi NCR</div>
      <h1>The Innovation That<br><span class="accent">Keeps You Safe.</span></h1>
      <p class="lead">IRIS Fire &amp; Security is a leading system integrator delivering turnkey fire detection, video surveillance, access control and building automation &mdash; engineered and serviced in your backyard.</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-primary">{I['chat']} Request a Consultation</a>
        <a href="solutions.html" class="btn btn-ghost" style="background:rgba(255,255,255,.1);color:#fff;border-color:rgba(255,255,255,.35)">Explore Solutions</a>
      </div>
      <div class="hero-stats">
        <div class="s"><b>120+</b><span>Projects delivered</span></div>
        <div class="s"><b>80+</b><span>Active AMCs</span></div>
        <div class="s"><b>8</b><span>Product lines</span></div>
      </div>
    </div>
  </div>
  <div class="hs-dots" id="hsDots">
    <button class="active" data-i="0" aria-label="Slide 1"></button>
    <button data-i="1" aria-label="Slide 2"></button>
    <button data-i="2" aria-label="Slide 3"></button>
  </div>
  <div class="hs-scroll">SCROLL</div>
</section>
<div class="rating-strip">
  <div class="rs"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><div>4.8<span style="color:var(--amber)"> /5</span><small>Google Reviews</small></div></div>
  <div class="rs"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><div>4.7<span style="color:var(--amber)"> /5</span><small>JustDial</small></div></div>
  <div class="rs"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><div>120+<small>Happy clients</small></div></div>
  <div class="rs"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><div>14+<small>Years trusted</small></div></div>
</div>
<section class="section services">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">What we deliver</span>
      <h2>End-to-end safety &amp; security solutions</h2>
      <p>From a single camera to a fully integrated life-safety ecosystem &mdash; customized, scalable and built for investment protection.</p></div>
    <div class="svc-grid">
      {svc_card(I['eye'],'Video Surveillance','IP &amp; AI CCTV, remote monitoring and loss-prevention video analytics.')}
      {svc_card(I['flame'],'Fire Alarm &amp; Detection','Intelligent detection &amp; alarm across high-rises, commercial &amp; industrial sites.')}
      {svc_card(I['lock'],'Access Control &amp; Barriers','Biometric, card &amp; boom-barrier systems from single-door to enterprise.')}
      {svc_card(I['home'],'Building / Home Automation','HVAC, lighting &amp; blinds control that cuts energy use and lifts comfort.')}
      {svc_card(I['speaker'],'PA &amp; Communication','Public address, intercom &amp; emergency communication for any building size.')}
      {svc_card(I['av'],'AV Solutions','Audio-visual integration &mdash; conference, retail &amp; experience environments.')}
      {svc_card(I['net'],'IT / Networking','Structured cabling &amp; network backbone that keeps every system online.')}
      {svc_card(I['wrench'],'AMC &amp; Maintenance','Comprehensive &amp; standard AMCs with SLAs, spares and end-user training.')}
    </div>
  </div>
</section>
<section class="section">
  <div class="container why-grid">
    <div class="why-copy reveal">
      <span class="eyebrow">Why IRIS</span>
      <h2>Built on trust, technology &amp; total effort</h2>
      <p style="color:var(--slate);font-size:17px">We aggressively pursue a mix of product technology and technical support &mdash; delivering turnkey, customized and scalable solutions that protect your investment for the long run.</p>
      <div class="why-list">
        {why_item('01','Turnkey execution','Design, supply, install and commission &mdash; one accountable partner end to end.')}
        {why_item('02','Investment protection','Customized, scalable systems engineered to grow with your building.')}
        {why_item('03','Local, fast response','Gurgaon-based team with 80+ active AMCs and SLA-backed maintenance.')}
        {why_item('04','Honest relationships','Transparency, training and accountability &mdash; the values clients return for.')}
      </div>
    </div>
    <div class="why-visual reveal d2"><img src="{ASSETS}/tech-cctv.png" alt="IRIS technician installing surveillance" /></div>
  </div>
</section>
<section class="section process">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">How we work</span>
      <h2>From assessment to always-on</h2>
      <p>A disciplined four-step method that takes you from risk to resilient, monitored protection.</p></div>
    <div class="steps">
      {step('01','Assess','Site survey, risk profiling and a tailored system design for your exact environment.')}
      {step('02','Design &amp; Quote','Transparent, best-value proposal with the right technology &mdash; no oversell.')}
      {step('03','Install &amp; Integrate','Certified engineers deploy and integrate every subsystem into one platform.')}
      {step('04','Monitor &amp; Maintain','AMC-backed upkeep, training and 24/7 readiness keep you protected long-term.')}
    </div>
  </div>
</section>
<section class="section services">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Who we protect</span>
      <h2>Solutions for every environment</h2>
      <p>From corner shops to blue-chip campuses &mdash; one standard of protection, adapted to your sector.</p></div>
    <div class="ind-grid">
      {ind_card(f'{ASSETS}/ind-school.png','Education','Schools, colleges &amp; universities')}
      {ind_card(f'{ASSETS}/ind-hospital.png','Healthcare','Hospitals &amp; clinics')}
      {ind_card(f'{ASSETS}/ind-villa.png','Residential','Villas, apartments &amp; societies')}
      {ind_card(f'{ASSETS}/hero-tower.png','Commercial','Offices, malls &amp; towers')}
      {ind_card(f'{ASSETS}/hero-soc.png','Government','Departments &amp; public infra')}
      {ind_card(f'{ASSETS}/tech-cctv.png','Retail &amp; Enterprise','Stores, warehouses &amp; HQs')}
      {ind_card(f'{ASSETS}/ind-school.png','Banking &amp; Finance','Branches &amp; data centres')}
      {ind_card(f'{ASSETS}/ind-hospital.png','Industrial &amp; Manufacturing','Plants, warehouses &amp; yards')}
      {ind_card(f'{ASSETS}/ind-villa.png','Hospitality','Hotels, resorts &amp; banquets')}
    </div>
    <div style="text-align:center;margin-top:48px" class="reveal"><a href="industries.html" class="btn btn-primary">Explore all industries</a></div>
  </div>
</section>
<section class="section testi">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Client stories</span>
      <h2>Trusted by Delhi NCR's operators</h2>
      <p>Facility managers, builders and business owners who rely on IRIS to keep people and assets protected &mdash; day and night.</p></div>
    <div class="testi-grid">
      <div class="testi-card reveal">
        <div class="mark">&ldquo;</div>
        <p class="quote">IRIS delivered our full CCTV and fire-alarm upgrade across two buildings on a tight deadline. Clean execution, zero downtime, and the AMC response has been genuinely fast whenever we've needed them.</p>
        <div class="who"><div class="av">RS</div><div><b>R. Sharma</b><span>Facilities Head, Golf Course Road</span></div></div>
      </div>
      <div class="testi-card reveal d2">
        <div class="mark">&ldquo;</div>
        <p class="quote">We moved our society to IRIS for access control and surveillance. The team explained options without overselling, trained our staff, and the system has been rock-solid for over a year.</p>
        <div class="who"><div class="av">AK</div><div><b>A. Kapoor</b><span>RWA President, DLF Phase 3</span></div></div>
      </div>
      <div class="testi-card reveal d3">
        <div class="mark">&ldquo;</div>
        <p class="quote">From design to handover, IRIS handled our office automation and PA system as one accountable partner. Transparent pricing and a support line that actually picks up &mdash; rare in this trade.</p>
        <div class="who"><div class="av">MV</div><div><b>M. Verma</b><span>Director, Sohna Road SME</span></div></div>
      </div>
    </div>
  </div>
</section>
<section class="cta-band"><div class="container cta-inner">
  <div><h2>Ready to make your building safer?</h2>
    <p>Talk to our Gurgaon team for a free assessment and a no-obligation quote tailored to your site.</p></div>
  <div style="display:flex;gap:14px;flex-wrap:wrap">
    <a href="https://wa.me/919996444222?text=Hi%20I'm%20Interested%20In%20your%20Services" class="btn btn-amber">{I['phone']} WhatsApp Us</a>
    <a href="tel:+919996444222" class="btn btn-ghost" style="background:rgba(255,255,255,.12);color:#fff;border-color:rgba(255,255,255,.3)">Call +91 99964 44222</a>
  </div>
</div></section>"""
    return page("IRIS Fire & Security — Mission-Critical Fire & Security Solutions | Delhi NCR",
                "IRIS Fire & Security is a leading system integrator in electronic safety & security. Turnkey fire alarm, CCTV, access control, automation & AMC across Delhi NCR.",
                body, "index.html", transparent=True)

def svc_card(ic,title,desc):
    return f'<div class="svc reveal"><div class="ic">{ic}</div><h3>{title}</h3><p>{desc}</p><a class="more" href="solutions.html">Learn more &rarr;</a></div>'

def why_item(n,t,d):
    return f'<div class="why-item"><span class="num">{n}</span><div><h4>{t}</h4><p>{d}</p></div></div>'

def step(n,t,d):
    return f'<div class="step reveal"><div class="n">{n}</div><h4>{t}</h4><p>{d}</p></div>'

def ind_card(img,t,sub):
    return f'<div class="ind reveal"><img src="{img}" alt="{t}" /><div class="cap"><h4>{t}</h4><span>{sub}</span></div></div>'

# ---- About ----
def about():
    body = f"""
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Home</a> / About</div>
  <h1>A system integrator built on <span style="color:var(--blue)">trust &amp; total effort.</span></h1>
  <p>&ldquo;IRIS Fire &amp; Security&rdquo; is a leading System Integrator in the electronic safety &amp; security sector &mdash; known for best-value products, reliable quality and satisfactory after-sale service based on 14+ years of field experience.</p>
</div></section>
<section class="section"><div class="container why-grid">
  <div class="why-visual reveal"><img src="{ASSETS}/hero-soc.png" alt="IRIS security operations" /></div>
  <div class="why-copy reveal d2">
    <span class="eyebrow">Our story</span>
    <h2>Technology with a human touch</h2>
    <p style="color:var(--slate);font-size:17px;margin-bottom:18px">IRIS aggressively pursues a mix of product technology and technical support while providing turnkey solutions to our clients. We firmly believe in building a <em>long-lasting relationship</em> by providing customized and scalable solutions &mdash; thus ensuring investment protection.</p>
    <p style="color:var(--slate);font-size:17px">Our customers range from small corner shops and doctors&rsquo; practices to schools, universities and blue-chip enterprises as well as large government departments. Our positive attitude towards customer satisfaction through the right solutions and latest technology has driven continuous growth in the safety &amp; security industry.</p>
  </div>
</div></section>
<section class="section services"><div class="container">
  <div class="section-head reveal"><span class="eyebrow">Our values</span>
    <h2>What we stand for</h2>
    <p>IRIS is a company with strong values. We foster honest relationships with our customers, our suppliers, and within our company.</p></div>
  <div class="val-grid">
    {val_card(I['handshake'],'Excellent work ethics with trust','We do what we say &mdash; and we say what we do.')}
    {val_card(I['bulb'],'Dedicated to meet customer needs','Every engagement starts with your requirement, not our catalogue.')}
    {val_card(I['chat'],'Open communication &amp; transparency','You always know what you are buying, why, and what it costs.')}
    {val_card(I['users'],'Respect for every individual','From our engineers to your front-desk staff &mdash; everyone matters.')}
    {val_card(I['shield'],'High level of accountability','Clear ownership from design through commissioning and beyond.')}
    {val_card(I['home'],'Work as a team with clients','We treat your project as a shared objective, not a transaction.')}
  </div>
</div></section>
<section class="section stats-band"><div class="container">
  <div class="stats-grid reveal">
    <div class="stat"><b>120+</b><span>PROJECTS DELIVERED</span></div>
    <div class="stat"><b>80+</b><span>ACTIVE AMCs</span></div>
    <div class="stat"><b>8</b><span>PRODUCT LINES</span></div>
    <div class="stat"><b>40+</b><span>TEAM MEMBERS</span></div>
  </div>
</div></section>
<section class="cta-band"><div class="container cta-inner">
  <div><h2>Let&rsquo;s build something safe together</h2><p>Get a free site assessment from the IRIS team in Gurgaon.</p></div>
  <a href="contact.html" class="btn btn-amber">Get a Quote</a>
</div></section>"""
    return page("About IRIS Fire & Security — Leading System Integrator | Delhi NCR",
                "IRIS Fire & Security is a Delhi NCR system integrator with 14+ years of experience in electronic safety & security, built on trust, transparency and accountability.",
                body, "about.html")

def val_card(ic,t,d):
    return f'<div class="val reveal"><div class="ic">{ic}</div><h4>{t}</h4><p>{d}</p></div>'

# ---- Solutions ----
SOLUTIONS = [
 ("eye","Video Surveillance",f"{ASSETS}/tech-cctv.png",
  "Modern CCTV technology is turning video surveillance into one of the most valuable loss-prevention, remote-monitoring, security and management tools available today.",
  ["IP &amp; HD-TVI camera systems","AI analytics: intrusion, loitering, face &amp; number-plate recognition","Centralized remote monitoring &amp; mobile viewing","Video management &amp; evidence-grade storage"]),
 ("flame","Fire Alarm &amp; Detection",f"{ASSETS}/hero-soc.png",
  "IRIS delivers a wide range of fire alarm &amp; protection services across various applications including high-rise commercials, apartments and industrial sites.",
  ["Addressable &amp; conventional fire detection","Smoke, heat, beam &amp; flame detectors","Voice evacuation &amp; alarm panels","Compliance-ready design &amp; sign-off support"]),
 ("lock","Access Control &amp; Barrier Solutions",f"{ASSETS}/ind-villa.png",
  "IRIS works with a wide range of manufacturers to deliver advanced access control solutions &mdash; from simple keypads to enterprise biometric platforms.",
  ["Biometric, card &amp; mobile-credential access","Turnstiles, boom barriers &amp; bollards","Visitor management &amp; attendance","Integration with CCTV &amp; fire for lock-down"]),
 ("home","Building / Home Automation",f"{ASSETS}/ind-villa.png",
  "Home and building automation handles many tasks (HVAC, lights, blinds) that reduce energy consumption and improve the comfort level across your space.",
  ["Lighting, curtain &amp; climate control","Scene &amp; schedule automation","Energy monitoring &amp; savings","App &amp; voice control"]),
 ("speaker","Communication &amp; PA System",f"{ASSETS}/hero-soc.png",
  "IRIS offers the most extensive range of communication systems in a variety of standard and digital designs to handle the needs of small to large businesses.",
  ["Public address &amp; background music","Emergency &amp; evacuation voice systems","Intercom &amp; nurse-call","IP-based paging across campuses"]),
 ("av","AV Solutions",f"{ASSETS}/ind-school.png",
  "IRIS offers Audio Visual Systems Integration (AVSI) solutions, services and support &mdash; fully customized as per client requirements.",
  ["Conference &amp; meeting-room systems","Digital signage &amp; displays","Lecture capture &amp; classrooms","Experience &amp; experience centres"]),
 ("net","IT / Networking Infrastructure",f"{ASSETS}/hero-tower.png",
  "A reliable network backbone is what keeps every security subsystem online. IRIS designs and installs structured cabling and active networking.",
  ["Structured cabling (Cat6/6A, fibre)","Network switches, Wi-Fi &amp; VLANs","PoE design for cameras &amp; access","Surveillance-grade storage &amp; NVRs"]),
 ("wrench","AMC &amp; Maintenance Services",f"{ASSETS}/tech-cctv.png",
  "IRIS undertakes Annual Maintenance Contracts (AMCs) with service-level commitments (SLAs) for projects executed by us and those installed by others.",
  ["Standard &amp; Comprehensive AMCs","SLA-backed response &amp; uptime","Spares &amp; non-repairable replacement","End-user &amp; train-the-trainer programs"]),
]

def solutions():
    rows=""
    for i,(ic,t,img,lead,feats) in enumerate(SOLUTIONS):
        rev = ' sol-rev' if i%2 else ''
        fl = "".join(f'<li>{I["check"]}{f}</li>' for f in feats)
        rows += f"""
<div class="sol{rev} reveal">
  <div class="visual"><img src="{img}" alt="{t}" /></div>
  <div class="copy">
    <span class="sol-index">SOLUTION {str(i+1).zfill(2)}</span>
    <div class="ic">{ic}</div>
    <h2>{t}</h2>
    <p class="lead">{lead}</p>
    <ul class="feat">{fl}</ul>
  </div>
</div>"""
    body = f"""
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Home</a> / Solutions</div>
  <h1>Eight integrated solutions.<br><span style="color:var(--blue)">One accountable partner.</span></h1>
  <p>Each system is delivered turnkey and designed to integrate into a single, monitored platform &mdash; protecting your investment as you grow.</p>
</div></section>
<section class="section" style="padding-top:60px">{rows}</section>
<section class="cta-band"><div class="container cta-inner">
  <div><h2>Not sure which solution you need?</h2><p>Our Gurgaon engineers will assess your site and recommend the right mix.</p></div>
  <a href="contact.html" class="btn btn-amber">Book a free assessment</a>
</div></section>"""
    return page("Solutions — IRIS Fire & Security | CCTV, Fire, Access Control, Automation",
                "Explore IRIS Fire & Security's eight integrated solutions: video surveillance, fire alarm, access control, automation, PA, AV, networking and AMC across Delhi NCR.",
                body, "solutions.html")

# ---- Industries ----
INDUSTRIES = [
 (f"{ASSETS}/ind-school.png",'Education','Schools, colleges &amp; universities',
  'Campus-wide CCTV, access control for labs and dorms, PA for emergency drills, and fire safety compliant with education norms.'),
 (f"{ASSETS}/ind-hospital.png",'Healthcare','Hospitals &amp; clinics',
  'Patient-zone access, nurse-call integration, smoke detection and uninterrupted power for life-safety systems.'),
 (f"{ASSETS}/ind-villa.png",'Residential','Villas, apartments &amp; societies',
  'Gated-community surveillance, visitor management, home automation and boom barriers for apartments and villas.'),
 (f"{ASSETS}/hero-tower.png",'Commercial','Offices, malls &amp; towers',
  'Enterprise access, intelligent video, fire alarm and building automation for high-rise commercial assets.'),
 (f"{ASSETS}/hero-soc.png",'Government','Departments &amp; public infra',
  'Perimeter security, command-and-control rooms, PA and integrated monitoring for public-sector facilities.'),
 (f"{ASSETS}/tech-cctv.png",'Retail &amp; Enterprise','Stores, warehouses &amp; HQs',
  'Loss-prevention analytics, people counting, access and central monitoring across multiple sites.'),
]
def industries():
    cards = "".join(
        f'<div class="ind reveal d{(i%3)+1}"><img src="{img}" alt="{t}" /><div class="cap"><h4>{t}</h4><span>{sub}</span></div><p style="position:relative;z-index:1;color:rgba(255,255,255,.85);padding:0 24px 24px;font-size:14.5px">{d}</p></div>'
        for i,(img,t,sub,d) in enumerate(INDUSTRIES)
    )
    body = f"""
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Home</a> / Industries</div>
  <h1>One standard of protection,<br><span style="color:var(--blue)">adapted to your sector.</span></h1>
  <p>From corner shops to blue-chip campuses &mdash; IRIS tailors the same trusted systems to the realities of your environment.</p>
</div></section>
<section class="section services"><div class="container"><div class="ind-grid">
  {cards}
</div><div style="text-align:center;margin-top:48px" class="reveal"><a href="solutions.html" class="btn btn-primary">See the solutions</a></div></div></section>
<section class="cta-band"><div class="container cta-inner">
  <div><h2>Tell us about your site</h2><p>We&rsquo;ll map the right solution set to your industry and risk profile.</p></div>
  <a href="contact.html" class="btn btn-amber">Talk to an engineer</a>
</div></section>"""
    return page("Industries Served — IRIS Fire & Security | Education to Government",
                "IRIS Fire & Security serves education, healthcare, residential, commercial, government and retail sectors across Delhi NCR with tailored fire & security systems.",
                body, "industries.html")

# ---- Projects ----
PROJECTS = [
 (f"{ASSETS}/hero-tower.png",'Commercial','High-Rise Commercial Tower','NCR','Integrated fire alarm, 200+ IP cameras and enterprise access control across a 30-floor Grade-A tower.',['Fire','CCTV','Access']),
 (f"{ASSETS}/ind-school.png",'Education','K-12 School Campus','Gurgaon','Campus-wide surveillance, PA for emergency drills and perimeter access for 1,800 students.',['CCTV','PA','Access']),
 (f"{ASSETS}/ind-hospital.png",'Healthcare','Multi-Speciality Hospital','Delhi','Patient-zone access, nurse-call integration and addressable fire detection across 8 floors.',['Access','Fire','AV']),
 (f"{ASSETS}/ind-villa.png",'Residential','Gated Villa Society','Gurgaon','Boom barriers, visitor management and home automation for 120 premium residences.',['Barriers','Automation','CCTV']),
 (f"{ASSETS}/hero-soc.png",'Government','Public Sector Command Room','NCR','Centralized monitoring room with video wall, PA and integrated alerting for a government facility.',['CCTV','PA','Network']),
 (f"{ASSETS}/tech-cctv.png",'Retail','Retail Chain (Multi-Site)','Delhi NCR','Loss-prevention analytics and central monitoring rolled out across 14 retail outlets.',['CCTV','Analytics','Network']),
]
def projects():
    cards = "".join(
        f'''<div class="proj reveal d{(i%3)+1}"><div class="ph"><span class="tag">{sector}</span><img src="{img}" alt="{t}" /></div>
        <div class="pb"><div class="meta">{loc} &middot; {sector}</div><h3>{t}</h3><p>{d}</p>
        <div class="chips">{''.join(f'<span class="chip">{c}</span>' for c in chips)}</div></div></div>'''
        for i,(img,sector,t,loc,d,chips) in enumerate(PROJECTS)
    )
    body = f"""
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Home</a> / Projects</div>
  <h1>120+ projects.<br><span style="color:var(--blue)">One promise &mdash; done right.</span></h1>
  <p>A snapshot of turnkey deployments across Delhi NCR. Client names are withheld for confidentiality &mdash; references available on request.</p>
</div></section>
<section class="section"><div class="container"><div class="proj-grid">
  {cards}
</div></div></section>
<section class="cta-band"><div class="container cta-inner">
  <div><h2>Want a reference visit?</h2><p>We&rsquo;ll arrange a site visit to a comparable project near you.</p></div>
  <a href="contact.html" class="btn btn-amber">Request references</a>
</div></section>"""
    return page("Projects & Case Studies — IRIS Fire & Security | Delhi NCR Deployments",
                "Explore IRIS Fire & Security project case studies across commercial, education, healthcare, residential, government and retail sectors in Delhi NCR.",
                body, "projects.html")

# ---- Contact ----
def contact():
    thanks = ("event.preventDefault();"
        "this.innerHTML='<div style=\\'padding:30px 0;text-align:center\\'>"
        "<div style=\\'width:54px;height:54px;border-radius:50%;background:rgba(34,197,94,.12);color:#22C55E;display:grid;place-items:center;margin:0 auto 16px;font-size:26px\\'>✓</div>"
        "<h3 style=\\'font-family:var(--font-display);margin-bottom:8px\\'>Thank you!</h3>"
        "<p style=\\'color:var(--slate)\\'>Our team will reach out within one business day.</p></div>';")
    body = f"""
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Home</a> / Contact</div>
  <h1>Let&rsquo;s make your building <span style="color:var(--blue)">safer.</span></h1>
  <p>Tell us about your site and we&rsquo;ll get back with a free assessment and a no-obligation quote.</p>
</div></section>
<section class="section"><div class="container contact-grid">
  <div class="reveal">
    <div class="form-card">
      <form onsubmit="{thanks}">
        <div class="half">
          <div class="field"><label>Full Name *</label><input type="text" required placeholder="Your name" /></div>
          <div class="field"><label>Mobile Number *</label><input type="tel" required placeholder="+91 ..." /></div>
        </div>
        <div class="field"><label>Email</label><input type="email" placeholder="you@company.com" /></div>
        <div class="field"><label>Interested in</label>
          <select><option>Video Surveillance</option><option>Fire Alarm &amp; Detection</option><option>Access Control &amp; Barriers</option><option>Building / Home Automation</option><option>PA &amp; Communication</option><option>AV Solutions</option><option>IT / Networking</option><option>AMC &amp; Maintenance</option><option>Full turnkey project</option></select></div>
        <div class="field"><label>Your Message</label><textarea placeholder="Tell us about your site, size and timeline..."></textarea></div>
        <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Send Enquiry</button>
      </form>
    </div>
  </div>
  <div class="reveal d2">
    <div class="info-card">
      <h3>IRIS Fire &amp; Security</h3>
      <p>Gurgaon-based, serving Delhi NCR. Reach us directly &mdash; we typically respond within one business day.</p>
      <div class="info-row"><div class="ic">{I['phone']}</div><div><b>Call / WhatsApp</b><span>+91 99964 44222</span></div></div>
      <div class="info-row"><div class="ic">{I['mail']}</div><div><b>Email</b><span>iris.gurgaon@gmail.com</span></div></div>
      <div class="info-row"><div class="ic">{I['pin']}</div><div><b>Service area</b><span>Gurgaon, Haryana &mdash; serving Delhi NCR</span></div></div>
      <div class="info-row"><div class="ic">{I['chat']}</div><div><b>Response time</b><span>Within 1 business day</span></div></div>
    </div>
    <div class="map-wrap" style="position:relative;background:linear-gradient(135deg,#0A1426,#10203B);display:grid;place-items:center">
      <div style="position:absolute;inset:0;background-image:radial-gradient(rgba(56,189,248,.18) 1px,transparent 1px);background-size:34px 34px;opacity:.5"></div>
      <div style="position:relative;text-align:center;color:#fff;padding:30px">
        <div style="width:62px;height:62px;border-radius:16px;margin:0 auto 18px;background:rgba(56,189,248,.15);color:#38BDF8;display:grid;place-items:center">{I['pin']}</div>
        <h3 style="font-family:var(--font-display);font-size:22px;margin-bottom:8px">Gurgaon, Haryana</h3>
        <p style="color:rgba(255,255,255,.72);font-size:14.5px;margin-bottom:20px">Serving Delhi NCR &mdash; Gurgaon, Faridabad, Noida &amp; Delhi</p>
        <a href="https://www.google.com/maps/search/?api=1&query=Gurgaon,Haryana,India" target="_blank" rel="noopener" class="btn btn-amber" style="background:#38BDF8;color:#06283d">{I['pin']} Open in Google Maps</a>
      </div>
    </div>
  </div>
</div></section>"""
    return page("Contact IRIS Fire & Security — Free Assessment | Gurgaon, Delhi NCR",
                "Contact IRIS Fire & Security in Gurgaon for a free site assessment and quote. Call/WhatsApp +91 99964 44222 or email iris.gurgaon@gmail.com.",
                body, "contact.html")

# ---- Blog ----
POSTS = [
 (f"{ASSETS}/tech-cctv.png",'December 24, 2019','IP CCTV Camera Advantages','IP stands for Internet Protocol. IP CCTV cameras utilize the internet to transmit digital video &mdash; unlocking remote viewing, higher resolution and smarter analytics than analog systems.',"https://irisfireandsecurity.com/ip-cctv-camera-advantages/"),
 (f"{ASSETS}/ind-school.png",'December 24, 2019','Benefits of CCTV Cameras in Schools','CCTV cameras are becoming increasingly used in schools to safeguard students, deter bullying and support staff &mdash; when deployed with the right privacy safeguards.',"https://irisfireandsecurity.com/nanotech-immersion-along-the-highway-2/"),
 (f"{ASSETS}/hero-tower.png",'December 24, 2019','How to Find the Best CCTV Camera for Home & Office','Choosing the right camera means matching resolution, lens, storage and night-vision to your space. We break down the essentials so you buy what you actually need.',"https://irisfireandsecurity.com/3-ways-to-position-your-business-growth/"),
]
def blog():
    cards = "".join(
        f'''<div class="post reveal d{(i%3)+1}"><div class="ph"><img src="{img}" alt="{t}" /></div>
        <div class="pb"><div class="meta">{date} &middot; IRIS</div><h3>{t}</h3><p>{d}</p>
        <a class="more" href="{url}" target="_blank" rel="noopener">Read more &rarr;</a></div></div>'''
        for i,(img,date,t,d,url) in enumerate(POSTS)
    )
    body = f"""
<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Home</a> / Blog</div>
  <h1>Insights on fire &amp; <span style="color:var(--blue)">security.</span></h1>
  <p>Practical guidance from the IRIS team &mdash; helping you choose and maintain the right protection.</p>
</div></section>
<section class="section"><div class="container"><div class="blog-grid">
  {cards}
</div></div></section>
<section class="cta-band"><div class="container cta-inner">
  <div><h2>Have a question for our team?</h2><p>Reach out &mdash; we&rsquo;re happy to advise, no obligation.</p></div>
  <a href="contact.html" class="btn btn-amber">Contact us</a>
</div></section>"""
    return page("Blog — IRIS Fire & Security | CCTV, Fire & Security Insights",
                "Read IRIS Fire & Security blog insights on IP CCTV cameras, school safety, and choosing the right CCTV for home and office.",
                body, "blog.html")

# ----------------------------------------------------------------------------
#  BUILD
# ----------------------------------------------------------------------------
PAGES = {
 "index.html": home(),
 "about.html": about(),
 "solutions.html": solutions(),
 "industries.html": industries(),
 "projects.html": projects(),
 "contact.html": contact(),
 "blog.html": blog(),
}

if __name__ == "__main__":
    for name, html in PAGES.items():
        out = os.path.join(ROOT, name)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  wrote {name:18s} {len(html):>7,} bytes")
    print(f"\nDone. {len(PAGES)} pages in {ROOT}")
