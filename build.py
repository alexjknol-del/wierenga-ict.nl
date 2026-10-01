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
        elif b[0]=="plink": o.append(f"<p>{b[1]}</p>")
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
 {"slug": "ict-beheer-uitbesteden-mkb", "titel": "ICT-beheer uitbesteden in het mkb: wat een vaste partner overneemt en wat niet", "cat": "Praktijk", "datum": "2026-09-25", "datum_nl": "25 september 2026", "lees": 5, "resume": "Een vaste ICT-partner neemt storingen, updates en vragen over Microsoft 365 over. Welke afspraken vooraf duidelijk moeten zijn en welke verantwoordelijkheid bij de organisatie zelf blijft.", "body": [
  ("p", "In veel kleine organisaties wordt de ICT erbij gedaan. Een medewerker die handig is met computers zet nieuwe laptops klaar, verlengt licenties en belt de provider als het internet wegvalt. Dat gaat goed tot die persoon op vakantie is, het bedrijf groeit of een storing groter blijkt dan gedacht. Op dat moment komt de vraag op of het beheer beter bij een externe partij kan liggen."),
  ("h2", "Waar losse hulp vastloopt"),
  ("p", "Bij een grotere storing blijkt vaak dat niemand precies weet hoe het netwerk is ingericht, welke beheeraccounts er zijn en waar de back-ups staan. Die kennis zit bij één persoon of bij een externe hulp die af en toe langskomt. Het zoeken naar wachtwoorden en instellingen kost dan meer tijd dan de oplossing zelf."),
  ("p", "Een vaste partner bouwt die kennis op en legt haar vast. Apparaten, accounts, licenties en afspraken staan op één plek, zodat ook een collega van de vaste contactpersoon een melding kan oppakken."),
  ("h2", "Wat onder ondersteuning valt"),
  ("p", "ICT-ondersteuning gaat verder dan een computer die niet opstart. Meldingen gaan over werkplekken, inlogproblemen in Microsoft 365, een printer die niet meer wordt gevonden, het netwerk of de beveiliging. Het grootste deel daarvan is op afstand op te lossen: de beheerder kijkt met toestemming mee op het scherm en past de instelling aan. Bij een defect apparaat of een probleem in de netwerkkast is een bezoek op locatie nodig."),
  ("plink", "Snelheid hangt vooral af van de manier waarop meldingen binnenkomen en worden verdeeld. Bij de ICT-ondersteuning van <a href=\"https://www.pixelbyte.nl/diensten/ict-ondersteuning/\" target=\"_blank\" rel=\"noopener\">pixelbyte.nl</a> komen vragen per telefoon of e-mail direct bij een deskundige medewerker terecht, krijgen ongeveer negen op de tien meldingen binnen een uur een reactie en wordt veel meteen op afstand opgelost. Lukt dat niet, dan komt er iemand langs."),
  ("h2", "Afspraken die vooraf duidelijk moeten zijn"),
  ("ul", ["Bereikbaarheid: via welke kanalen een melding binnenkomt en binnen welke tijd een reactie volgt.", "Afhandeling: wat op afstand gebeurt en wanneer iemand op locatie komt.", "Toegang: wie de beheeraccounts heeft en waar de herstelcodes liggen.", "Vertrek: hoe documentatie en toegang worden overgedragen als de samenwerking stopt."]),
  ("p", "Dat laatste punt wordt vaak vergeten. Een organisatie hoort zelf eigenaar te blijven van haar domeinnaam, haar Microsoft 365-omgeving en de hoofdbeheeraccounts, ook als een partner het dagelijkse werk doet."),
  ("h2", "Met of zonder contract"),
  ("plink", "Niet elke organisatie heeft een vast beheercontract nodig. Een kantoor met drie werkplekken vraagt iets anders dan een bedrijf met zestig medewerkers op twee locaties. Sommige ICT-bedrijven bieden daarom ondersteuning met en zonder servicecontract. <a href=\"https://www.pixelbyte.nl/\" target=\"_blank\" rel=\"noopener\">Pixelbyte</a> uit Alkmaar werkt op die manier voor organisaties met 1 tot 100 medewerkers, zonder langlopende contracten en met een voorkeur voor Europese oplossingen waar privacy meespeelt. Zo is het mogelijk om klein te beginnen en het beheer uit te breiden als de organisatie groeit."),
  ("h2", "Beheer voorkomt een deel van de meldingen"),
  ("p", "Goede ondersteuning begint voordat er iets misgaat. Updates die op vaste momenten worden uitgerold, een back-up die wordt gecontroleerd en accounts van oud-medewerkers die direct worden uitgeschakeld, voorkomen een groot deel van de storingen en incidenten. Een partner die alleen op meldingen reageert, ziet die kant niet. Bij de keuze helpt het om te vragen welke controles standaard worden uitgevoerd en hoe daarover wordt gerapporteerd."),
  ("h2", "Wat binnen de organisatie blijft"),
  ("p", "Uitbesteden betekent niet dat de organisatie niets meer met ICT te maken heeft. Er blijft een interne contactpersoon nodig die meldingen bundelt, nieuwe medewerkers op tijd doorgeeft en keuzes maakt over prioriteiten. Met die rolverdeling helder blijft de techniek op de achtergrond werken en houden medewerkers meer tijd over voor hun eigen vak."),
 ]},
 {"slug": "barcode-etiketten-scanner-en-voorraadsysteem", "titel": "Barcode etiketten in het magazijn: scanner, software en etiket op elkaar afstemmen", "cat": "Praktijk", "datum": "2026-09-07", "datum_nl": "7 september 2026", "lees": 4, "resume": "Een barcode werkt pas als scanner, software en etiket bij elkaar passen. Waar het bij de koppeling met een voorraadsysteem misgaat en hoe dat te voorkomen is.", "body": [
  ("p", "Barcodes in een magazijn lijken een kwestie van etiketten printen en scanners aansluiten. In de praktijk loopt een invoering vaker vast op de koppeling tussen de onderdelen: een code die de scanner wel leest maar de software niet herkent, een etiket dat na een paar weken onleesbaar is, of een scanner die een extra teken meestuurt. Wie de onderdelen vooraf op elkaar afstemt, voorkomt het meeste gedoe."),
  ("h2", "Begin bij de gegevens"),
  ("p", "Een barcode is een andere schrijfwijze van een code die al in een systeem staat. Voor locaties is dat een vaste opbouw van gang, stelling, plank en vak. Voor artikelen is dat het artikelnummer uit het voorraad- of ERP-systeem. Die nummering hoort eerst in het systeem vast te liggen, pas daarna worden etiketten gemaakt. Een wijziging achteraf betekent alle etiketten opnieuw."),
  ("h2", "Het barcodetype kiezen"),
  ("p", "Code 128 is voor interne codes de meest gebruikte keuze: compact, geschikt voor letters en cijfers en door vrijwel elke scanner te lezen. Code 39 is ouder en neemt bij dezelfde lengte meer ruimte in. EAN-13 hoort bij producten in de handel en werkt met nummers die centraal worden uitgegeven, en is dus niet bedoeld voor eigen locatiecodes. Een QR-code bevat meer gegevens en is met een telefooncamera te lezen, maar vraagt om een scanner die tweedimensionale codes ondersteunt."),
  ("h2", "Scanner en software laten samenwerken"),
  ("p", "De meeste handscanners gedragen zich tegenover de computer als een toetsenbord. Ze typen de code in het veld waar de cursor staat en sluiten af met een Enter. Dat is eenvoudig, maar er gaat geregeld iets mis. Een scanner die een voorvoegsel of een Tab meestuurt, of een toetsenbordindeling die afwijkt van die van de computer, levert codes op met verkeerde tekens. De instellingen zijn bij de meeste scanners aan te passen door een configuratiebarcode uit de handleiding te scannen."),
  ("p", "Bij draadloze scanners en mobiele terminals speelt ook het netwerk mee. Een magazijn met een zwak wifisignaal tussen de stellingen levert scans op die niet aankomen of dubbel worden verwerkt. Een meting van de dekking voordat de scanners in gebruik gaan, bespaart later zoekwerk naar voorraadverschillen."),
  ("h2", "Een etiket dat leesbaar blijft"),
  ("plink", "Een scanfout ligt niet altijd aan de techniek. Een gekreukeld, vuil of half losgelaten etiket leest slecht, en een glanzende toplaag kan licht terugkaatsen. Op stalen stellingen worden vaak magnetische etiketten gebruikt, omdat die mee kunnen verhuizen als de indeling verandert. Bij <a href=\"https://www.mms-magneet.nl/barcode-etiketten/\" target=\"_blank\" rel=\"noopener\">MMS Magneetservice</a> zijn magazijnetiketten zowel magnetisch als zelfklevend verkrijgbaar, kant-en-klaar gedrukt op basis van aangeleverde gegevens of als materiaal om zelf te printen."),
  ("p", "Bij zelf printen moet het etiketmateriaal passen bij de printer. Een thermotransferprinter vraagt om ander materiaal dan een inkjet- of laserprinter, en niet elk etiket verdraagt de warmte van elke printer."),
  ("h2", "Testen voor de uitrol"),
  ("p", "Een proef met een paar stellingen levert meer op dan een volledige uitrol in één weekend. Het etiket hoort getest te worden op de werkelijke plek en afstand, met de scanner die er straks gebruikt wordt. Daarna volgt een controle in het systeem: komt de gescande code op de juiste regel terecht, en klopt de voorraadmutatie? Pas dan volgt de rest van het magazijn."),
  ("h2", "Beheer na de invoering"),
  ("plink", "Een barcodesysteem vraagt om onderhoud. Nieuwe artikelen en locaties krijgen direct een etiket, beschadigde etiketten worden vervangen en de scannerinstellingen horen in de documentatie van de ICT-omgeving, zodat een vervangend apparaat op dezelfde manier wordt ingesteld. Over etiketmateriaal en houders is telefonisch advies te krijgen via <a href=\"https://www.mms-magneet.nl/\" target=\"_blank\" rel=\"noopener\">mms-magneet.nl</a>."),
  ("p", "Met goed afgestemde onderdelen blijft de voorraad in het systeem gelijk aan wat er werkelijk op de plank ligt."),
 ]},
 {"slug":"ict-veiligheid-zonder-dure-omwegen","titel":"ICT-veiligheid zonder dure omwegen","cat":"Praktijk","datum":"2026-09-05","datum_nl":"5 september 2026","lees":8,
  "resume":"Back-ups testen, phishing beperken, wachtwoorden regelen en updates beheren: de basis die een mkb-organisatie echt kan uitvoeren.",
  "body":[
  ("p", "ICT-veiligheid klinkt vaak groter dan het is. Bij een mkb-bedrijf gaat het meestal om gewone keuzes: wie mag erbij, waar staat data, en hoe snel herstel je na gedoe. Daar zit de winst. Niet in een map vol beleid die niemand opent."),
  ("p", "Een organisatie met twaalf werkplekken heeft geen bankniveau nodig. Wel afspraken die iemand kan uitvoeren op een drukke dinsdag. Denk aan hersteltests, tweefactor, automatische updates en een simpele lijst met kritieke diensten. Wie die basis strak regelt, haalt veel risico uit het dagelijkse werk."),
  ("h2", "ICT-veiligheid begint bij keuzes die je test"),
  ("p", "Beleid klinkt netjes, maar gedrag telt. Een back-upplan zonder hersteltest geeft vooral een prettig gevoel. Pas bij terugzetten merk je of de boekhoudmap compleet is, of de rechten kloppen en hoe lang het bedrijf stilvalt."),
  ("p", "Een goede test hoeft geen project van drie weken te zijn. Kies \u00e9\u00e9n map, \u00e9\u00e9n mailbox en \u00e9\u00e9n applicatie. Zet die terug op een aparte plek en noteer de tijd. Na een uur weet je vaak meer dan na tien vergaderingen."),
  ("p", "Werk met een kleine lijst van vragen. Die lijst voorkomt dat beveiliging vaag blijft. Gebruik hem elk kwartaal, niet alleen na een incident."),
  ("ul", ["<strong>Welke data mag maximaal \u00e9\u00e9n werkdag kwijt zijn?</strong>", "<strong>Welke systemen moeten binnen vier uur terug zijn?</strong>", "<strong>Wie kan herstel starten als de beheerder ziek is?</strong>", "<strong>Waar liggen wachtwoorden en herstelcodes veilig opgeslagen?</strong>"]),
  ("plink", "Ook hardware hoort in dit verhaal. Een traag of oud apparaat krijgt minder aandacht van gebruikers en blijft vaker achter met updates. Bij nieuwe of tweedehands werkplekken helpt een nuchtere <a href=\"https://www.computerzaak.nl/laptop-keuzehulp/\" target=\"_blank\" rel=\"noopener\">laptop kiezen voor werk</a> om beheer simpel te houden."),
  ("h2", "Back-ups: niet bewaren, maar terugzetten"),
  ("p", "Veel bedrijven hebben ergens een back-up. Dat zegt weinig. De echte vraag is of je data terugkrijgt zonder paniek, zonder giswerk en zonder drie dagen zoeken naar een wachtwoord."),
  ("p", "Hanteer liever drie vaste kopie\u00ebn dan vijf onduidelijke. E\u00e9n kopie staat op het systeem zelf, \u00e9\u00e9n op een andere locatie en \u00e9\u00e9n is afgeschermd tegen wijzigen. Dat laatste helpt bij ransomware, omdat versleutelde bestanden anders keurig worden meegekopieerd."),
  ("p", "De bekende 3-2-1-regel blijft nuttig. Drie kopie\u00ebn, twee soorten opslag en \u00e9\u00e9n kopie buiten de deur. Maak het niet mooier dan nodig. Een kleine praktijk met pati\u00ebntgegevens heeft vooral zekerheid nodig over herstel en bewaartermijnen."),
  ("p", "Let scherp op cloudsync. OneDrive, Google Drive of Dropbox is handig, maar sync is geen volledige back-up. Verwijdert iemand een map of versleutelt malware bestanden, dan verspreidt die fout zich snel. Versiebeheer helpt, maar alleen als je weet hoe ver het teruggaat."),
  ("h2", "Herstel oefenen zonder verstoring"),
  ("p", "Plan hersteltests op een rustig moment. Vrijdagmiddag lijkt aantrekkelijk, maar dan wil niemand uitzoeken waarom rechten ontbreken. Een maandagochtend met \u00e9\u00e9n testmap werkt vaak beter. Iedereen is fris en fouten krijgen direct opvolging."),
  ("p", "Schrijf de stappen kort op. Niet als handleiding van twintig pagina\u2019s, maar als werkinstructie voor iemand die stress heeft. Welke knop open je eerst? Welk account gebruik je? Wie controleert of de teruggezette data bruikbaar is?"),
  ("h2", "Phishing blijft vooral mensenwerk"),
  ("p", "De meeste aanvallen beginnen nog steeds in de inbox. Filters houden veel tegen, maar geen enkel filter kent de toon van je leverancier perfect. Een mail over een openstaande factuur voelt snel geloofwaardig als de naam klopt."),
  ("p", "Maak melden makkelijker dan negeren. Een medewerker die twijfelt, moet niet bang zijn voor gezucht van de beheerder. E\u00e9n doorgestuurde mail kan voorkomen dat vijf collega\u2019s op dezelfde link klikken. Kleine cultuur, groot effect."),
  ("plink", "Training werkt alleen als die aansluit op echte situaties. Gebruik voorbeelden van pakketdiensten, salarisstroken, Microsoft 365-meldingen en facturen. De uitleg van <a href=\"https://www.ncsc.nl/phishing/hoe-herken-ik-een-phishing-e-mail\" target=\"_blank\" rel=\"noopener\">phishing e-mails herkennen volgens het NCSC</a> is een bruikbare basis voor herkenning zonder bangmakerij."),
  ("p", "Leg ook vast wat iemand doet na een klik. Schaamte kost tijd. Laat medewerkers direct melden, ook als ze al een wachtwoord hebben ingevuld. Daarna kun je sessies intrekken, het wachtwoord wijzigen en controleren of er regels in de mailbox zijn aangemaakt."),
  ("p", "Techniek ondersteunt dit werk. Zet SPF, DKIM en DMARC goed neer voor je domein. Daarmee voorkom je niet alle misbruik, maar je maakt vervalsing lastiger. Controleer ook of oude mailboxen en gedeelde accounts nog bestaan."),
  ("h2", "Wachtwoorden en tweefactor zonder gedoe"),
  ("p", "Wachtwoordbeleid mislukt vaak door te veel regels. Elke maand verplicht wijzigen leidt tot plakbriefjes en kleine variaties. Een lang uniek wachtwoord per dienst werkt beter. Een wachtwoordmanager maakt dat haalbaar voor mensen die al genoeg moeten onthouden."),
  ("p", "Tweefactor is geen luxe laagje. Het vangt veel schade op wanneer een wachtwoord uitlekt. Kies bij voorkeur een authenticator-app of fysieke sleutel. Sms is beter dan niets, maar gevoeliger voor misbruik en nummerovername."),
  ("p", "Begin met de accounts die veel macht hebben. Denk aan Microsoft 365-beheer, boekhouding, domeinregistratie, hosting en remote toegang. Wie daar binnenkomt, kan vaak mailboxen lezen, facturen aanpassen of back-ups saboteren."),
  ("p", "Gebruik geen gedeelde beheeraccounts voor dagelijks werk. Maak persoonlijke accounts met aparte rechten. Dan zie je achteraf wie wat deed. Bij een incident scheelt dat uren zoeken in logboeken."),
  ("p", "Toegang moet ook eindigen. Een medewerker die vertrekt, mag niet maanden later nog in bestanden kunnen. Zet uitdiensttreding in een checklist met accounts, apparaten, sleutels en doorstuurregels. Die lijst hoeft niet lang te zijn, zolang iemand hem gebruikt."),
  ("h2", "Updates, cloud en afspraken met leveranciers"),
  ("p", "Kwetsbaarheden klinken technisch, maar de praktijk is simpel. Een lek dat al maanden bekend is, vormt vaak meer risico dan een geheim lek. Aanvallers scannen breed en kiezen systemen die achterlopen."),
  ("p", "Automatische updates lossen veel op, maar niet alles. Sommige applicaties vragen handwerk of een herstart. Spreek daarom een vast onderhoudsvenster af. Een kwartier verstoring voelt vervelend, maar een dag stilstand is erger."),
  ("plink", "Ransomware verdient aparte aandacht. Criminelen kijken naar back-ups, verzekeringen en onderhandelingsruimte. De waarschuwing over <a href=\"https://www.ncsc.nl/nieuws/ransomware-in-het-mkb-cybercriminelen-verhogen-losgeld-bij-cyberverzekering\" target=\"_blank\" rel=\"noopener\">ransomware risico\u2019s voor het mkb</a> laat zien dat kleine bedrijven niet buiten beeld blijven."),
  ("p", "Cloud verlaagt beheerlast, maar verplaatst verantwoordelijkheid. De leverancier regelt het platform, jij regelt vaak gebruikers, rechten en bewaartermijnen. Lees daarom niet alleen de prijs per gebruiker. Kijk naar exportmogelijkheden, logbestanden en ondersteuning bij vertrek."),
  ("p", "Maak afspraken concreet. Wat is de hersteltijd bij storing? Hoe snel reageert support bij een beveiligingsmelding? Wie bewaart bewijs als een mailbox is misbruikt? Zulke vragen klinken saai tot ze nodig zijn."),
  ("p", "AVG past ook in deze aanpak. De wet vraagt passende maatregelen, geen theater. Voor een mkb-bedrijf betekent dat meestal: minimale rechten, goede back-ups, versleutelde apparaten en duidelijke afspraken met verwerkers."),
  ("p", "Bewaar niet alles omdat het kan. Oude klantbestanden, exportlijsten en mailboxarchieven vergroten de schade bij een lek. Spreek bewaartermijnen af en ruim periodiek op. Minder data betekent minder risico en minder zoekwerk."),
  ("p", "De beste beveiliging voelt niet als een extra baan. Ze zit in vaste gewoonten: maandelijks updates controleren, elk kwartaal herstel testen en direct melden bij twijfel. Dat is nuchter, uitvoerbaar en precies waar veel organisaties al genoeg aan hebben."),
 ]},

 {"slug":"security-awareness-meertalig-team","titel":"Security awareness in een meertalig team: waarom de standaardtraining niet aankomt","cat":"Praktijk","datum":"2026-08-22","datum_nl":"22 augustus 2026","lees":6,
  "resume":"Phishingtraining in het Nederlands mist precies de collega die het meeste risico loopt. Wat er wel werkt in een ploeg met vijf moedertalen.",
  "body":[
  ("p", "In veel mkb-bedrijven bestaat het personeelsbestand allang niet meer uit alleen Nederlandstalige medewerkers. In de techniek, de logistiek en de productie is een ploeg met vier of vijf moedertalen normaal. De securitytraining is dat meestal niet: die is in het Nederlands, bestaat uit tekst en wordt een keer per jaar afgevinkt."),
  ("p", "Het gevolg is voorspelbaar. De medewerker die de taal het minst goed beheerst, haalt het minste uit de training en is tegelijk het meest kwetsbaar voor een bericht dat op het eerste gezicht klopt."),
  ("h2", "Waarom taal hier zwaarder weegt dan elders"),
  ("p", "Phishing werkt op nuance. Een net iets te formele aanhef, een woord dat een Nederlander nooit zou gebruiken, een zin die grammaticaal klopt maar vreemd voelt. Precies die signalen zijn onzichtbaar voor iemand die de taal functioneel maar niet gevoelsmatig beheerst."),
  ("p", "Daar komt bij dat aanvallers hun berichten inmiddels foutloos laten vertalen. Het klassieke advies om op spelfouten te letten werkt niet meer, en voor anderstalige collegas werkte het sowieso al niet."),
  ("h2", "Wat er in de praktijk misgaat"),
  ("ul", ["De training staat alleen in het Nederlands en wordt niet aangeboden in de talen die op de vloer worden gesproken.",
     "Er wordt getoetst op afvinken en niet op begrip, waardoor niemand merkt dat de boodschap niet is overgekomen.",
     "Meldingen doen gaat via een formulier in het Nederlands, dus wordt er niet gemeld.",
     "De voorbeelden komen uit een kantooromgeving terwijl de doelgroep in een loods of een werkplaats staat."]),
  ("h2", "Wat wel werkt"),
  ("p", "Begin bij het meldingsproces en niet bij de training. Een medewerker die twijfelt, moet in dertig seconden kunnen melden zonder een formulier in te vullen dat hij half begrijpt. Een appgroep met een vaste contactpersoon doet meer voor de veiligheid dan een uitgebreide e-learning."),
  ("p", "Daarnaast helpt het om de training visueel te maken. Schermafbeeldingen van echte berichten met pijlen erbij komen aan zonder dat er veel tekst aan te pas komt. Simulaties werken om dezelfde reden goed: je oefent het gedrag in plaats van de theorie."),
  ("h2", "Taalvaardigheid is een securitymaatregel"),
  ("p", "Op langere termijn is investeren in de taalvaardigheid van het team ook een investering in weerbaarheid. Wie de werktaal beter beheerst, leest instructies nauwkeuriger, meldt eerder en begrijpt waarom een procedure bestaat."),
  ("plink", "Aanbieders van zakelijke taaltraining werken daarom vaak incompany met materiaal uit de organisatie zelf. Bij <a href=\"https://speakandspoke.nl/\" rel=\"nofollow\">Speak And Spoke</a> is dat het uitgangspunt: de woorden die geoefend worden zijn de woorden die op die specifieke werkvloer rondgaan, inclusief de begrippen uit procedures en veiligheidsinstructies."),
  ("plink", "Voor organisaties die dat gefaseerd willen aanpakken, is een online leeromgeving een praktische tussenstap. Op <a href=\"https://speakandspoke.nl/online-leren/\" rel=\"nofollow\">speakandspoke.nl</a> staat beschreven hoe zon omgeving naast klassikale sessies functioneert."),
  ("h2", "Praktisch beginnen"),
  ("p", "Voor een mkb-bedrijf met een gemengd team zijn drie stappen genoeg om het niveau merkbaar op te tillen. Vertaal de meldprocedure naar de talen die daadwerkelijk worden gesproken. Vervang de jaarlijkse tekstuele training door vier korte sessies met echte voorbeelden. En laat na elke sessie iemand in eigen woorden herhalen wat hij moet doen bij twijfel."),
  ("p", "Dat kost samen minder dan een dag per jaar en pakt de zwakste schakel aan in plaats van de gemiddelde.")]},

 {"slug":'patronen-herkennen-ict-knelpunten','titel':'Zo leer je patronen herkennen achter steeds terugkerende ICT knelpunten',"cat":'Praktijk',"datum":'2026-08-20',"datum_nl":'20 augustus 2026','lees':5,
  'resume':'Hetzelfde probleem duikt steeds weer op, maar ziet er elke keer net iets anders uit. Met een paar bewuste stappen maak je het patroon zichtbaar.',
  "body":[
  ('p', 'Herken je dat: hetzelfde probleem duikt steeds weer op, maar elke keer ziet het er net even anders uit? Dat betekent vaak dat je naar symptomen kijkt in plaats van naar oorzaak. Met een paar bewuste stappen kun je patronen zichtbaar maken en veel terugkerende ellende voorkomen.'),
  ('h2', 'Begin met concrete voorbeelden'),
  ('p', 'Pak drie recente situaties waarin hetzelfde knelpunt speelde. Beschrijf per geval wat er gebeurde, wie erbij betrokken waren en welke omstandigheden aanwezig waren. Door die concrete gevallen naast elkaar te leggen zie je snel overeenkomsten of verschillen.'),
  ('h2', 'Gebruik data en visualisatie'),
  ('p', 'Data hoeft niet ingewikkeld te zijn; een simpele tabel of tijdslijn helpt al. Maak grafieken of procesflows en let vooral op waar frequenties of doorlooptijden oplopen. Enkele handige dingen om te verzamelen:'),
  ('ul', ['tijdsduur van stappen', 'frequentie van fouten', 'wie er betrokken is']),
  ('p', 'Een visuele weergave maakt patronen zichtbaar die in losse verslagen verborgen blijven.'),
  ('h2', 'Check methodes voor root cause'),
  ('plink', 'Als je patroon eenmaal zichtbaar is, ga dan dieper. Tools zoals 5 Whys of een visgraatdiagram helpen om niet bij het eerste antwoord te stoppen. Wil je dit grondig aanpakken, dan kan het nuttig zijn om externe methodes te vergelijken; een praktisch startpunt is <a href="https://www.melliusbrouwer.com/root-cause-analysis-bedrijfsproblemen-oplossen" target="_blank" rel="noopener">bedrijfsproblemen structureel oplossen</a>, waar je voorbeelden en werkvormen vindt die je direct kunt toepassen.'),
  ('h2', 'Maak kleine experimenten'),
  ('p', 'Voer gerichte veranderingen uit op één plek en meet het effect. Kleine pilots verminderen risico en geven snel leerpunten. Documenteer wat je doet en wanneer, zodat je later precies kunt terugvinden welke aanpassing het verschil maakte.'),
  ('h2', 'Voorkom veelgemaakte fouten'),
  ('p', 'Een valkuil is te snel concluderen of alleen naar technische oplossingen zoeken. Vaak zit het hem in processen of communicatie. Betrek mensen uit verschillende teams; die geven vaak onverwachte inzichten. En vergeet niet: patronen veranderen, blijf monitoren en bijstellen.'),
  ('p', 'Met deze aanpak leer je niet alleen knelpunten terug te vinden, je bouwt ook aan een cultuur waarin problemen blijvend worden opgelost in plaats van steeds opnieuw opgelost.'),
  ]},
 {"slug":'softwaretesten-betrouwbare-digitale-producten','titel':'Hoe softwaretesten helpt om betrouwbare digitale producten te bouwen',"cat":'Praktijk',"datum":'2026-08-20',"datum_nl":'20 augustus 2026','lees':5,
  'resume':'Testen is niet alleen foutvissen; het zorgt dat een product doet wat het belooft, veilig blijft en prettig voelt voor gebruikers.',
  "body":[
  ('p', 'Heb je ooit een app gebruikt die constant vastloopt op het meest ongelegen moment? Dat gevoel van frustratie kan voorkomen worden door goed softwaretesten. Testen is niet alleen foutvissen; het zorgt ervoor dat jouw product doet wat het belooft, veilig blijft en prettig voelt voor gebruikers.'),
  ('h2', 'Waarom testen loont'),
  ('p', "Testen vindt problemen vroeg en goedkoop. Een bug die tijdens de ontwerpfase wordt ontdekt, kost veel minder tijd en geld om te verhelpen dan eentje die pas in productie opduikt. Bovendien helpt testen risico's te prioriteren: welke fouten hebben direct impact op de gebruiker en welke kunnen wachten?"),
  ('h2', 'Verschillende vormen van testen'),
  ('p', 'Niet één type test doet alles. Een goede aanpak combineert verschillende lagen:'),
  ('ul', ['Unit tests voor kleine onderdelen van code', 'Integratietests om te zien of modules samenwerken', 'Systeem- of end-to-end tests die echte gebruikersstromen nabootsen', 'Exploratory testing waarbij testers vrij zoeken naar onverwachte problemen']),
  ('h2', 'Automatisering en handmatig testen'),
  ('p', 'Automatisering is fantastisch voor repetitieve controles: regressietests, builds en performance checks kun je automatiseren zodat je snel feedback krijgt. Handmatig testen blijft cruciaal voor usability, toegankelijkheid en het herkennen van subtiele problemen die scripts missen. Een slimme mix van beide geeft de beste resultaten.'),
  ('h2', 'Testen en gebruikersvertrouwen'),
  ('p', 'Gebruikersvertrouwen bouw je niet met één test, maar met continu betrouwbare ervaringen. Snelle laadtijden, consistente uitkomsten en weinig crashes zorgen ervoor dat mensen terugkomen. Testen helpt ook bij beveiliging: door kwetsbaarheden vroeg te vinden voorkom je dat data en reputatie op het spel komen te staan.'),
  ('h2', 'Praktische tips om te beginnen'),
  ('plink', 'Begin klein: schrijf unit tests voor de meest kritieke functies en laat teamleden pair-testen of code reviews doen. Stel een testplan op met heldere acceptatiecriteria. En als je serieus wilt investeren in testkennis, kan een solide basiscertificering helpen, bijvoorbeeld <a href="https://startel.nl/trainingen/istqb-foundation-inclusief-examen/" target="_blank" rel="noopener">ISTQB Foundation inclusief examen</a>, die veel teams gebruiken als gemeenschappelijke taal rondom testen.'),
  ('p', 'Tot slot: testen is geen aparte activiteit aan het einde van een project, het is een mindset. Integreer testen vroeg en vaak, deel resultaten met het hele team en verbeter continu. Dan bouw je stap voor stap betrouwbaardere digitale producten.'),
  ]},
 {"slug":'telefonie-bij-een-ict-migratie','titel':'Telefonie bij een ICT-migratie: het onderdeel dat te laat aan bod komt',"cat":'Praktijk',"datum":'2026-08-19',"datum_nl":'19 augustus 2026','lees':5,
  'resume':'Werkplekken en bestanden staan in het plan. De telefooncentrale komt er meestal achteraan.',
  "body":[
  ('p', 'In een migratieplan staan de werkplekken, de bestandsopslag en de e-mail. Telefonie staat er zelden in, en komt in beeld op het moment dat het nieuwe netwerk al draait en de doorschakelingen niet meer werken.'),
  ('h2', 'Waarom het misgaat'),
  ('p', 'Telefonie hangt aan meer dan alleen een verbinding. Er zit een nummerplan achter, een keuzemenu, een reeks doorschakelingen bij afwezigheid en vaak een koppeling met het klantsysteem. Die onderdelen zijn ooit ingeregeld en daarna jarenlang niet meer aangeraakt.'),
  ('p', 'Wanneer een organisatie migreert, blijkt dan dat niemand meer weet waarom een bepaalde doorschakeling bestaat. Het gevolg is een centrale die opnieuw wordt opgebouwd op basis van aannames, met gemiste oproepen in de weken erna.'),
  ('h2', 'Wat er vooraf in kaart hoort'),
  ('ul', ['Alle nummers, inclusief de nummers die alleen intern worden gebruikt.', 'Wie welk toestel of welke app gebruikt, en op welke locatie.', "De keuzemenu's en de teksten die daarbij worden afgespeeld.", 'De afspraken over openingstijden, feestdagen en avonddoorschakeling.']),
  ('plink', 'Die inventarisatie kost een halve dag en voorkomt het grootste deel van de problemen. Wat een gehoste oplossing daarbij betekent staat bij <a href="https://www.pbxcomplete.nl/cloud-telefonie/" rel="nofollow">PBXcomplete</a>.'),
  ('h2', 'Nummerbehoud'),
  ('p', 'Nummerportering is de stap met de langste doorlooptijd en de minste flexibiliteit. Een porteringsdatum ligt vast, en die datum bepaalt vervolgens het hele migratieschema en niet andersom.'),
  ('plink', 'Plan de portering daarom vroeg en houd rekening met een overlapperiode waarin oud en nieuw naast elkaar draaien. Wat er bij zakelijke telefonie aan mogelijkheden is, staat op <a href="https://www.pbxcomplete.nl/voip-zakelijk/" rel="nofollow">pbxcomplete.nl</a>.'),
  ('h2', 'Na de overgang'),
  ('p', 'Controleer in de eerste week de gemiste oproepen en de bezetting per keuzemenu. Een verkeerd doorgezette keuze valt in een test zelden op en in de praktijk binnen dagen.'),
  ('p', 'Leg de nieuwe inrichting bovendien vast in een document dat bij de rest van de netwerkdocumentatie hoort. Dat is precies wat er bij de vorige migratie ontbrak, en zonder die vastlegging herhaalt het probleem zich over een paar jaar opnieuw.'),
  ('h2', 'Kosten die pas later zichtbaar worden'),
  ('p', "Bij de overstap wordt gerekend met de maandelijkse abonnementskosten per gebruiker. Wat er zelden bij staat, zijn de kosten van toestellen, de inrichting van keuzemenu's en het meeverhuizen van een koppeling met het klantsysteem."),
  ('p', 'Vraag daarom een opgave over drie jaar in plaats van per maand, inclusief de eenmalige posten. Een abonnement dat per gebruiker een euro goedkoper is maar een aanzienlijke inrichting vraagt, valt over die periode duurder uit dan het alternatief.'),
  ('p', 'Let daarbij ook op de opzegtermijn en op wat er gebeurt met de nummers bij beëindiging. Nummers die formeel op naam van de leverancier staan in plaats van op naam van de organisatie, maken een latere overstap aanzienlijk ingewikkelder dan hij zou moeten zijn.'),
  ("p", DISC),
 ]},
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
    <p style="margin-top:12px"><a href="https://www.dataopslagnederland.nl/" target="_blank" rel="noopener">dataopslagnederland.nl</a></p>
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
<div class="card"><h3>DLSA Letselschade Advocaten</h3><p>DLSA is gespecialiseerd in letselschade, onder meer voor (oud-)militairen met gezondheidsklachten door chroom-6 of PTSS, en begeleidt schadeclaims tegen Defensie.</p><p style="margin-top:10px"><a href="https://dlsa.nl/letselschade/ambtenaar/schadeclaim-defensie/" target="_blank" rel="noopener">defensie advocaat</a></p></div><div class="card"><h3>Intermax</h3><p>Intermax biedt Nederlandse cloudoplossingen, met dienstverlening op het gebied van private cloud voor bedrijven die waarde hechten aan controle en dataresidentie.</p><p style="margin-top:10px"><a href="https://www.intermax.nl/oplossingen/cloudoplossingen/private-nederlandse-cloud/" target="_blank" rel="noopener">nederlandse cloud</a></p></div><div class="card"><h3>LeadToday</h3><p>LeadToday is een Nederlands online marketing bureau met specifieke dienstverlening voor consultancybureaus op het gebied van leadgeneratie.</p><p style="margin-top:10px"><a href="https://www.leadtoday.nl/focusbranches/consultancy-marketing" target="_blank" rel="noopener">consultancy marketing</a></p><div class="card"><h3>Init3</h3><p>Init3 uit Heerenveen verzorgt ICT-support voor het midden- en kleinbedrijf, met een telefonische helpdesk, hulp op afstand, bezoek ter plaatse en doorlopende bewaking van servers en netwerk.</p><p style="margin-top:10px"><a href="https://www.init3.nl/diensten/ict-support/" target="_blank" rel="noopener">ICT support via Init3</a></p></div>
</div>
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
