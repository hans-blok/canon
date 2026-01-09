# Wetten van IT-Ontwikkeling

Deze wetten zijn verzamelde wijsheden en principes die software-ontwikkeling en IT-projecten beheersen.

## Wet van Conway

> "Organisaties die systemen ontwerpen, zijn gedwongen ontwerpen te maken die de communicatiestructuur van deze organisaties kopiëren."
> — Melvin Conway, 1967

**Implicatie**: De architectuur van je software weerspiegelt de structuur van je organisatie. Als je monolithische teams hebt, krijg je monolithische systemen. Als je teams autonoom zijn, krijg je modulaire systemen.

## Wet van Brooks

> "Het toevoegen van mensen aan een te laat softwareproject maakt het nog later."
> — Fred Brooks, "The Mythical Man-Month", 1975

**Implicatie**: 
- Communicatie-overhead neemt exponentieel toe met teamgrootte
- Nieuwe teamleden hebben inwerktijd nodig
- Kennisoverdracht kost tijd van bestaande teamleden

## Wet van Hofstadter

> "Het duurt altijd langer dan je verwacht, zelfs als je rekening houdt met de Wet van Hofstadter."
> — Douglas Hofstadter, "Gödel, Escher, Bach", 1979

**Implicatie**: Software-schattingen zijn notoir onbetrouwbaar. Plan buffers in, en realiseer je dat zelfs die buffers te klein kunnen zijn.

## Wet van Pareto (80/20-regel)

> "80% van de resultaten komen voort uit 20% van de inspanningen."
> — Vilfredo Pareto

**Implicatie in software**:
- 80% van bugs zitten in 20% van de code
- 80% van gebruikers gebruikt 20% van de features
- 80% van waarde komt uit 20% van de functionaliteit

## Wet van Postel (Robustness Principle)

> "Wees conservatief in wat je stuurt, wees liberaal in wat je accepteert."
> — Jon Postel, RFC 761, 1980

**Implicatie**: Systemen moeten tolerant zijn voor variaties in input, maar strict in hun eigen output. Dit bevordert interoperabiliteit.

## Wet van Linus

> "Met genoeg ogen zijn alle bugs oppervlakkig."
> — Eric S. Raymond, "The Cathedral and the Bazaar", 1999

**Implicatie**: Open source en code review verhogen de kwaliteit. Meer mensen die naar code kijken, verhoogt de kans dat problemen worden gevonden.

## Wet van Hyrum

> "Met een voldoende groot aantal gebruikers van een API, maakt het niet uit wat je in het contract belooft: alle waarneembare gedragingen van je systeem zullen door iemand afhankelijk worden gemaakt."
> — Hyrum Wright

**Implicatie**: Elke implementatie-detail kan een publieke API worden. Backward compatibility is moeilijker dan je denkt.

## Wet van Wirth

> "Software wordt sneller langzamer dan hardware sneller wordt."
> — Niklaus Wirth

**Implicatie**: Hardware-verbeteringen worden vaak tenietgedaan door software-bloat. Performance moet een bewuste keuze zijn.

## Wet van Zawinski

> "Elk programma probeert uit te breiden totdat het email kan versturen. Programma's die niet kunnen uitbreiden om email te versturen, worden vervangen door programma's die dat wel kunnen."
> — Jamie Zawinski

**Implicatie**: Feature creep is onvermijdelijk. Systemen groeien in complexiteit tenzij actief beheerd.

## Wet van Greenspun

> "Elk voldoende complex C- of Fortran-programma bevat een ad hoc, informeel gespecificeerde, bug-rijke, trage implementatie van de helft van Common Lisp."
> — Philip Greenspun

**Implicatie**: Complexe systemen herbouwen uiteindelijk features die al bestaan in krachtigere talen of frameworks. Kies je tools zorgvuldig.

## Wet van Gall

> "Een werkend complex systeem evolueert altijd uit een werkend eenvoudig systeem. Een complex systeem ontworpen vanaf nul werkt nooit en kan niet worden gerepareerd om te werken. Je moet opnieuw beginnen met een werkend eenvoudig systeem."
> — John Gall, "Systemantics", 1975

