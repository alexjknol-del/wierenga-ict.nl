#!/usr/bin/env python3
# Generator voor wierenga-ict.nl - onafhankelijke kennisgids over ICT en digitale veiligheid voor het mkb.
import os, json, html, hashlib
def _ver(p):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),p),'rb').read()).hexdigest()[:8]
    except Exception: return "1"
BASE="https://wierenga-ict.nl"; SITE="Wierenga ICT"; EMAIL="info@wierenga-ict.nl"
AUTEUR="Joost Wierenga"; AUTEUR_ROL="Redacteur ICT"
SRC=os.path.dirname(__file__); OUT=os.path.join(SRC,"site"); CSS_VER=_ver("assets/css/style.css")
def esc(s): return html.escape(str(s), quote=True)
DISC="Dit artikel geeft algemene informatie. Elke omgeving verschilt, en een maatregel die in de ene situatie werkt kan elders ongewenste gevolgen hebben. Bij ingrijpende wijzigingen is toetsing door een ICT-beheerder verstandig."

IC={
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="14" rx="2"/><path d="M8 21h8"/><path d="M12 18v3"/></svg>',
 "scale":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 4h-3a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5H20z"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}
NAV=[("Home","/"),("Onderwerpen","/onderwerpen/"),("Gidsen","/gidsen/"),("Nieuws","/nieuws/"),("Over","/over/"),("Partners","/partners/"),("Contact","/contact/")]

def head(t,d,path,ld=None):
    can=BASE+path
    j="".join('<script type="application/ld+json">'+json.dumps(b,ensure_ascii=False)+'</script>' for b in (ld or []))
    nav="".join(f'<a class="navlink" href="{h}">{esc(l)}</a>' for l,h in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)}</title><meta name="description" content="{esc(d)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website"><meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}"><meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(d)}"><meta property="og:url" content="{can}">
<meta name="theme-color" content="#26315B">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}</head><body>
<header class="site-head"><nav class="nav" id="nav">
  <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Wierenga ICT</b><span>Kennisgids</span></span></a>
  {nav}
  <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
</nav></header>
"""

def footer():
    return f"""<footer class="foot"><div class="wrap"><div class="cols">
  <div><a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Wierenga ICT</b><span style="color:#7C89A8">Kennisgids</span></span></a>
    <p class="note">Wierenga ICT is een onafhankelijke kennisgids over ICT en digitale veiligheid voor kleine en middelgrote organisaties. Het platform levert geen diensten en verkoopt geen software.</p></div>
  <div><h4>Kennis</h4><a href="/onderwerpen/">Onderwerpen</a><a href="/gidsen/">Gidsen</a><a href="/nieuws/">Nieuws</a><a href="/redactie/">Over de redactie</a></div>
  <div><h4>Informatie</h4><a href="/over/">Over dit platform</a><a href="/contact/">Contact</a><a href="/privacybeleid/">Privacybeleid</a><a href="/cookiebeleid/">Cookiebeleid</a></div>
