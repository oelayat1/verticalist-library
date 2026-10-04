# The Dark Marketplace

Published: 2026-05-01
Type: essay
Summary: Explores agent-run marketplaces where discovery, negotiation, and purchasing happen out of sight, making buyer judgment and learning loops central to defensibility.
Original PDF: 2026-05-01 The Dark Marketplace.pdf

## Essay text

The Dark Marketplace
Vertical AI is coming for commerce — the winners will be the
ones that learn how buyers think
MAY 01, 2026
Last week, Anthropic published the results of an experiment called
Project Deal. For one week, inside their San Francisco office, 69
employees listed personal items for sale — snowboards, office chairs,
bags of ping-pong balls — on a classified marketplace run entirely by AI
agents. Every negotiation, every counteroffer, every deal was handled
by Claude models acting on behalf of their assigned humans. No one
typed a price. No one browsed a listing. The agents read a brief intake
interview, figured out what each person wanted, and went to work.
The result: 186 completed deals, over $4,000 in total value, real money
changing hands. One participant’s agent bought them a snowboard they
already owned. Another’s agent negotiated a deal so efficiently the
human didn’t realize it had happened until the experiment ended —
autonomy, whether they wanted it or not.Per Anthropic, on their Project Deal results: “Same broken
folding bike. Same buyer. Same seller. Haiku sold it for $38.
Opus got $65.”
The most telling finding, though, wasn’t deal volume. Anthropic secretly
split participants between their frontier model and a smaller, less
capable one. Users represented by the stronger model got objectively
better outcomes — better prices, better matches, more deals. But the
humans on the losing end didn’t notice. They had no idea their agent
was underperforming. Anthropic’s term for this: “agent quality gaps.”
Five days later, Amazon, Meta, Microsoft, Salesforce, and Stripe joined
the Universal Commerce Protocol council — the first serious attempt to
standardize how AI agents discover products, negotiate prices, and
execute transactions across platforms. The same week, eBay updated
its terms of service to explicitly ban “buy-for-me agents, LLM-driven
bots, or any end-to-end flow that attempts to place orders without
human review.”
The battle lines are drawn. Some of the largest companies in commerce
are racing to build the infrastructure for a world where agents transacton behalf of humans. Others are trying to lock the door before the
agents get in.
Both camps see the same future. We’re calling it the Dark Marketplace: a
transactional, multi-sided platform where the complex work of
discovery, negotiation, and purchase happens entirely out of sight. Not
“dark” as in illicit — dark as in dark matter. The invisible force that holds
the system together, but that no one directly observes.
We believe Dark Marketplaces have the potential to create hundreds of
billions in enterprise value by eroding the key friction inherent in even
the most successful marketplaces today. But building one requires
solving a problem that goes far deeper than better search or naturallanguage UI. It requires abstracting human judgment — the gut-level,
context-dependent, edge-case-handling decision-making that makes
experienced buyers and sellers effective — and encoding it into an
agent that can act on their behalf.
This essay is about how that happens, which companies are positioned
to do it, and what founders should build toward.
Thanks for reading The Verticalist! Subscribe
for free to stay ahead of the curve in Vertical
AI.
Subscribed
A Brief History of Commerce Getting
SmarterEvery major leap in commerce has been accompanied by a shift in
demand intent from the buyer’s mind to external systems.
Understanding this arc matters because each migration has produced a
corresponding explosion in both transaction volume and buyer
satisfaction — and the current moment represents the largest migration
yet.
For roughly 7,000 years, the dominant mechanism for externalizing
demand intent was a good salesperson. From Bronze Age agoras to
Bloomingdale’s, the source was someone who remembered what you
liked, what you’d bought before, and what you could afford. Merchants
built increasingly sophisticated environments — bazaars, malls,
department stores, showrooms — designed to crystallize purchase
intent at the point of sale. The information lived in a person’s head, and
the best merchants were those who kept it there the longest.
Over the last twenty years, digital breadcrumbs — ad data, purchase
history, demographic profiles, search behavior — created a second
external source of demand intent. This enabled the recommendation
engines, retargeting campaigns, and personalized pricing that built
Amazon, Meta, and the modern e-commerce stack. But even with all
that data, the fundamental transaction model barely changed. Buyers
still search, filter, compare, and click “buy.” Sellers still optimize SKU
pages, photos, and reviews to convert at the point of sale. The data
made the guessing game more efficient, but it remained a guessing
game: please tell us what we might be able to sell you.
B2B system integration — ERP, POS, WMS, TMS feeds — created a third
layer roughly a decade ago. Companies like Faire, Odeko, and
GrubMarket used these integrations to build procurement marketplaces
that could infer what buyers need before they search. This was a real
step forward: the system didn’t just respond to expressed intent, it
anticipated latent demand based on operational data. But the buyer still
made the final call. The human remained in the loop — reviewing a
suggested order, approving a cart, and confirming a substitution.Now we’re at the threshold of a fourth migration. LLMs can absorb
natural-language context, learn from behavioral patterns across
thousands of interactions, and act autonomously. The gap between
“system anticipates what you need” and “system acts on what you
need” is closing fast.
Each previous migration produced a massive increase in transaction
volume and buyer satisfaction. Faster, more efficient deals generate
surplus, which, in an efficient market, flows into better service and
lower prices. The pattern is consistent enough to be treated as
structural. And LLMs’ natural-language and abstraction capabilities are
the best-suited technology we’ve seen to migrate an unprecedented
share of demand intent out of buyers’ heads.
To unlock this, however, AI-native marketplaces and commerce engines
have to do much more than expose merchandising to natural language.
The key to autonomous, trusted, and accurate transactions at scale is
the abstraction of human judgment.
Current LLMs and image diffusion models are trained on the biggest
corpuses of freely available human data we have: writing, photos,
videos. World and physical AI models, in contrast, are training labelled
captures of human action and behavior. What’s the analog for
transactional judgment?
Every marketplace and SaaS tool on earth can capture stated
preferences. Dropdowns, filters, onboarding surveys, saved searches —
these are table stakes. But human buying judgment relies on something
much richer than what fits in a form field, much more nuanced even
than an optimization based on past purchases.
Judgment Abstraction is the Gateway
ProblemThe defining challenge — and the defining moat — for the next
generation of transactional B2B businesses is the ability to abstract
complex human judgment: the tacit, context-dependent, real-time,
edge-case-handling decision-making that separates a stated preference
from a trusted purchase decision. It’s usually highly vertical by nature.
Its contours vary widely by industry, company, and even individual.
Consider a café owner in Portland ordering supplies. She doesn’t just
order “oat milk.” She knows that her Tuesday afternoon traffic spike
requires a specific volume, that her primary supplier’s delivery window
shifted three weeks ago, that a particular substitute brand will alienate
two of her regulars, and that she’s been meaning to try a new cold-brew
concentrate but only if it arrives before the weekend rush. Some of this
is preference. Most of it is judgment — accumulated through years of
operating this specific café, serving these specific customers, working
with these specific suppliers.
Or consider a freight broker dispatching a load. He doesn’t follow a
decision tree. He knows which carriers reliably answer the phone late
Friday afternoon, which lanes are soft this week based on conversations
he had yesterday, which shipper’s “firm” rate actually has room, and
when it’s worth eating margin to preserve a relationship. That
knowledge doesn’t live in a CRM. It lives in his head, reinforced by
thousands of reps across thousands of loads.
Or consider a physician choosing a treatment protocol. She weighs the
patient’s history, her own clinical experience, the insurance formulary,
the likelihood of compliance, and the latest evidence — simultaneously.
OpenEvidence can surface the literature. But the physician’s judgment
about this patient in this moment is what matters.
These examples share a common structure. The judgment is per-user,
per-context, and per-moment. It’s shaped by experience, not just data.
The Ghost in the MachineAnd it’s precisely the thing that AI agents need to absorb if they’re
going to transact on someone’s behalf without destroying trust.
Building a Dark Marketplace, then, means building systems that don’t
just ask users what they want—they observe, absorb, and learn how
users actually decide across hundreds or thousands of interactions. You
could think of this as another tier of model training, except the “model”
is per-user and the “training data” is the messy, unstructured reality of
daily operations. And this abstraction may differ not only company to
company, but user to user. The Portland café owner and the Dallas café
owner may carry identical inventory and make radically different
purchasing decisions.
How do you build this? The answer is a function of two variables: how
deeply your product engages with the user’s decision-making process,
and how close it sits to the actual transaction.
We think the most useful way to evaluate a company’s Dark
Marketplace potential runs along two axes — both of which speak to
the ability to abstract the appropriate judgment.
The Engagement-Proximity MatrixMeasures how much high-frequency, low-friction interaction the
product captures. High-engagement products are those that users
interact with daily, sometimes hourly, and whose interactions generate
rich behavioral signals. Voice AI that listens to every customer call. A
POS integration that sees every transaction in real time. A workflow tool
embedded in the daily operating rhythm of the business. Lowengagement products are the ones users touch quarterly, or only during
onboarding — heavy configuration UIs, periodic surveys, static system
integrations that pipe data but don’t observe behavior.
Measures how close the product sits to the actual purchase or sale
decision. High-proximity products facilitate, mediate, or execute
transactions. They’re the system through which orders get placed, loads
get booked, and appointments get scheduled. Low-proximity products
inform decisions but don’t facilitate them— such as analytics
X. Engagement Depth
Y. Transaction Proximitydashboards, coaching tools, clinical decision support, and market
intelligence platforms.
The interplay between these two dimensions determines a company’s
path to the Dark Marketplace.
1. Top-right: Dark Marketplace–ready.
These companies capture rich behavioral data and sit on the
transaction. They can progress through the full journey of judgment
abstraction — from stated preferences to autonomous decisionmaking — because they have both the signal and the surface area
to act on what they learn. This, obviously, is the end-state and holy
grail.
2. Top-left: Rich signal, wrong place.
These companies capture enormous amounts of judgment data
through high-frequency interaction, but they don’t (yet) facilitate
the transaction itself. Rilla is the archetype: it records and analyzes
every in-person contractor sales conversation, giving it proprietary
data on what language and techniques close deals in home
services. But Rilla doesn’t close the deal. The path forward is to
extend toward the transaction — if Rilla builds into lead routing,
quoting, or contractor-side procurement, the data it’s already
capturing becomes the basis for a marketplace priced on proven
persuasion. OpenEvidence is similar: it absorbs a physician’s
clinical decision-making reflex, but sits upstream of the
prescription, the diagnostic order, the device selection. The path:
become the routing layer between physicians and the downstream
systems where clinical decisions get executed. Keychain may be
the purest two-sided Dark Marketplace candidate in the cohort —
with $78M raised in just 18 months, the platform connects 30k+
CPG co-manufacturers with 20k+ brands / retailers. A brand AI
describes a product spec; manufacturer AIs bid against it.3. Bottom-right: Transaction seat, slow learner.
These companies sit on the transaction but learn slowly because
interactions are infrequent, shallow, or insufficiently captured.
Odeko lives here: its POS integration provides a real-time demand
signal, its overnight delivery network handles transactions, and its
auto-reorder engine absorbs the café owner’s entire purchasing
judgment. The owner wakes up to a stocked kitchen, not a catalog.
Faire is a useful example of the opportunity in this quadrant: it’s
already an $8B+ wholesale marketplace connecting over 700,000
retailers with brands, and it’s literally facilitating the transaction.
But today, a retailer still browses. Faire could layer in AI to capture
a retailer’s daily sales patterns, foot traffic, vendor conversations,
and seasonal behavior — the engagement signals that make autocuration possible. The retailer would see a suggested cart, not a
catalog. LightSource tells the same story from the procurement
side: automating RFX & bids for enterprises like Yum! Brands and
Hello Fresh, proximity is high — but procurement events are
periodic, not continuous. The path to the top-right: capture the
inter-cycle signals like supplier emails, market pricing shifts, and
informal negotiations.
The strategic implication is asymmetric. Companies in the top-left need
to build toward the transaction — extending into procurement, ordering,
checkout, and booking. Companies in the bottom-right need to earn
engagement — layering in AI capture via voice, conversation, behavioral
inference, and deeper workflow embedding. The winners will be those
who close whichever gap they have the fastest.
The proximity gap is a matter of product extensibility toward the
fruition of transactions. The engagement gap is a bit more nuanced, but
AI itself offers new modalities to jump it. We discussed this in our piece
on voice-first playbooks in Vertical AI:
One of the most interesting emerging use cases of Voice AI we have been
thinking about centers around multi-party transactions and brokering.Digital marketplaces have struggled to gain traction in many segments,
often because of unwillingness to share margin or complexity in facilitating
the transaction. But a voice-first digital brokering model could unlock value.
Parties (both human and agentic) could interact through voice — instead of
endless email chains — to move transactions forward. — The Verticalist
For a future Dark Marketplace, voice and or other multi-model AI can be
more than just hot wedge products. They can power the engagement
layer that makes judgment abstraction possible — the mechanism by
which a platform learns how its users actually think, not just what they
say they want.
Toma — a resident of our top-left quadrant — is a case in point. Its AI
voice agents handle 100% of a dealership's inbound calls (service
scheduling, parts orders, recall checks, sales inquiries), trained on each
store's call corpus and integrated into the DMS. The Dark Marketplace
potential emerges when the other side gets an agent too: an insurer's
claims AI calls Toma to schedule a repair, an OEM's recall agent books
warranty service, a customer's AI price-shops a brake job across three
dealers. Agent-to-agent, no hold music required.
Once a company is positioned in the right quadrant — high
engagement, high proximity — how does it actually progress toward a
Dark Marketplace? In our emerging playbooks piece, we defined the
concept of the Authoring Layer:
We see AI wedges as — ideally — the launch point for a particular highvalue workflow. A motion that doesn’t just automate something; it results in
an output that will be used and increasingly relied upon by the business. We
call this species of wedge solution the “Authoring Layer.” Because it is the
first step in a process, it often does not require substantial integrations with
The Four Stages of Judgment Abstractionpre-existing SaaS. It creates something that a human would’ve created —
documentation, notes, a lead, an appointment — and hands it off to
another system as a human would have. — The Verticalist
The Dark Marketplace journey is what happens when the authoring layer
matures beyond creating outputs a human would have created, and
starts making decisions a human would have made. We think that the
journey follows four stages, each building on the last.The user tells the system what they want. Filters, onboarding surveys,
saved searches, and approval limits. Every marketplace does this. A
Faire retailer selects “home goods” and “under $50 wholesale.” A Torch
Stage 1 — Stated PreferencesDental office manager sets par levels for gloves and composite. This is
the starting line, and the data generated here is useful but shallow.
The system observes what the user does and infers patterns that the
user never articulated. POS velocity, reorder frequency, time-on-page,
substitution acceptance rates, and supplier switching behavior. Odeko
notices that a café reorders oat milk every six days, not seven, and that
volume drops on Mondays. It adjusts the auto-order without being told.
The user doesn’t have to explain their behavior; the system reads it. This
is where most AI-native vertical companies are today or working
toward.
The system integrates external context — market conditions, supplier
reliability, perishability, seasonality, counterparty behavior, and
regulatory constraints — to make decisions the user would make if they
had unlimited time and perfect information. GrubMarket’s AI agent
recognizes a regional tomato shortage from supply-chain signals
across its network, switches a distributor’s order to a substitute variety
at a comparable price point, and factors in that distributor’s historical
tolerance for substitutions before acting. Green Cabbage benchmarks a
Salesforce renewal against thousands of comparable contracts to set a
walkaway price that the buyer’s own procurement team couldn’t
calculate. This stage requires both deep user-specific data and broad
market data — the combination of engagement and proximity.
The agent acts on behalf of the user with minimal or no human
oversight. The transaction is “dark” — the user sees the outcome, not
the process. No company operates here yet — but the projected
endgame is visible. A broker-side AI receives a load request, queries
carrier-side AIs, negotiates rate and timing, books the load, confirms the
pickup, and sends a summary. A brand AI submits a product spec,
Stage 2 — Behavioral Inference
Stage 3 — Contextual Judgment
Stage 4 — Autonomous Decision-Makingmanufacturer AIs bid against it, and both sides see only the deal. Human
decision-makers intervene on exceptions, not defaults.
The connection between the two frameworks is direct: only companies
in the top-right quadrant of the engagement × proximity matrix can
realistically progress through all four stages. Companies with
engagement but low proximity may reach Stage 2, but Stages 3 and 4
require both deep behavioral data and the ability to execute on what
the system has learned. Companies with proximity but low engagement
may handle Stage 1 transactions efficiently, but will struggle to infer and
act on the judgment patterns that make autonomous decision-making
trustworthy.
Consumer agentic commerce gets the headlines because of the scale of
the opportunity. OpenAI embedded checkout in ChatGPT. Amazon’s
Rufus handled 250M shoppers in 2025, although we do wonder how
many of those interactions were more from morbid curiosity than utility.
Why Consumers Won’t Lead the Way“Rufus on Rash Cream,” now streaming wherever you watch
and listen!
Morgan Stanley predicts half of online shoppers will use AI agents by
2030. PYMNTS found that 41% of consumers have already used AI for
product discovery. And yet, almost none of those consumers completed
a purchase through the agent. What’s billed as a revolution in commerce
is, for now, “a highly intelligent search bar.” The models are excellent atresearch and shortlisting. The infrastructure to execute the purchase
autonomously remains a gap.
We believe dark Marketplaces will emerge first in B2B, and for structural
reasons.
Much of B2C purchasing actively resists judgment abstraction. For
many consumers, the buying journey — the discovery, the browsing, the
choosing — isn’t friction to be eliminated. It’s the product. Seventy
percent of consumers say they want personalized in-store service, and
73% of Gen Z — the most digitally native cohort — shop in-person at
least once a week, more than Baby Boomers. Billions are spent on highend retail showrooms, experiential flagship stores, and grocery halls for
a reason.
DTC subscription models have proven that some narrow, predictable
replenishment buying can be automated — toothpaste, razors, dog
food — but even here, the ceiling is remarkably low. Only 23% of U.S.
Amazon customers actively use Subscribe & Save, despite over a decade
of investment in the most frictionless auto-replenishment product ever
built. Subscription box churn rates of 10–20% monthly are considered
normal in DTC. Amazon's attempt to go further with Alexa —
abstracting not just reordering but the entire purchase decision through
voice — has been an instructive failure. Alexa, a voice commerce
solution in search of a problem, has been running Amazon 7-8 figure
losses.
Anthropic’s hilarious Project Vend — in which they put a Claude instance
in charge of a vending machine — was clearly a marketing stunt.
“Claudius” took about a month to go bankrupt — hallucinating fake
vendors, an identity (“blue blazer and a red tie”), and raging demand for
“metal cubes” along the way. But it summed up nicely how not to
No Alexa, I Don’t Want to Subscribe to Pizza
Bagelsattempt AI-automated commerce: ignore judgment abstraction, isolate
the system from substantive sources of progressive learning, apply no
deterministic guardrails, and focus on a preference-driven consumer
purchase.
“Claudius’… most precipitous drop was due to the purchase
of a lot of metal cubes that were then to be sold for less
than what Claudius paid.” — Anthropic
Outside of a small minority of roles — fashion or art buyers, for
example — business procurement is repeat, policy-driven, and marginoriented. B2B buyers operate within procurement budgets, approved
vendor lists, compliance constraints, and established reorder cadences.
Their decisions are more abstractable than a consumer deciding between
sneakers — there are more patterns to detect, more rules to encode,
more operational data to learn from. A café ordering supplies every
morning is a far better substrate for judgment abstraction than a
consumer buying a birthday gift once a year.
Dark Marketplaces are a B2B GameB2B buyers already share operational data with platforms. ERP
integrations, POS feeds, inventory APIs — the data-sharing and
integration work required for judgment abstraction is table stakes in
B2B, not a privacy negotiation. Even if it’s much more complex and
often difficult to capture, the data exists and there is significant
incumbent plumbing to leverage.
And once an agent absorbs a buyer’s operational heuristics —
substitution tolerances, timing patterns, supplier preferences, risk
appetite — the relationship becomes the moat. Ripping out the agent
means losing institutional memory. Switching costs compound with
every interaction, deepening the moat automatically over time. We
explored this dynamic in our emerging playbooks piece through the lens
of authoring layers and systems of intelligence: the system that
captures the most workflow data eventually becomes the system of
record.
Dark Marketplaces take this one step further — the system that
captures the most judgment data becomes the system of action. When
that action anchored in a profit motive, rather than an experience one,
incentives towards pure automation align.
The classic framework for marketplace success — drawn here from the
team at NEA and from Jonathan Golden’s work at Airbnb — centers on
three demand-side enablers: Discovery, Convenience, and Trust. On the
supply side, the analogs are Utilization, Revenue, and Convenience.
These create flywheels that drive platform metrics: fill rate, time-topurchase, demand retention, AOV, take rate, leakage.
How “Dark” Transforms Marketplace
FundamentalsTo be clear, when we say “Dark Marketplaces” we mean all forms of
transactional platform — not necessarily marketplaces in the traditional
business model sense. That said, many of the same drivers and metrics
will apply to Dark Marketplaces. And many of these, in turn, will be
fundamentally transformed (or made obsolete) by agentic automation.
In a traditional marketplace, discovery is the primary value proposition
— aggregating fragmented supply, optimizing the buyer’s ability to find
the best counterparty. In a Dark Marketplace, the buyer doesn’t
discover the supply. The agent knows what the buyer needs, finds it,
evaluates it, and either presents a recommendation or completes a
transaction. Discovery friction approaches zero. Jonathan Golden
described how reducing “cognitive load” in heterogeneous
marketplaces was the key challenge for buyer conversion. Dark
Marketplaces solve this by removing the human from the discovery
loop entirely.
NEA framed convenience as a “utility leap forward” — making it
significantly easier for both supply and demand to get on-platform and
Discovery becomes elimination.
Convenience becomes invisibility.transact. In a Dark Marketplace, the leap is from “easier” to “invisible.”
The transaction happens in the background. The buyer’s first instinct is
to check a notification from their agent, not to open a browser and
start browsing a feed of SKUs.
In traditional marketplaces, trust is built through reviews, brand
reputation, fulfillment reliability, and return policies — all signals
designed to reassure a human making a judgment call. In a Dark
Marketplace, trust attaches to the agent’s track record. Did it save
money? Avoid stockouts? Handle exceptions gracefully? Choose the
right substitute? Trust becomes measurable and continuous, not a onetime assessment at the point of purchase.
These transformations mitigate the classic marketplace failure modes —
poor discovery, insufficient convenience, and lack of trust. But they
introduce a new one: judgment drift. If the agent makes a few bad calls
— wrong substitution, an overstock, a missed timing window — the user
overrides it, stops trusting it, and re-engages manually. Maintaining
judgment accuracy across changing conditions, evolving preferences,
and edge cases becomes the new retention metric. This is why the
engagement axis matters so much: the more continuously the system
observes, the faster it corrects, and the less likely judgment drift
becomes.
Not all startups looking to transform the fundamentals are on equal
footing. Vertical AI and vertically integrated players have an unfair
advantage here. In some markets, incumbency may also offer an edge.
GrubMarket is an interesting example here — with ~$680M raised and a
$3.5B valuation, they’re 12 years old. But that time in market has
allowed them to build a lot of leverage. They’re both the marketplace
and the supplier: running warehouses and distribution across all 50
states while selling WholesaleWare, an AI-powered ERP, to third-party
distributors. Last year, it launched purpose-built AI agents for inventory,
Trust shifts from perceptual to empirical.reporting, and monitoring. Because GrubMarket controls supply,
demand, and the intelligence layer, its agents train on both sides of
every transaction. The endgame: wholesaler agents auto-negotiate with
grower agents and GrubMarket captures the spread.
Across the landscape of funded vertical AI companies, a handful seem
to be approaching the Dark Marketplace threshold from different
angles. Though none, of course, has arrived at the eventual end-state:
true AI-automated, human-free commerce. Below are the companies we
find most instructive, organized by their current phase of judgment
abstraction.
The Dark Marketplace Landscape
36 Vertical AI startups positioned to enable autonomous commerce, mapped by
Abstraction Layer phase (cf. Journey to Dark Marketplace chart).
So how does competition play out? Like in traditional marketplaces and
commerce, there will be 800-pound gorillas thriving alongside vertically
focused, even niche players. While we strongly believe AI-nativity is
going to key to velocity on the Dark Marketplace approach, the optimal
angle of attack is something we’re still watching closely. Let’s consider
freight brokerage. Augment ($110M, Redpoint-led) embeds deeply into
one side of the workflow — full order-to-cash automation across $35B
in freight under management. FleetWorks ($17.5M, First Round-led) is
two-sided from day one — its AI dispatcher serves both carriers and
brokers, with 10,000+ carriers and Uber Freight already on-platform. An
open question: does depth-first (focus on building AI into a single ICP
on one side of the network) or breadth-first (start with both sides
already present, progressing toward agent-to-agent clearing eventually)
reach Phase 4 faster?
The Dark Horses of Autonomous
CommerceAs we wrote in Software Is Dead — Long Live Software: “The immutable
primitives of software defensibility are workflow and data. Speed is a
compounding advantage in the early days of a category, but it is not a
durable moat.” In the Dark Marketplace context, this means the wedge
— the voice agent, the auto-reorder, the procurement bot — is
necessary but insufficient alone. We explored why in our essay on the
Dispatcher Problem:
An AI Service company whose primary value is “we deliver this service
cheaper by using LLMs” is a dispatcher sitting on a proprietary margin
advantage that doesn’t belong to them. It belongs to the cost curve of
inference — and that curve is controlled by model labs, hyperscalers, chip
manufacturers, and energy producers. — The Verticalist
The escape route from the Dispatcher Problem is judgment data. Peruser, per-context, accumulated over thousands of interactions — the
kind of data that gets more valuable the longer the relationship lasts,
and that a competitor can’t replicate by plugging into the same model
API. Five principles for founders building toward this:
If you have to choose one, lean engagement. Retrofitting ambient data
capture is much harder than extending a product toward a transaction.
Voice AI, conversation capture, and workflow-embedded tools are
better wedges than dashboards or analytics — they generate the
behavioral data that judgment abstraction requires. For Dark
Marketplaces, the authoring layer is the engagement surface.
Takeaways for Founders Building Dark
Marketplaces
Start with the wedge that maximizes engagement and
proximity
Design for per-user judgment capture, not aggregate
preferencesThe Dark Marketplace advantage is that every user’s agent is different
— trained on that user’s specific behavior, context, and edge cases.
Build structured memory, per-user context retrieval, and feedback loops
from day one. These aren’t features to add later; they’re the
architecture. The per-user fine-tuning challenge is real — latency, cost,
and negative artifacts grow with context window size — but the
approaches emerging around memory layers, retrieval-augmented
generation, and parameter-efficient adapters are exactly the right
toolkit.
Food distribution, freight, construction materials, dental supplies,
specialty pharma, auto parts — verticals where buyers make dozens of
decisions per week, and supply is heterogeneous enough to justify
intermediation. These are the markets where judgment abstraction
produces the highest ROI: enough decision volume to learn quickly,
enough supply complexity to create real value, and enough repeat
behavior to compound switching costs. Also, learn the lesson many B2B
Marketplaces have over the last decade: if you don’t understand why
brokers and distributors exist in your vertical, there’s a good chance
you misunderstand their service role or leverage point.
Don’t build an autonomous agent on day one — you’ll lose trust before
you’ve earned it. Build a system that captures stated preferences, earns
the right to infer behavior, proves it can handle contextual judgment,
and only then operates autonomously. Each stage is a trust-building
exercise with the user base. Trying to skip stages is how you get
judgment drift, manual overrides, and churn.
In a Dark Marketplace, the interface is fungible. What matters is the
accumulated knowledge of how this buyer decides — substitution
Pursue B2B verticals with repeat purchasing and fragmented
supply
Plan the journey from Stage 1 to Stage 4
Remember that the moat is memory, not UItolerances, timing preferences, risk appetite, supplier relationships. That
memory is the switching cost. Invest in it like infrastructure, because
your competitors will.
When Anthropic ran Project Deal, the detail that stuck with us wasn’t the
number of deals or the dollar volume. It was what happened with the
weaker model. Participants represented by the less capable AI got
worse outcomes, but had no idea. They couldn’t tell their agent was
underperforming because they only saw the result, not the process.
This is the core tension of the Dark Marketplace. When the transaction
goes dark, the quality of the agent’s judgment becomes everything. A
great agent saves money, avoids stockouts, finds better suppliers, and
handles exceptions gracefully. A mediocre one makes quiet mistakes
that compound over time. And the user can’t tell the difference until the
damage is done and trust is gone (likely forever).
That’s why judgment abstraction is the moat, the product, and the risk all
at once. The companies that will build the next hundred-billion-dollar
marketplaces won’t win on merchandising or slick UX. They’ll win
because they deeply understand their customers and build systems that
think like them, reliably. And of course, because they succeed in
eliminating market inefficiencies, deadweight loss, time lost, and human
mistakes across trillions of transactions.
You may be familiar with Adam Smith’s “invisible hand.” Contrary to the
popular mythos, the metaphor was meant to illustrate not the universal
efficiency of markets, but rather that self-interested choices by market
participants, collectively, can benefit society. The “hand” of the market
is invisible because it’s defined by choices buried in the heads of billions
of buyers and sellers. When the buyer’s judgment is freed from the
The Invisible Hand, Revisitedconfines of their head and gut — abstracted into AI that acts
continuously, autonomously, and at a scale no human could manage —
the potential is immense.
The marketplace doesn’t disappear. It just goes dark.
Thanks for reading The Verticalist!
Euclid is an inception-stage VC built for Vertical AI founders. If anyone in your
network is considering building in Vertical AI, we’d love to help. Just drop us a
line via the comments below or on LinkedIn.
