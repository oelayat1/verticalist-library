# Vertical AI's Integration Problem

Published: 2025-05-22
Type: essay
Summary: Surveys five responses to closed incumbent systems: integration kludges, partnerships, customer segmentation, wedge selection, and emerging AI infrastructure.
Original PDF: 2025-05-22-vertical-ais-integration-problem.pdf

## Essay text

Vertical AI's Integration Problem
And the 5 Ways Founders Are Solving It Today
MAY 22, 2025
Today’s post is a collaboration with Luke Sophinos. He writes one of our favorite Substacks, Linear: A
Vertical Software Newsletter, and is an Operating Partner at Atomic.
Join the discussion on LinkedIn!
There are over a thousand industries documented by the Department of Labor. Car Dealerships,
Law Firms, Doctors’ Offices, Fuel Dealers, Jewelry Stores… the list is massive. For every one of
those industries, there is a host of vertical software applications that serve them.
The major industry-specific software player in nearly every vertical is almost always the system
of record (SOR)—the business management system or ERP. In other words, the place every
owner or employee is supposed to go to log every single interaction happening within that
particular business.
One of the biggest headwinds to Vertical Software achieving significant scale is the fact that, in
a ton of industries, the business management system has shut off integrations. They don’t allow
third-party tools (i.e., start-ups or new kids on the block) to access this data. Or, if they do, they
only allow third-party vendors to selectively access a subset of their broader data set.
For instance, Epic Systems (the 800-pound gorilla of hospital records) is notorious for high
integration fees and complex, unique deployments for each customer. Likewise, entrenched
software like Yardi in real estate or Dentrix in dentistry hold critical data but weren’t built to
easily share it.
These monopolistic vertical platforms “throw their weight around” to maintain leverage or
extract integration tolls. Sometimes, intentions may not be competitively malicious but the
demand just hasn’t been there to build an open-data ecosystem like a Salesforce or Toast.
It’s a great strategy for a big legacy software provider. They’ve built the integral platform of their
space, and they know how incredibly painful it is for their customers to leave. So while their
NPS probably goes down over time as customers feel this frustration—and they are unable toadopt new technology that they believe will improve their business—most of them just stay on
their sh*tty, old-school system.
A few weeks ago, I (Nic) hosted a Roundtable focused on key challenges for early-stage Vertical
AI companies (we wrote more about it here). Attendees included founders from a wide range of
verticals, including healthcare, supply chain, retail, construction, and insurance. And one
problem in particular stood out. One founder shared his dilemma: "There are certain customers
who say, 'Hey, this is amazing, but if it doesn't integrate with our core system, we just can’t use
it.'"
Again, however, the incentive or ability for incumbents to facilitate the sort of connectivity a
Vertical AI company needs is often just not there. A few other founders chimed in: “A lot of
these legacy [providers] are not tech forward and don't have open APIs. Many don't want to
integrate our product for competitive reasons, and more just don't have the engineering teams
to even build open APIs.” Moreover, their skepticism around open data has, in some cases, bled
down into the buyer universe. “CIOs and execs will not let you have access to their systems of
record,” another CEO reflected. “It's just like a no-go for them.”
While integration challenges have plagued software since the earliest enterprise systems, it’s
becoming an especially acute problem for Vertical AI. Luckily, AI also offers some novel
potential solutions.
There are a lot of creative strategies vertical SaaS founders have deployed to get around this. The
most common strategy is building a wedge product, achieving that “selective” data integration
element with the source of record, then expanding into a few more modules, before swallowing
the frog and offering your own management system / ERP. This works, it’s just typically a ten
year plus journey. I (Luke) ran this exact play in Trade Schools and it took 11+ years to make it
happen.
A second way to get around this is building data extraction products that go into these systems
and pull out the data so that customers can move away easier. The big legacy companies don’t
like this, typically sue, but we’ve also seen this work. Especially when systems operate on
The Vertical Software Integration Problem
Solutions for Vertical AI Founderssomething like EDI where file exchange is normalized. Where legacy systems explicitly don’t
provide APIs or exchanges, this may be a bit of a cautious / scary strategy… but it can work.
The third and final way I’ve seen folks make this work, is by building a janky integration like a
timed file drop. These can leverage import / export functionality from an existing ERP system.
As one founder from the roundtable put it, “We reverse-engineered [it]...there were no API
integrations. [So we] crawl into a Windows machine and inject things into a database.” This
works, but typically is only acceptable by small to medium sized customers. Medium to large
companies won’t accept the security risk or the lack of real-time data. Which leads to what’s
probably the most common solution right now: simply trading flat files.
Now this is how things have been the last decade or so, but Vertical AI is a really exciting
opportunity because if the Vertical AI app can actually replace a full time employee, Vertical AI
tools can charge slightly less than that particular salary, and in many verticals actually end up
being more costly than the industries management system.
But in most cases the Vertical AI employee still has to interact with the business management
system / ERP. And in some ways, the need for data will be even greater in the AI era than it was
for the first few waves of SaaS. In many vertical workflows, some of the most important data
doesn’t exist in any system of record. It lives in email threads, paper files, phone calls, or simply
employees’ heads—pure tribal knowledge.
Vertical AI often aims at precisely these unstructured processes—one reason it holds so much
promise—but that means integration in the traditional sense doesn’t capture everything. A legal
AI solution might need to read contract comments exchanged over email or analyze negotiation
behaviors, none of which reside in an official Case or Practice Management System like Clio. A
construction AI solution might glean insights from foremen’s daily logbooks or on-site
photographs. These rich data sources fall outside typical SaaS integrations. As a result, Vertical
AI developers must broaden their notion of “integration” and get creative beyond the standard
SaaS API.
So how do we overcome this challenge? Here are a few ideas…We’re seeing a lot of founders with SOR-adjacent Vertical AI wedges get log-in credentials from
the customer. “AI employees” are then able to execute work in the ERP directly, reading and
writing data in the background.
This is an amazing workaround, but it’s messy and definitely a legal gray area. A recent court
case brought this question to the fore. Last year, Real Time Medical Systems (RTMS, a provider
of analytics to nursing facilities) sued EHR PointClickCare for using tactics like CAPTCHAs and
account restrictions to block its automated access to patient data, despite customers authorizing
that access. In March, the court ruled in favor of RTMS, stating PointClickCare’s actions likely
violated open EHR legislation and constituted unfair competition. The decision hopefully sets a
precedent for software openness—but healthcare also has special protections in this regard (via
the 21st Century Cures Act and other laws) that other verticals may not.
And there are legitimate concerns with every Vertical AI company trying to kludge its own
workarounds. Compliance weighs heavily given regulations like HIPAA and GDPR. But a poorly
orchestrated ecosystem could also be vulnerable to prompt injection attacks or the exposure of
sensitive credentials. Both OpenAI and Anthropic are actively working on defenses in this
Option #1: Kludgeregard (e.g., Anthropic’s content classifier during computer vision steps). So long-term prospects
for this AI workaround across verticals remain quite unclear.
Be the AI partner to the legacy software provider / ERP. If you can actually go and partner with
the legacy company (who probably thinks AI is a trend and just helps them figure out how to
cook dinner), and build out a whole host of Vertical AI employees while leveraging their data
set. If you do this, you can probably become bigger in scale than the management system. Why?
Because your product gets compared to an employee’s salary versus a typical per seat SaaS
contract.
I don’t think enough folks are actually trying this, despite the fact that many legacy companies
would rather take a 10% commission from you than to go build it out on their own. This
statement is obviously very industry dependent but my experience is so many of these shops are
running 10-15 years behind.
This creates some down-stream risk as they wake up but you can probably build your own ERP
by the time that happens. I think you could do it much faster than Option #1 as well.
Go SMB. The business management system / ERP is far less sticky with smaller customers. They
typically are much more modern / open systems with API’s, because they don’t have the lock-in
power the ERPs have with mid-market and enterprise businesses. You can likely leverage their
data any which way you want here. Just make sure the SMB segment in a particular industry is
big enough for you to build the size of business you’re aiming for. You also have to build an
incredible product that delivers on its promise because competition here is typically pretty
ruthless.
Focus on offering Vertical AI that doesn’t need to interact with the ERP / System of Record.
There are plenty of opportunities and industries where you can provide a ton of value and build
a big business without needing to touch it. Think AI Sales Agents trained on everything in a
particular industry. AI Customer Support Reps for a particular industry. The list goes on. You
Option #2: Partnership
Option #3: Segmentation
Option #4: Wedge Selectioncan even charge by performance (IE leads delivered, tickets closed, etc.). If the performance is
good enough they will gladly key this info in to their management system.
Bet on the AI data infrastructure ecosystem to help alleviate this problem in the near-term.
There are two developments we see as particularly promising here.
First is the rise of standardized agentic communication frameworks. Last year, Anthropic
announced the Model Context Protocol (MCP)
1
, an open standard designed to solve the
combinatorial explosion of AI-to-tool integrations. MCP enables AI systems to dynamically
fetch external data and execute tools in a standardized, model-agnostic way: a “USB-C port for
AI applications.” Built on a client-host-server architecture, MCP lets AI applications (clients)
access resources hosted by external services (servers) via a coordinated environment (host). For
Vertical AI founders, frameworks like MCP may offer a way to decouple integration logic from
their core product and reduce reliance on brittle, one-off connectors.
Second, Vertical AI may have options that are less reliant on behavior change of legacy systems
or even users themselves. The emerging concept of AI-driven “computer use” extends
traditional RPA (which can already click buttons in a scripted way) by adding flexibility and
understanding. An AI agent can interpret new situations or adapt to slight changes in the
interface that would break a rigid script. OpenAI recently released, for example, ChatGPT
“Operator.” It uses a new Computer-Using Agent (CUA) model that combines GPT-4’s vision
(image understanding) with reinforcement learning for advanced operation of a cloud-based
browser on the user’s behalf. They could, for example, instruct Operator to “find and book a
reservation next week at the highest-rated Italian food restaurant that has outdoor seating.”
You can see how a more powerful enterprise version would be valuable for Vertical AI startups.
And of course, many startups—like Adept, with >$400M raised—are targeting such B2B use
cases directly. Computer Use is fairly nascent and not ready for prime-time but we expect that to
change fast.
So that’s our quick riff on the problem statement. It’s not perfect, and it’s ever changing, but
these are a few ways to attack the challenge.
Option #5: AI Infra
ConclusionNow, we’d love to hear from you all:
What are other creative ways to solve the integration problem with Vertical AI?
What have you seen work that we have not listed above?
Reply directly here or jump into the comments!
Thanks for reading Euclid Insights! Additional sources here.
2
If you know a founder thinking through Vertical AI product challenges, we’d love to be a sounding
board. Just reach out via LinkedIn, email, or here on Substack.
1 If you’d like to get up to speed on MCP, we’d suggest the three long reads in the sources below. All
well-thought-out primers with examples.
2 US CFPB (2024). CFPB proposes rule to jumpstart competition and accelerate shift to open banking.
Consumer Financial Protection Bureau.
Headstorm (2020). Modern Moves in Logistics: From EDI to API. Headstorm.
Koul (2025). The Model Context Protocol (MCP): A Complete Tutorial. Medium.
Kuttner (2024). An Epic Dystopia. The American Prospect.
Mekala (2025). Missing Piece of the Puzzle: MCP with LLMs. Medium.
Mindbowser (2025). Model Context Protocol: How It is Changing Healthcare Chatbots.
Mindbowser.
Pai (2025). Model Context Protocol and Why It Matters for AI Agents. Medium.