</div><div class="foot-bottom"><span>&copy; 2026 {esc(SITE)}</span>
<span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span></div></div></footer>
</body></html>"""

def crumb(i): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":k+1,"name":n,"item":BASE+u} for k,(n,u) in enumerate(i)]}
def crumbs_html(i):
    o=[f'<a href="{u}">{esc(n)}</a>' for n,u in i[:-1]]; o.append(f'<span>{esc(i[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(o)+'</nav></div>'
def write(path,c):
    f=os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(f),exist_ok=True); open(f,"w",encoding="utf-8").write(c)
def blocks(bs):
    o=[]
    for b in bs:
        if b[0]=="p": o.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="h2": o.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": o.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": o.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
    return "".join(o)
def byline(): return f'<div class="byline"><img src="/assets/img/auteur.svg" alt="{esc(AUTEUR)}"><div class="who">{esc(AUTEUR)}<small>{esc(AUTEUR_ROL)}</small></div></div>'

ONDERWERPEN=[
 {"slug":"back-up-en-herstel","naam":"Back-up en herstel",
  "resume":"Een back-up die nooit is teruggezet, is geen back-up. Het herstel is het onderdeel dat in de praktijk faalt.",
  "specs":[("Regel","3-2-1"),("Test","Periodiek"),("Bewaartijd","Meerdere versies")],
  "secties":[("De 3-2-1-regel","Drie kopieën van de gegevens, op twee verschillende soorten opslag, waarvan één op een andere locatie. Die derde kopie is bedoeld voor gebeurtenissen die de hele locatie treffen, zoals brand, waterschade of gijzelsoftware die zich over het netwerk verspreidt."),
   ("Waarom herstel getest moet worden","Een back-uptaak die groen afmeldt zegt alleen dat het kopiëren is gelukt, niet dat de gegevens bruikbaar zijn. Periodiek een bestand of een volledige map daadwerkelijk terugzetten legt problemen bloot die anders pas op het slechtst denkbare moment zichtbaar worden."),
   ("Versies en bewaartermijn","Een enkele actuele kopie beschermt niet tegen bestanden die dagen geleden zijn beschadigd of versleuteld. Meerdere versies over een langere periode maken het mogelijk terug te gaan naar een moment vóór het probleem ontstond.")],
  "punten":["Drie kopieën, twee soorten opslag, één extern","Herstel periodiek testen, niet alleen de back-up","Meerdere versies bewaren","Een offline of onveranderlijke kopie is de laatste redding"]},
 {"slug":"phishing-en-e-mail","naam":"Phishing en e-mailbeveiliging",
  "resume":"De meeste incidenten beginnen bij een e-mail. Techniek vangt veel af, maar niet alles.",
  "specs":[("Records","SPF, DKIM, DMARC"),("Melden","Vast aanspreekpunt"),("Training","Herhaald")],
  "secties":[("Wat SPF, DKIM en DMARC doen","SPF legt vast welke servers namens een domein mogen verzenden, DKIM voegt een handtekening toe die onderweg controleerbaar blijft, en DMARC bepaalt wat er gebeurt als een bericht niet aan die eisen voldoet. Samen maken ze het aanzienlijk moeilijker om berichten te versturen die van een organisatie lijken te komen."),
   ("Waar techniek ophoudt","Een phishingbericht dat vanaf een gecompromitteerd account van een echte leverancier wordt verstuurd, doorstaat alle controles. Daarom blijft een proces nodig: een tweede verificatie via een bekend telefoonnummer bij wijzigingen in rekeningnummers of betalingen."),
   ("Melden zonder drempel","Medewerkers die bang zijn een fout te melden, melden later of niet. Een cultuur waarin een gemelde misklik zonder verwijt wordt opgepakt, levert meer beveiliging op dan een extra filter.")],
  "punten":["SPF, DKIM en DMARC correct instellen","Betaalwijzigingen altijd via een tweede kanaal verifiëren","Melden moet drempelloos zijn","Herhaalde training werkt beter dan eenmalig"]},
 {"slug":"wachtwoorden-en-tweefactor","naam":"Wachtwoorden en tweefactor",
  "resume":"Een uniek wachtwoord per dienst en een tweede factor vangen samen het grootste deel van de aanvallen af.",
  "specs":[("Beheer","Wachtwoordmanager"),("Tweede factor","App of sleutel"),("Wisselen","Alleen bij verdenking")],
  "secties":[("Hergebruik is het kernprobleem","Wanneer een dienst wordt gelekt, worden de buitgemaakte combinaties elders geprobeerd. Een uniek wachtwoord per dienst beperkt de schade tot die ene dienst. Een wachtwoordmanager maakt dat praktisch haalbaar zonder dat iemand tientallen reeksen hoeft te onthouden."),
   ("Verplicht wisselen werkt averechts","Het periodiek verplicht wijzigen van wachtwoorden leidt tot voorspelbare varianten met een oplopend cijfer. Actuele richtlijnen adviseren wijzigen alleen bij aanwijzingen van misbruik, in combinatie met lengte en uniciteit."),
   ("Niet elke tweede factor is gelijk","Een code per sms is te onderscheppen bij overname van een telefoonnummer. Een authenticatie-app is aanzienlijk sterker, en een fysieke sleutel biedt de beste bescherming tegen phishing omdat die de website controleert voordat er iets wordt vrijgegeven.")],
  "punten":["Uniek wachtwoord per dienst","Wachtwoordmanager maakt dat werkbaar","Alleen wisselen bij verdenking","Fysieke sleutel is sterker dan sms"]},
 {"slug":"updates-en-patchbeheer","naam":"Updates en patchbeheer",
  "resume":"Bekende, niet gedichte kwetsbaarheden vormen een groter risico dan onbekende zwakke plekken.",
  "specs":[("Inventaris","Alles in beeld"),("Ritme","Vast moment"),("Uitzonderingen","Vastgelegd")],
  "secties":[("Eerst weten wat er draait","Een organisatie kan niet bijwerken wat niet in beeld is. Naast werkplekken en servers gaat het om netwerkapparatuur, printers, camera's en apparaten die ooit zijn aangesloten en vergeten. Een actuele inventaris is de basis van elk patchbeleid."),
   ("Vast ritme met ruimte voor spoed","Een vast moment per maand geeft voorspelbaarheid en maakt testen mogelijk. Daarnaast is een spoedprocedure nodig voor kwetsbaarheden die actief worden misbruikt, waarbij wachten op het volgende moment te lang duurt."),
   ("Einde ondersteuning","Apparatuur en software waarvoor geen updates meer verschijnen, blijven kwetsbaar zonder dat daar iets aan te doen is. Het einde van de ondersteuning hoort in de inventaris te staan, zodat vervanging tijdig wordt ingepland.")],
  "punten":["Inventaris is de basis","Vast ritme plus een spoedprocedure","Testen voor uitrol op alle werkplekken","Einde ondersteuning vooraf inplannen"]},
 {"slug":"cloud-of-lokaal","naam":"Cloud of lokaal",
  "resume":"De keuze draait zelden om kosten alleen, en veel vaker om beheerlast, herstelmogelijkheden en afhankelijkheid.",
  "specs":[("Beheer","Verschuift"),("Kosten","Investering of abonnement"),("Uitwijk","Contractueel")],
  "secties":[("Wat er verschuift","Bij een clouddienst neemt de leverancier onderhoud, beschikbaarheid en een deel van de beveiliging over. Wat blijft liggen bij de organisatie zijn toegangsbeheer, gegevensclassificatie en, in veel gevallen, de back-up van de eigen gegevens. Dat laatste wordt vaak verkeerd ingeschat."),
   ("Gedeelde verantwoordelijkheid","Vrijwel alle grote aanbieders werken met een model waarin de leverancier de infrastructuur beschermt en de klant verantwoordelijk blijft voor de eigen gegevens en instellingen. Het verwijderen van een bestand door een medewerker valt daarmee buiten de bescherming van de leverancier."),
   ("Afhankelijkheid en uitstappen","Voordat een dienst in gebruik wordt genomen, is de vraag hoe gegevens er weer uit komen minstens zo belangrijk als de vraag hoe ze erin komen. Exportmogelijkheden en de opzegtermijn horen vooraf duidelijk te zijn.")],
  "punten":["Beheer verschuift, verantwoordelijkheid deels niet","Eigen back-up blijft vaak nodig","Exportmogelijkheden vooraf controleren","Toegangsbeheer blijft altijd eigen taak"]},
 {"slug":"avg-en-gegevensbeveiliging","naam":"AVG en gegevensbeveiliging",
  "resume":"De wet vraagt passende maatregelen, en dat begrip krijgt invulling door wat gangbaar en haalbaar is.",
  "specs":[("Basis","Register"),("Melden","72 uur"),("Verwerkers","Overeenkomst")],
  "secties":[("Beginnen bij het overzicht","Een verwerkingsregister legt vast welke persoonsgegevens worden verwerkt, waarom, hoe lang en met wie ze worden gedeeld. Dat overzicht is niet alleen een verplichting, het maakt ook duidelijk welke systemen extra bescherming verdienen."),
   ("Datalek en de meldtermijn","Bij een datalek met risico voor betrokkenen geldt een meldplicht bij de Autoriteit Persoonsgegevens binnen 72 uur na ontdekking. Die termijn loopt door in het weekend, wat vraagt om een vooraf belegd aanspreekpunt in plaats van improvisatie op het moment zelf."),
   ("Verwerkersovereenkomsten","Met elke partij die namens de organisatie persoonsgegevens verwerkt, van een hostingpartij tot een salarisadministratie, is een verwerkersovereenkomst nodig. Die legt vast wat de partij wel en niet mag en welke beveiliging is afgesproken.")],
  "punten":["Verwerkingsregister als vertrekpunt","Meldtermijn van 72 uur na ontdekking","Verwerkersovereenkomst met elke partij","Bewaartermijnen vastleggen en naleven"]},
]
def onderwerp(s): return next(x for x in ONDERWERPEN if x["slug"]==s)

GIDSEN=[
 {"slug":"eerste-uur-bij-een-incident","titel":"Het eerste uur bij een digitaal incident","ic":"scale",
  "resume":"De eerste beslissingen bepalen hoeveel bewijs bewaard blijft en hoe ver de schade zich verspreidt.",
  "body":[("p","Bij een vermoeden van gijzelsoftware of een ingebroken account telt snelheid, maar overhaaste stappen vernietigen sporen die later nodig zijn om vast te stellen wat er is gebeurd."),
   ("h2","Isoleren zonder uitschakelen"),("p","Een besmet systeem loskoppelen van het netwerk beperkt verspreiding. Uitzetten wist het werkgeheugen, waarin vaak precies de informatie zit die nodig is voor onderzoek. Loskoppelen van de netwerkkabel of het uitschakelen van de draadloze verbinding heeft daarom de voorkeur boven afsluiten."),
   ("h2","Wat direct gebeurt"),("ul",["Getroffen systemen van het netwerk halen, zonder ze uit te zetten.","Back-ups loskoppelen zodat die niet worden meegenomen.","Wachtwoorden van beheeraccounts wijzigen vanaf een schoon systeem.","Vastleggen wie wat wanneer heeft gedaan."]),
   ("h2","Wie er wordt ingelicht"),("p","Naast de eigen ICT-partij zijn dat mogelijk de Autoriteit Persoonsgegevens bij een datalek, de verzekeraar bij een cyberpolis, en klanten of leveranciers waarvan gegevens zijn geraakt. Aangifte bij de politie is in veel gevallen ook aan de orde."),
   ("callout","Betalen bij gijzelsoftware biedt geen garantie op herstel en houdt het verdienmodel in stand. De aanbeveling van opsporingsdiensten is niet te betalen en eerst te onderzoeken of herstel uit back-up mogelijk is."),
   ("h2","Daarna pas herstellen"),("p","Herstellen naar dezelfde omgeving zonder te weten hoe de toegang is verkregen, leidt geregeld tot een tweede incident. Eerst vaststellen hoe het is gebeurd, dan pas terugzetten."),
   ("p",DISC)]},
 {"slug":"ict-leverancier-kiezen","titel":"Een ICT-leverancier kiezen: waar het op vastloopt","ic":"doc",
  "resume":"Niet de prijs per werkplek, maar de afspraken over beschikbaarheid en vertrek bepalen de werkelijke kosten.",
  "body":[("p","Een ICT-contract loopt meestal jaren en raakt vrijwel elk bedrijfsproces. De punten die achteraf voor problemen zorgen, staan zelden op de offerte."),
   ("h2","Reactietijd en oplostijd"),("p","Een reactietijd zegt alleen iets over hoe snel er wordt gereageerd, niet over wanneer iets is opgelost. Afspraken die alleen een reactietijd noemen, geven geen zekerheid. Ook telt wat er buiten kantooruren geldt en wat als spoed wordt aangemerkt."),
   ("h2","Eigenaarschap van gegevens en toegang"),("ul",["Wie is eigenaar van de licenties en domeinnamen.","Wie beheert de beheerderswachtwoorden.","Hoe worden gegevens opgeleverd bij vertrek, en in welk formaat.","Welke documentatie blijft achter bij de organisatie."]),
   ("h2","Vertrekscenario vooraf"),("p","De vraag hoe een samenwerking eindigt, hoort bij de start te worden beantwoord. Een leverancier die daar geen duidelijkheid over geeft, creëert een afhankelijkheid die bij een conflict duur uitpakt."),
   ("h2","Onafhankelijkheid van advies"),("p","Een partij die zowel adviseert als levert, heeft een belang bij de uitkomst van het advies. Dat hoeft geen probleem te zijn, mits het expliciet is en er ruimte blijft voor een tweede mening bij grote beslissingen."),
   ("p",DISC)]},
]

ARTIKELEN=[
 {"slug":"waarom-back-ups-falen","titel":"Waarom back-ups vaker falen dan gedacht","cat":"Praktijk","datum":"2026-07-18","datum_nl":"18 juli 2026","lees":4,
  "resume":"Bijna elke organisatie heeft een back-up. Aanzienlijk minder organisaties hebben er ooit een teruggezet.",
  "body":[("p","Het vertrouwen in back-ups is groot en de controle erop klein. Dat verschil komt pas aan het licht op het moment dat herstel nodig is."),
   ("h2","Groen betekent niet bruikbaar"),("p","Back-upsoftware meldt of de taak is voltooid, niet of de inhoud consistent is. Databases die tijdens het kopiëren in gebruik waren, kunnen een kopie opleveren die technisch bestaat maar niet start."),
   ("h2","Wat er systematisch buiten valt"),("ul",["Gegevens in clouddiensten, in de veronderstelling dat de leverancier dat regelt.","Postbussen en gedeelde mappen van vertrokken medewerkers.","Configuraties van netwerkapparatuur en firewalls.","Bestanden op lokale schijven van laptops."]),
   ("h2","De kopie die niet mee mag"),("p","Gijzelsoftware zoekt actief naar aangesloten opslag en netwerkschijven. Een back-up die permanent bereikbaar is vanaf het netwerk, wordt in veel gevallen meeversleuteld. Een offline kopie of opslag die niet te overschrijven is, blijft dan als enige over."),
   ("p",DISC)]},
 {"slug":"schaduw-it","titel":"Schaduw-IT: hulpmiddelen die niemand heeft goedgekeurd","cat":"Achtergrond","datum":"2026-07-04","datum_nl":"4 juli 2026","lees":4,
  "resume":"Medewerkers kiezen zelf een oplossing wanneer de officiële weg te traag is. Dat is zelden onwil.",
  "body":[("p","Bestanden delen via een privéaccount, een gratis vertaaldienst voor een klantdocument, een eigen chatgroep voor overleg: schaduw-IT ontstaat waar de goedgekeurde route niet voldoet."),
   ("h2","Waarom het gebeurt"),("p","In vrijwel alle gevallen is de reden praktisch. Het officiële systeem is traag, het aanvragen van toegang duurt weken, of de goedgekeurde toepassing kan iets niet wat nodig is. Verbieden zonder alternatief verplaatst het probleem naar plekken die nog minder zichtbaar zijn."),
   ("h2","De risico's"),("ul",["Bedrijfsgegevens buiten het zicht van back-up en beveiliging.","Geen verwerkersovereenkomst met de gebruikte dienst.","Toegang die blijft bestaan nadat iemand uit dienst gaat.","Gegevens die bij een leverancier belanden zonder dat dit is beoordeeld."]),
   ("h2","Wat wel werkt"),("p","Inventariseren welke hulpmiddelen feitelijk worden gebruikt, en per stuk beoordelen of er een goedgekeurd alternatief is dat hetzelfde kan. Waar dat ontbreekt, is de vraag of de officiële route aanpassing behoeft eerlijker dan een verbod."),
   ("p",DISC)]},
]

def tile(s):
    return f"""<a class="tile" href="/onderwerpen/{s['slug']}/"><h3>{esc(s['naam'])}</h3><p>{esc(s['resume'][:96].rsplit(' ',1)[0])}...</p></a>"""
def newscard(a):
    return f"""<article class="news"><span class="cat">{esc(a['cat'])}</span>
  <h3><a href="/nieuws/{a['slug']}/" style="color:inherit;text-decoration:none">{esc(a['titel'])}</a></h3>
  <p>{esc(a['resume'])}</p><div class="meta">{esc(a['datum_nl'])} &middot; {a['lees']} min lezen</div></article>"""

def p_home():
    ld=[{"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#w","url":BASE+"/","name":SITE,"inLanguage":"nl-NL",
         "description":"Onafhankelijke kennisgids over ICT en digitale veiligheid voor kleine en middelgrote organisaties."},
        {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#o","name":SITE,"url":BASE+"/","email":EMAIL},crumb([("Home","/")])]
    gids="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p></div>' for g in GIDSEN)
    h=head("Wierenga ICT | kennisgids over ICT en digitale veiligheid",
      "Onafhankelijke kennisgids over ICT en digitale veiligheid voor het mkb. Back-up, phishing, wachtwoorden, updates, cloud en AVG in gewone taal.","/",ld)
    h+=f"""<section class="hero"><div class="wrap hero-inner">
  <div><span class="eyebrow">{IC['scale']}Kennisgids</span>
  <h1>ICT-veiligheid <em>zonder ruis</em></h1>
  <p class="lead">Back-up, phishing, wachtwoorden en updates: welke maatregelen werkelijk verschil maken voor een kleine organisatie, en welke vooral geld kosten. Onafhankelijk en zonder verkoopbelang.</p>
  <div class="hero-actions"><a class="btn btn-plum" href="/onderwerpen/">Bekijk de onderwerpen {IC['arrow']}</a><a class="btn btn-ghost" href="/gidsen/">Naar de gidsen</a></div>
  <div class="hero-meta"><span>{IC['check']}6 onderwerpen</span><span>{IC['check']}Gericht op het mkb</span><span>{IC['check']}Geen leverancier</span></div></div>
  <div class="hero-art"><img src="/assets/img/hero.svg" alt="Illustratie van een beveiligde werkplek" width="480" height="340"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['doc']}Onderwerpen</span><h2>De onderwerpen die het meeste opleveren</h2>
  <p class="lead">Per onderwerp de kern, de maatregelen die echt helpen en de punten waarop het in de praktijk misgaat.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in ONDERWERPEN)}</div></div></section>

