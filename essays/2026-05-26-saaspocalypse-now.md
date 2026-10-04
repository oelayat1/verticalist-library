# SaaSpocalypse Now

Published: 2026-05-26
Type: essay
Summary: Tests five common explanations for the software selloff against public-company data and examines what AI exposure and pricing models imply for Vertical AI founders.
Original PDF: 2026-05-26 - SaaSpocalypse Now.pdf

## Essay text

SaaSpocalypse Now
Five myths about the software selloff — and what they mean
for Vertical AI
MAY 26, 2026
Public SaaS stocks just went through a brutal repricing, with the median
price down 32%. Median EV/Revenue tanked from 9.1x to 4.8x — a 42%
contraction, during which 86% of companies saw their multiples
compress. At minimum, this should tell us something about how the
potential of AI is interpreted by the wider market — we’re interested in
it as a foil for thinking about the future landscape of application layer
software.
Public market performance, of course, is an imperfect teacher for
founders and VCs. After all, public SaaS downturns can have both bad
(the application layer is dying) and good (the next generation is taking over
fast) implications for startups. Especially in moments of uncertainty,
markets can be sentiment-driven — a Buffett voting machine that’s at
best distracting to those concerned with 10-20-year cycles.
Yet certain conclusions have been popularized in the wake of the
“SaaSpocalypse” that, absorbed without proper context, lead to the
wrong vision for the future of the software. This essay is our attempt to
make sense of the lessons we can draw from public SaaS movements
over the preceding months: dispelling some that unfairly discount the
potential for AI-native software, and highlighting others we think are
portents for the future of the Vertical AI landscape.
1. Vertical Software Has Stopped GrowingTom Tunguz’s article from a few months back was a great, concise
summary of the recent public market movements. Ultimately, it laid the
blame for poor vertical SaaS performance on fundamentals. Despite
ostensible value in their moats, he said, they were repriced more
aggressively because they are slowing down:
Vertical software companies like Veeva, AppFolio, & Procore
possess genuine moats: regulatory barriers, deep integrations
that make their products operating systems for entire
industries, years of accumulated domain data that is
particularly relevant for AI. If anything, these companies should
be harder to displace than generic workflow tools. Yet vertical
software trades at the steepest discount. Because they simply
aren’t growing that fast.
— Tom Tunguz, How Markets Price AI Risk
You wouldn’t have to indict vertical SaaS as a business model to believe
that story. On average, public vertical SaaS companies are nearly 10
years older than horizontal peers. A thick cohort of legacy, pre-internet
vertical players — Dye & Durham (1874), FICO (1956), Agilysys (1963),
Tyler (1966) — pulls the 75th percentile vertical age to 42 years old
versus 27 for horizontals, which might explain slower growth across the
bucket.
There’s just one small problem with the “slower growers” explanation:
it’s not true. Our review of 130 public SaaS stocks yielded effectively no
difference between median LTM growth: horizontals grew 14.7%,
verticals 14.1%. Across our SaaS comp set, fundamentals had almost no
correlation with price performance. Revenue growth correlated with
returns at r = 0.07; EBITDA margins at -0.03. Within Vertical SaaS, thebottom 15 performers had higher median margins and higher median
growth than the top 15.
In his piece, Tom also summed up the popular view well: “Vertical
software has fallen 43% this year. DevTools, just 21%. The gap between
them… tells you what markets actually believe about AI.” While facially
accurate, this takeaway misses a few things.
It implies that the market concluded that vertical software itself — by
nature of being industry-specific — was vulnerable to AI. Many have run
with that conclusion, surmising that vertical SaaS is easier to replicate
with LLMs.
2. Vertical Software is Less AI-MoatedThose conclusions fly in the face of two realities, however:
1. The performance differential had more to do with a handful of
horizontal SaaS companies that were “graded” by the market as
being not just defensible but poised to benefit from the rise of AI.
The following tickers got the “AI picks-and-shovels” treatment,
appreciating by >50%: Bandwidth (telecom APIs), Datadog
(observability), MongoDB (database), Twilio (comms APIs), Fastly
and Akamai (CDN), JFrog (software supply chain), and Innodata
(AI training data).
2. Vertical SaaS still trades at a premium to horizontal peers, even
accounting for fundamentals. The recent repricing reflects a
significant rethinking of that “narrative premium.” In other words,
vertical software traded much higher to begin with, so this is
perhaps just a case of the bigger they are, the harder they fall. From
our perspective, this largely reflects a devaluing of moats that are
not immediately visible in the P&L (more on this to come).
None of this suggests that Vertical SaaS is less defensible from AI. It
suggests that perhaps the traditional valuation bonuses they fetched
are less rich—and that only the most legible, near-term AI tailwinds are
being rewarded (more on that below).Thanks for reading The Verticalist! Subscribe
to receive our weekly analysis on Vertical AI,
from the investment team at Euclid.
Subscribed
Looking across the whole data set, consumption-based access &
pricing models were the clearest driver of software performance over
the last several months. We came to this conclusion by blind-scoring all
130 software stocks on the six most important a priori considerations¹.
Strong correlations should suggest how the market is “grading” AI
3. The Market Has Correctly Repriced Terminal
Valueexposure. Whether a company’s existing product and monetization will
thrive in a world where agents are doing more and more work is a very
reasonable measure of immediate AI benefit. It’s telling, however, that
less tangible moats — workflow depth, proprietary data, regulatory &
domain complexity — were not rewarded.
We can even simplify the moat that mattered to one question: Are you
agentic infrastructure?
Let’s put that question to the test by comparing Bandwidth (a
horizontal that appreciated 280% despite an R40² of 6) and Doximity (a
vertical that drew down 65%). If you aren’t familiar with Bandwidth,
they’re a Twilio competitor — a CPaaS (Communications Platform as a
Service) that sells APIs for voice and SMS used by RingCentral, Zoom,
etc. In an AI world, every voice agent that makes a phone call using
BAND generates usage-based revenue. As Tom put it, “the data
infrastructure tailwind is structural. More AI means more queries, more
embeddings, more vector operations.” It’s less immediately clear how
Doximity — LinkedIn for physicians, more or less — will benefit fromagentic work under the current business model. After all, pharma and
hospitals pay subscriptions to market to Doximity’s audience.
Much is lost in this simplistic view of AI moats, however. Doximity, for
example, has strong network effects, with 80%+ of doctors on the
platform and many hospitals requiring them to sign up. They have data
gravity, aggregating proprietary clinical datasets (e.g., PeerCheck,
Pathway Medical), which have immediate value to current customers.
They have a relatively AI-ready talent, with a 380-person R&D team
already layering AI tools (Scribe, DoxGPT) to drive new revenue from
health systems. They have workflow loops that deeply integrate with
telehealth, faxing, and clinical documentation. And finally, they arguably
have regulatory moats from operating all this in a HIPAA-regulated
environment.
It’s further evidence that the SaaSpocalypse offered reprieve only to
those with immediate revenue opportunity — the potential to benefit
from AI in any manner more complicated than picks-and-shovels tomorrow
was flatly ignored. Not exactly a deep consideration of terminal value,
as one might expect from public markets mostly concerned with next
quarter’s earnings.
As Ben Thompson observed in his Stratechery interview: “the
destruction and the value creation are not simultaneous in time.” Public
markets are pricing the destruction phase. They are pricing the obvious
acceleration. They have ignored the longer-term value creation.When we classify the 57 public vertical SaaS players in our dataset by
source of defensibility — using the moat taxonomy from Dude, Where’s
My Moat? — three groups fall out.
1. Proprietary data moats. Verisk, FICO, Cadence, Veeva, CCC (20
total). These sit on data that cannot be reconstructed or easily
replicated. A year ago, they traded at 220% above what a
horizontal with the same growth and margins would command.
Today: 72%. 18 of 20 are still trading above their horizontal
equivalents.
2. Regulatory barriers without compounding data. Tyler
Technologies, ADP, Constellation, nCino, Q2 (16 total). Legal and
procedural barriers to entry, rather than data-driven ones. Their
premium went from 120% to 15%.
4. All Vertical Moats Are Eroding Equally3. The vertical halo. ServiceTitan, Par Technology, Toast, Lightspeed,
MNTN (15 total). They traded at a 41% premium a year ago on the
vertical SaaS narrative — own the vertical, high NRR, extensibility.
Today, they trade at a 40% discount to the horizontal equivalent.
Clear and present vertical data moats are still rewarded in the market
with elevated multiples (even after accounting for fundamentals). Along
with pretty much everything outside of immediate AI revenue tailwinds,
however, the recent repricing assigned zero value to even the strongest
cases of data gravity.In an essay three months ago, we shared a simple litmus test on the
defensibility of Vertical SaaS: Is the data proprietary? Is there regulatory
lock-in? Is the software embedded in the transaction? Two or three yeses
and you’re probably fine. The market’s repricing roughly tracks this —
proprietary data moats still command a 72% premium. But it’s assigning
nearly zero credit for the second and third.
The market is pricing the impacts of widespread AI adoption in our
economy, including both the decreased cost of software development
and the resulting absorption of work by agents. It isn’t yet pricing in the
rise of a new generation of AI-native software. Accordingly, pipes that
serve AI, generating near-term revenue uplift, get insulated — while
software across the board sees erosion, with staying power in question.
It certainly isn’t pricing to an application-layer AI steady state, in which
data and workflows will be more valuable than ever.
5. The Application Layer Is DyingAs we shared in our initial essay on the SaaSpocalypse earlier this year,
we are still quite early in the destruction phase, despite the market
panic.
Some vertical software companies will die, though we think the durability of
those names is far higher than that of their horizontal peers. Some of the
next generation of vertical AI companies will be built on the rubble, but
most of them will be built on green fields. The market, by definition, cannot
expand if it’s just ripping and replacing legacy vendors.
— The Verticalist
LLMs have demonstrated the value of scaling for training data and the
ability of agents to become more capable through reinforcement
learning. To expand beyond language-centric use cases, however, AI willneed domain-specific data and decision context. It exists nowhere on
the public internet, isn’t for sale, and in many cases, it lives only in the
minds of professionals. Vertical platforms have always been best
positioned to capture this data. Only now is it becoming so valuable —
even if the market hasn’t yet priced it in.
The bears assume AI will shrink the market for vertical software. They're
wrong — it will dramatically expand it. AI needs domain-specific data
and decision context to move beyond language-centric use cases, and
that data exists nowhere on the public internet. It lives in the workflows,
transactions, and institutional knowledge that vertical platforms are
uniquely positioned to capture. Some incumbents with strong moats
and the willingness to cannibalize their own products in favor of an AI
angle will thrive. But the biggest winners will be a new generation of AInative companies — built not just on the rubble of legacy software, but
also on greenfield use cases, budgets, and verticals the public market
hasn’t even begun to consider.
1 Proprietary Data Flywheel measures whether the company accumulates
irreplaceable, compounding data through its product — the kind of dataset a
foundation model or new entrant couldn’t reconstruct in 12 months. Verisk’s
decades of actuarial claims history scores a 5. Dropbox’s file storage, where
the data belongs to the customer, scores a 1.
Pricing Alignment captures whether the revenue model benefits or suffers
when AI agents generate more activity. Consumption and usage-based models
where more API calls mean more revenue — Bandwidth, MongoDB, and
Datadog score highest. Seat-based models where AI reduces the number of
humans who need licenses — Asana, Monday.com, Workday — score lowest.
Workflow Replaceability asks how deeply embedded the product is in the
customer’s operations, scored inversely — a 5 means the product is nearly
impossible to rip out. Oracle’s ERP and ADP’s payroll infrastructure score 5.
Dropbox and Amplitude, which could be swapped in a week, score 1.AI Credibility assesses whether the company has the engineering team, R&D
investment, and leadership DNA to build real AI capabilities — not just bolt on a
chatbot. We looked at R&D as a percentage of revenue, the CEO's
background, AI acquisitions, and named AI products with measurable
adoption. Palantir and Datadog score 5. Tyler Technologies and Constellation
Software score 2.
Domain Complexity measures how regulated, specialized, or expertdependent the customer environment is. Deep regulatory barriers that take
years to satisfy — FDA clinical trial submissions at Veeva, CJIS certification at
Tyler, credit scoring regulation at FICO — score 5. Horizontal markets with no
such barriers score 1.
Agent Ecosystem asks the forward-looking question: in a world where AI
agents orchestrate enterprise workflows, does this product get more or less
usage? Products that agents can route through — databases, communication
APIs, security layers, observability platforms — score 5. Products that are
human coordination layers agents are unlikely to use — task trackers,
dashboards, file storage — score 1.
2 Rule of 40 Score: Revenue Growth + EBITDA Margin.