**Implicatie**: Start klein en itereer. Big bang rewrites falen meestal. Evolutionaire architectuur werkt beter.

## Wet van Eagleson

> "Elke code waar je meer dan 6 maanden niet naar hebt gekeken, is net zo goed geschreven door iemand anders."
> — Eagleson

**Implicatie**: Schrijf leesbare, gedocumenteerde code. Je toekomstige zelf zal je dankbaar zijn.

## Wet van Kernighan

> "Debuggen is twee keer zo moeilijk als code schrijven. Dus als je code zo slim mogelijk schrijft, ben je per definitie niet slim genoeg om het te debuggen."
> — Brian Kernighan, "The Elements of Programming Style", 1974

**Implicatie**: Schrijf eenvoudige, begrijpelijke code. Slimheid is vaak een nadeel, geen voordeel.

## Wet van Lehman

> "Een systeem dat gebruikt wordt, zal blijven evolueren, anders wordt het steeds minder nuttig."
> — Manny Lehman, 1974

**Implicatie**: Software-onderhoud is geen keuze, het is een noodzaak. Systemen die niet evolueren, sterven.

## Principe van Least Surprise (POLA)

> "In interface design, doe altijd het minst verrassende ding."

**Implicatie**: Consistentie en voorspelbaarheid zijn belangrijker dan creativiteit in API- en UI-design.

## YAGNI (You Aren't Gonna Need It)

> "Implementeer dingen alleen wanneer je ze daadwerkelijk nodig hebt, niet wanneer je voorspelt dat je ze nodig zult hebben."
> — Extreme Programming

**Implicatie**: Voortijdige abstractie en over-engineering verspillen tijd en voegen complexiteit toe.

## DRY (Don't Repeat Yourself)

> "Elk stukje kennis moet een enkele, ondubbelzinnige, gezaghebbende representatie hebben binnen een systeem."
> — Andy Hunt en Dave Thomas, "The Pragmatic Programmer", 1999

**Implicatie**: Duplicatie leidt tot inconsistenties en onderhoudsproblemen. Abstractie moet doordacht zijn.

## KISS (Keep It Simple, Stupid)

> "De meeste systemen werken het beste als ze eenvoudig worden gehouden in plaats van complex gemaakt."
> — Kelly Johnson, Lockheed Skunk Works

**Implicatie**: Eenvoud is een deugd. Complexiteit moet verdiend worden, niet het standaard zijn.

## Wet van Metcalfe

> "De waarde van een netwerk is proportioneel aan het kwadraat van het aantal verbonden gebruikers van het systeem."
> — Robert Metcalfe

**Implicatie**: Netwerkeffecten zijn krachtig. Platforms en ecosystemen worden exponentieel waardevoller met adoptie.

## Wet van Reed

> "De waarde van grote netwerken groeit exponentieel met de grootte van het netwerk."
> — David P. Reed

**Implicatie**: Groepsvorming in netwerken (sociale netwerken, forums) creëert nog meer waarde dan simpele connecties.

## Principe van Least Privilege

> "Elk programma en elke gebruiker van het systeem moet opereren met de minimale set privileges die nodig zijn om de taak te voltooien."

**Implicatie**: Beveiliging door beperking van toegang. Minimaliseer de impact van security breaches.

## Murphy's Law voor Software

> "Als iets fout kan gaan, zal het fout gaan."

**Implicatie**: Plan voor fouten. Defensive programming, error handling, logging, monitoring en graceful degradation zijn essentieel.

---

**Conclusie**: Deze wetten zijn geen absolute waarheden, maar patronen die keer op keer waargenomen worden in software-ontwikkeling. Ze helpen om realistische verwachtingen te scheppen en betere ontwerpbeslissingen te nemen.

---

*Dit document bevat verzamelde wijsheden uit de IT-wereld die software-ontwikkelaars, architecten en projectmanagers helpen betere beslissingen te nemen.*