<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h2>Twee praktische gidsen</h2></div>
  <div class="grid cols-2">{gids}</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['clock']}Nieuws</span><h2>Laatste artikelen</h2></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div>
  <p style="margin-top:22px"><a class="more" href="/nieuws/">Alle artikelen {IC['arrow']}</a></p></div></section>

<section class="section panel"><div class="wrap prose">
  <span class="eyebrow">{IC['doc']}Aanbevolen</span>
  <h2>Back-up en opslag buiten de deur</h2>
  <p class="lead">Van alle maatregelen op deze site levert een werkende back-up buiten het eigen netwerk het meeste op. Een van de partijen die dat voor het mkb verzorgt:</p>
  <div class="callout">
    <p><strong>Data Opslag Nederland</strong></p>
    <p>Data Opslag Nederland levert cloudopslag en automatische back-ups voor bedrijfsgegevens, met servers in Amsterdam en Delft en opslag die voldoet aan de AVG. Het aanbod omvat versleutelde uitwisseling met externe partijen, toegangsbeheer en synchronisatie tussen apparaten, met Nederlandstalige ondersteuning per telefoon. Geschikt voor organisaties van enkele gebruikers tot enkele duizenden medewerkers.</p>
    <p style="margin-top:12px"><a href="https://www.dataopslagnederland.nl/" target="_blank" rel="noopener">dataopslagnederland.nl {IC['arrow']}</a></p>
  </div>
</div></section>

<section class="section tight"><div class="wrap"><div class="cta">
  <h2>Een onderwerp gemist?</h2><p>Deze gids groeit op basis van vragen die binnenkomen. Suggesties en correcties zijn welkom bij de redactie.</p>
  <a class="btn btn-gold" href="/contact/">Mail de redactie {IC['arrow']}</a></div></div></section>"""
    write("/",h+footer())

def p_ond_index():
    path="/onderwerpen/"; c=[("Home","/"),("Onderwerpen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Onderwerpen","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":s["naam"],"url":BASE+f"/onderwerpen/{s['slug']}/"} for i,s in enumerate(ONDERWERPEN)]},crumb(c)]
    h=head("Onderwerpen ICT | "+SITE,"Overzicht van ICT-onderwerpen: back-up en herstel, phishing, wachtwoorden, patchbeheer, cloud en AVG.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['doc']}Overzicht</span>
  <h1>Onderwerpen</h1><p class="lead">Zes onderwerpen die samen de basis vormen van digitale weerbaarheid in een kleine organisatie.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in ONDERWERPEN)}</div></div></section>"""
    write(path,h+footer())

def p_ond(s):
    path=f"/onderwerpen/{s['slug']}/"; c=[("Home","/"),("Onderwerpen","/onderwerpen/"),(s["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":s["naam"],"description":s["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    sp="".join(f"<div><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>" for l,v in s["specs"])
    sec="".join(f"<h2>{esc(t)}</h2><p>{esc(p)}</p>" for t,p in s["secties"])
    pt="".join(f'<li>{IC["check"]}<span>{esc(x)}</span></li>' for x in s["punten"])
    anders=[x for x in ONDERWERPEN if x["slug"]!=s["slug"]][:3]
    h=head(f"{s['naam']} | uitgelegd | {SITE}", s["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section tight"><div class="wrap prose"><span class="eyebrow">{IC['scale']}Onderwerp</span>
  <h1>{esc(s['naam'])}</h1><p class="lead">{esc(s['resume'])}</p></div>
  <div class="wrap"><dl class="specs">{sp}</dl></div>
  <div class="wrap prose">{sec}<h2>Kort samengevat</h2><ul class="ticks" style="margin-bottom:16px">{pt}</ul>
  <p class="disc">{esc(DISC)}</p>{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Andere onderwerpen</h2></div>
  <div class="grid cols-3">{"".join(tile(x) for x in anders)}</div></div></section>"""
    write(path,h+footer())

def p_gidsen():
    path="/gidsen/"; c=[("Home","/"),("Gidsen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Gidsen","inLanguage":"nl-NL"},crumb(c)]
    cards="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p><p style="margin-top:10px"><a class="more" href="/gidsen/{g["slug"]}/">Lees de gids {IC["arrow"]}</a></p></div>' for g in GIDSEN)
    h=head("Gidsen | incident en leverancierskeuze | "+SITE,"Praktische gidsen over de eerste stappen bij een digitaal incident en over het kiezen van een ICT-leverancier.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span>
  <h1>Gidsen</h1><p class="lead">Twee situaties waarin de eerste beslissingen bepalend zijn voor wat er daarna mogelijk is.</p></div>
  <div class="grid cols-2">{cards}</div></div></section>"""
    write(path,h+footer())

def p_gids(g):
    path=f"/gidsen/{g['slug']}/"; c=[("Home","/"),("Gidsen","/gidsen/"),(g["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":g["titel"],"description":g["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{g['titel']} | {SITE}", g["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC[g['ic']]}Gids</span>
  <h1>{esc(g['titel'])}</h1><p class="lead">{esc(g['resume'])}</p>{blocks(g['body'])}{byline()}</div></section>"""
    write(path,h+footer())

def p_nieuws():
    path="/nieuws/"; c=[("Home","/"),("Nieuws",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"},crumb(c)]
    h=head("Nieuws | artikelen over ICT in de praktijk | "+SITE,"Achtergrondartikelen over ICT in de praktijk, van falende back-ups tot hulpmiddelen die buiten het zicht worden gebruikt.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['clock']}Nieuws</span>
  <h1>Artikelen</h1><p class="lead">Achtergrond bij wat er in de praktijk misgaat, en waarom.</p></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div></div></section>"""
    write(path,h+footer())

def p_art(a):
    path=f"/nieuws/{a['slug']}/"; c=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":a["titel"],"description":a["resume"],
         "datePublished":a["datum"],"inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{a['titel']} | {SITE}", a["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['clock']}{esc(a['cat'])}</span>
  <h1>{esc(a['titel'])}</h1><p class="meta" style="margin-bottom:22px">Door {esc(AUTEUR)} &middot; {esc(a['datum_nl'])} &middot; {a['lees']} min lezen</p>
  {blocks(a['body'])}{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Meer lezen</h2></div>
  <div class="grid cols-2">{"".join(newscard(x) for x in ARTIKELEN if x['slug']!=a['slug'])}</div></div></section>"""
    write(path,h+footer())

def p_over():
    path="/over/"; c=[("Home","/"),("Over",path)]
    ld=[{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over","inLanguage":"nl-NL"},crumb(c)]
    h=head("Over Wierenga ICT | wat dit platform is | "+SITE,
      "Wierenga ICT is een onafhankelijke kennisgids over ICT en digitale veiligheid. Geen leverancier, geen dienstverlening en geen productvoorkeuren.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['book']}Over het platform</span>
  <h1>Een kennisgids, geen leverancier</h1>
  <p class="lead">Wierenga ICT legt uit welke ICT-maatregelen voor een kleine organisatie werkelijk verschil maken, en welke vooral budget kosten zonder het risico noemenswaardig te verlagen.</p>
  <h2>Waarom deze gids bestaat</h2>
  <p>Kleine organisaties krijgen advies van partijen die tegelijk leveren. Dat hoeft niet verkeerd te zijn, maar het maakt lastig te beoordelen of een voorstel het risico verlaagt of vooral de omzet verhoogt. Deze gids beschrijft de maatregelen los van welk product dan ook.</p>
  <div class="callout"><p><strong>Geen leverancier.</strong> Dit platform levert geen diensten, verkoopt geen software en heeft geen afspraken met leveranciers. Overeenkomsten met namen van bestaande ICT-bedrijven berusten niet op enige samenwerking of betrokkenheid.</p></div>
  <h2>Wat hier wel staat</h2>
  <p>Per onderwerp wat de maatregel doet, wat die in de praktijk oplevert en waar het misgaat. Productnamen blijven achterwege, omdat het aanbod sneller verandert dan het principe erachter.</p>
  <h2>Verschillen per omgeving</h2>
  <p>Wat verstandig is, hangt af van de omvang, de sector en de bestaande inrichting. Een maatregel die in de ene omgeving vanzelfsprekend is, kan elders onwerkbaar zijn. Bij ingrijpende wijzigingen blijft toetsing door een beheerder verstandig.</p>
  <p style="margin-top:16px"><a class="btn btn-plum" href="/redactie/">Over de redactie {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Naar de onderwerpen</a></p></div></section>"""
    write(path,h+footer())

def p_redactie():
    path="/redactie/"; c=[("Home","/"),("Over de redactie",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#joost","name":AUTEUR,"jobTitle":AUTEUR_ROL,"worksFor":{"@type":"Organization","name":SITE}},
        {"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":"Over de redactie","inLanguage":"nl-NL"},crumb(c)]
    h=head(f"Over de redactie: {AUTEUR} | {SITE}", f"{AUTEUR} schrijft de onderwerpen en gidsen van Wierenga ICT.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="persona">
  <div class="persona-photo"><img src="/assets/img/auteur.svg" alt="Illustratie van {esc(AUTEUR)}"></div>
  <div><span class="eyebrow">{IC['scale']}De redactie</span><h1>{esc(AUTEUR)}</h1>
  <p class="lead">{esc(AUTEUR_ROL)}. Joost schrijft de onderwerpen, de gidsen en de artikelen op deze site.</p></div></div></div></section>
<section class="section panel"><div class="wrap prose">
  <h2>Van de servicedesk naar de redactie</h2>
  <p>Joost werkte jaren als systeembeheerder bij een middelgroot bedrijf, waar dezelfde patronen terugkwamen: een back-up die niemand had getest, een leverancierscontract zonder vertrekscenario, en beveiligingsmaatregelen die vooral op papier bestonden.</p>
  <h2>Principes boven producten</h2>
  <p>Op deze site staan geen productnamen en geen aanbevelingen voor specifieke leveranciers. Wat er wel staat is welk probleem een maatregel oplost, zodat een aanbieding daaraan getoetst kan worden in plaats van andersom.</p>
  <h2>Een getekend portret</h2>
  <p>De illustratie op deze pagina is een tekening, geen foto.</p>
  <h2>Contact</h2>
  <p>Correcties en suggesties komen binnen via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>"""
    write(path,h+footer())


def p_partners():
    path="/partners/"; c=[("Home","/"),("Partners",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Partners","inLanguage":"nl-NL"}]
    h=head("Partners | "+SITE,"Partners en bronnen waar Wierenga ICT naar verwijst.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
  <span class="eyebrow">Partners</span><h1>Partners en bronnen</h1>
  <p class="lead">Wierenga ICT verwijst hier naar externe partners en bronnen.</p>
  <div class="grid" style="grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px">
  <div class="card"><h3>Van der Zwaard</h3><p>Van der Zwaard is een accountants- en belastingadvieskantoor in Den Haag, met dienstverlening voor ondernemers op het gebied van boekhouding, administratie en belastingadvies.</p><p style="margin-top:10px"><a href="https://www.vanderzwaard.nl/diensten/administratie-den-haag/" target="_blank" rel="noopener">administratie den haag</a></p></div>
<div class="card"><h3>DLSA Letselschade Advocaten</h3><p>DLSA is gespecialiseerd in letselschade, onder meer voor (oud-)militairen met gezondheidsklachten door chroom-6 of PTSS, en begeleidt schadeclaims tegen Defensie.</p><p style="margin-top:10px"><a href="https://dlsa.nl/letselschade/ambtenaar/schadeclaim-defensie/" target="_blank" rel="noopener">defensie advocaat</a></p></div>
</div>
</div></section>"""
    write(path,h+footer())

def p_contact():
    path="/contact/"; c=[("Home","/"),("Contact",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, correctie of suggestie voor Wierenga ICT? Een e-mail komt rechtstreeks bij de redactie binnen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['mail']}Contact</span>
  <h1>Contact met de redactie</h1>
  <p class="lead">Deze site heeft geen contactformulier. Een e-mail komt rechtstreeks bij de redactie binnen.</p>
  <div class="callout"><p><strong>E-mailadres</strong></p><p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:600">{EMAIL}</a></p></div>
  <h2>Waar de redactie iets mee kan</h2>
  <ul><li>Een correctie op een beschrijving, met onderbouwing.</li><li>Een onderwerp dat nog ontbreekt in de gids.</li><li>Praktijkervaring die iets aanvult of tegenspreekt.</li></ul>
  <h2>Waar niet</h2>
  <p>Dit platform levert geen diensten en beoordeelt geen individuele omgevingen. Bij een lopend incident zijn de eigen ICT-partij, de verzekeraar en zo nodig de politie de aangewezen partijen.</p></div></section>"""
    write(path,h+footer())

def legal(path,titel,bs):
    c=[("Home","/"),(titel,path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":titel,"inLanguage":"nl-NL"}]
    h=head(f"{titel} | {SITE}", f"{titel} van {SITE}.",path,ld)+crumbs_html(c)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(titel)}</h1>{"".join(bs)}</div></section>'
    write(path,h+footer())

def p_legal():
    legal("/privacybeleid/","Privacybeleid",[
      "<p>Wierenga ICT is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>De site bevat geen contactformulier. Wie per e-mail contact opneemt, deelt uitsluitend wat in dat bericht staat, en dat wordt alleen gebruikt om te antwoorden.</p>",
      "<h2>Statistieken</h2><p>Als bezoekcijfers worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder verkoop aan derden.</p>",
      "<h2>Bewaartermijn</h2><p>E-mails worden niet langer bewaard dan nodig is voor de afhandeling.</p>",
      f"<h2>Vragen</h2><p>Vragen over privacy kunnen naar {EMAIL}.</p>"])
    legal("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Alleen cookies die nodig zijn voor het functioneren van de pagina's kunnen worden geplaatst.</p>",
      "<h2>Lettertypen</h2><p>De lettertypen worden geladen via een externe dienst, wat bij het tonen van een pagina een verzoek naar die dienst met zich meebrengt.</p>",
      f"<h2>Vragen</h2><p>Vragen over cookies kunnen naar {EMAIL}.</p>"])

def p_404():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
  <span class="eyebrow" style="justify-content:center">404</span><h1>Deze pagina bestaat niet</h1>
  <p class="lead">De link is mogelijk verouderd. Het overzicht van onderwerpen is een goed vertrekpunt.</p>
  <p><a class="btn btn-plum" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Alle onderwerpen</a></p></div></section>"""
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h+footer())

def extras():
    u=["/","/over/","/redactie/","/onderwerpen/","/gidsen/","/nieuws/","/partners/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+=[f"/onderwerpen/{s['slug']}/" for s in ONDERWERPEN]+[f"/gidsen/{g['slug']}/" for g in GIDSEN]+[f"/nieuws/{a['slug']}/" for a in ARTIKELEN]
    open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write(f"https://www.wierenga-ict.nl/* {BASE}/:splat 301!\n")

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    p_home(); p_over(); p_redactie(); p_ond_index()
    for s in ONDERWERPEN: p_ond(s)
    p_gidsen()
    for g in GIDSEN: p_gids(g)
    p_nieuws()
    for a in ARTIKELEN: p_art(a)
    p_contact(); p_partners(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()
