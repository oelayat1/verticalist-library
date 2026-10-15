# Service-Level Disagreement

Published: 2026-04-16
Type: essay
Summary: Distinguishes services-as-a-wedge from services-as-delivery, examining automation, liability, TAM, and why durable AI businesses still need workflow ownership and software moats.
Source URL: https://insights.euclid.vc/p/service-level-disagreement-ai-services-versus-software

## Essay text

The VC debate on AI Services — and why they won't escape the gravity of software

Recent pieces from [Emergence](https://www.emcap.com/thoughts/the-ai-native-services-playbook), [Sequoia](https://sequoiacap.com/article/services-the-new-software/), and others have touched on the growing trend of AI-native services (AINS). The central insight is that AI companies should sell the *work*, not just the *tool,* enabling startups to capture and unlock hard-to-access budgets. In other words, sell the outcome, not the software. Outsourced work is more easily replaced than insourced work, and the TAM is much larger: every software dollar equals six in services.[1](https://insights.euclid.vc/p/service-level-disagreement-ai-services-versus-software#footnote-1)

While we agree there are many appealing features of the model, we are likely more cautious than our peers regarding the scope (which markets this applies to), the addressable market (how large a business you can realistically build), and venture fundability (the proportion of AINS startups that are a good fit for venture capital). In fact, we have been sharing our concerns with the growing enthusiasm for services for almost two years. From our piece in November 2024, *[The Siren Song of Services](https://insights.euclid.vc/p/the-siren-song-of-services)*:

> *As with any venture thesis in vogue, however, an antithesis is looming. Today, we are seeing a broad embrace of startups tackling services, many without clear paths to automation or without a natural venture-scale second act. Some bet that AI will catch up, and margins with it. Others trade away the software business model wholesale in exchange for TAM, taking vertical integration to its extreme. Far too many are forgetting why software is such a hallowed category of investment, making all-too-liberal assumptions around the ease of automating humans out of an industry, the down-market valuation of services revenue, or the right to grow a product suite horizontally. — The Verticalist*

---

## The Case for AI Services

The pitch for AI-enabled services is rational. The logic is inextricably tied to the changes LLMs have enabled, generally running as follows:

- Due to various factors — including the rapidly increasing number of SaaS tools and incentives against innovation in some industries — the traditional angle of attack (selling and monetizing cloud software) has stalled.
- To expand their reach, startups need to shift from SaaS to services, focusing on the rapid improvements in LLMs to deliver outcomes rather than just tools and, in some cases, completely taking over the operating businesses they previously considered customers.
- By including labor budgets in scope alongside traditional IT budgets, TAMs for AI Services startups are massively expanded. Moreover, in markets with labor supply constraints, AINS are particularly compelling because they can deliver immediate revenue acceleration by removing the bottleneck.[2](https://insights.euclid.vc/p/service-level-disagreement-ai-services-versus-software#footnote-2)
- With the potential of LLMs and agentic platforms to boost automation and increase gross margins in traditionally manual workflows, AI Services are now venture-backable, venture-scalable, and have software-like terminal margin potential.

A common feature of such arguments is the tendency to treat all AI-native service models as the same. In practice, we see two distinct models emerging. They are two fundamentally different strategies, with different prospects for all downstream considerations that matter: go-to-market, margin structure, hiring, and defensibility.

[![Figure from the published essay](https://substackcdn.com/image/fetch/$s_!mJml!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfdc2256-11ac-4972-901f-6a24e4ecea8a_666x375.png)](https://substackcdn.com/image/fetch/$s_!mJml!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfdc2256-11ac-4972-901f-6a24e4ecea8a_666x375.png)

1. **Services-as-a-Wedge**

Here, you enter a market by taking on work outcomes like NDAs or insurance brokering. Often, these are already outsourced to consultants or BPOs, for example. Services are the initial beachhead; you use them to build trust and gather data, then gradually automate more with software (internal or external) to control the workflow and tap into insourced TAM. Over time — if the hypothesis is correct and the AI-powered workflow improves sufficiently — the need for the human service layer recedes. This is what people generally mean by an “AI Services startup” — or at least, it was until recently.
2. **Services-as-Delivery-Engine**
The second archetype contemplates a very different business model. Workflow software is developed, but software alone cannot deliver the complete customer outcome. Human service remains essential at the last mile: filing with regulators, interfacing with high-value customers, approving items requiring certified experts, etc. In this model, the service component is a permanent delivery mechanism, not just an entry point. As AI advances, the service becomes more efficient, but the underlying need for human judgment in the loop remains.

These two approaches are likely to yield fundamentally different business models. It’s not just that they have different leverage points around human-in-the-loop and ultimately margins. It’s also that they are built to serve two different types of products, which in turn are often built to serve two different types of markets. A fund administrator or financial auditor, for example, is a very different type of services firm than an insurance or freight broker. Let us explain.

Services-as-a-Wedge relies on “intelligence arbitrage.” Its fundamental bet is rapid AI improvement, allowing what was once a low-margin service to become a software-like business with a low marginal cost of growth. In contrast, Services-as-Delivery-Engine leverages “coordination advantage,” where advances in the AI model drive a product superior to the status quo, even if the margin profile never looks SaaS-like. The former transitions quickly into additional services before it becomes commoditized, while the latter strengthens its advantage through automating exception handling and coordination.

### Comparing the two models

[![Figure from the published essay](https://substackcdn.com/image/fetch/$s_!c6t-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e1f854d-a396-4970-8601-bd7056e4bbdb_668x375.png)](https://substackcdn.com/image/fetch/$s_!c6t-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e1f854d-a396-4970-8601-bd7056e4bbdb_668x375.png)

Automation Trap = humans turn out to be hard to automate away, margin expansion never materializes. [Dispatcher Trap](https://insights.euclid.vc/p/who-gets-to-eat) = risk of commoditization (competitors and legacy services have the same LLMs you do).

The wedge approach is effective in categories where work is already outsourced, tasks are intelligence-based and can be automated, and buyers are comfortable with external providers. Here, substitution involves changing vendors rather than reorganizing internal processes.

- **Insurance brokerage** exemplifies this model. Standard commercial lines brokerage involves comparing carriers and completing forms, which is primarily intelligence work. The distribution layer is highly fragmented among many small brokers, so no single incumbent controls customer relationships. [Harper](https://www.harperinsure.com/) and [Panta](https://pantainsure.com/) are recent examples of this model.
- **Transactional legal work** fits the same pattern. NDAs, regulatory filings, standard contract drafting — well-defined tasks with standardized outputs that most companies already outsource to outside counsel. [Crosby](https://crosby.ai/) and [Arcline](https://www.arcline-ai.com/) enter as the autopilot, replacing counsel on the straightforward stuff.

In delivery models, the primary challenge is not intelligence work but coordination, compliance, liability ownership, and the physical-world handoff between the software-powered output and the customer’s desired outcome. The service provider is effectively an embedded partner and owns the outcome. Owning the outcome means the last mile is structurally lengthy, at least today. The work is typically outsourced, but can also be insourced.

- **Communication compliance** is a strong example of the delivery engine model. Firms in regulated industries, including financial services, healthcare, and government contracting, must monitor, archive, and report employee communications. [Hadrius](https://www.hadrius.com/) and [Norm AI](https://www.hadrius.com/) are addressing this need in financial services. While the intelligence work can be automated, achieving the desired outcome requires ongoing regulatory filings, audit readiness, and liability for missed violations.
- **Fund administration** is another strong example. Running NAV calculations is intelligent work that the model can handle. But the outcome the GP is paying for is auditable books, trusted LP reporting, and a system of record that holds the fund’s entire operational history. The promise of AI-native fund administration is an ERP-like stickiness with a service-layer last-mile. But no matter how good the ERP is, the coordination, regulatory compliance, and judgment layers are critical to the business's success. [Hanover Park](https://www.hanoverpark.com/), [Maybern](https://www.maybern.com/), and [Formulary](https://www.formulary.co/) are recent startups to emerge in this category.

In delivery models, the primary challenge is not intelligence work but coordination, compliance, liability ownership, and the physical-world handoff between the software-powered output and the customer’s desired outcome. The service provider is effectively an embedded partner and owns the outcome. Owning the outcome means the last mile is structurally lengthy, at least today. The work is typically outsourced, but can also be insourced.

### The Diagnostic: Three Questions

We suggest that founders aiming to build an AI-services business should answer three questions to define which model to pursue:

**1. Are you an external vendor or an embedded partner?**

If service is your entry point, you are entering the market by performing outsourced work, replacing another vendor, and following the wedge strategy. Your priority should be to progress toward workflow ownership before the intelligence layer becomes commoditized. If service is your delivery mechanism, providing last-mile coordination as an embedded partner adds value to the software; your focus should be on deepening the surface area of this capability while pursuing automation.

**2. Who owns the outcome?**

In the wedge model, the customer typically retains liability; you’re doing the work, but they’re responsible for the output. The executor of the NDA is liable. The customer still signs off on the insurance policy. In the delivery-layer model, *you* own the liability, even if it’s implicit. The human judgment layer is not going away when filing the tax return. Administering the fund and closing the books with your name on the audit trail. Liability ownership sounds like risk (as it should be!), but it’s actually leverage when executed correctly to build a durable moat. It converts cost-center pricing into insurance pricing and creates switching costs that no feature comparison can replicate.

**3. What happens to your business when the model gets 10x better?**

For wedge companies, a better model makes your entry point easier, but also makes everyone else’s entry point easier. The advantage is temporary unless you’ve compounded data and trust into internal workflow ownership. For delivery-layer companies, a better model makes your service layer cheaper and faster to deliver, but the coordination and compliance requirements don’t go away. Your margins should improve. Your moat gets wider. If a 10x better model helps your competitors as much as it helps you, you’re in the wedge. If it disproportionately helps you because you’ve built the coordination infrastructure to exploit it, you’re in the service layer.

The worst position is misdiagnosing which model you’re in. A wedge company that thinks it has a service-layer moat will get commoditized while congratulating itself on its service quality. A service-layer company that tries to shed its coordination layer to look like a pure software business will gut the very thing that makes it defensible.

---

## The Challenges with Services

#### The Allure of Trading Margins for Revenue

It’s easy to see why services present such an alluring target. Large prospective markets are up for grabs within the arbitrage window as intelligence capabilities accelerate. The first pillar of that argument is that selling the work, not the tool, can be the right approach to wedge into software-shy buyers — opening doors where SaaS struggled. Replacing an existing vendor is a simpler buyer consideration than training on a new software platform. There’s simply less organizational change required, which can be substantial in industries where something has been done one way for decades. The second pillar of that argument is the fact that, as the Sequoia piece put it, “For every dollar spent on software, six are spent on services.” Hypothetically, 100% of the TAM is up for grabs, rather than just the IT budget (more on this later).

As we wrote in [our piece on the dispatch problem earlier this year](https://insights.euclid.vc/p/who-gets-to-eat), while we are generally bullish on AI services, we do not believe services are the right path for every vertical market, nor will they be the most dominant approach overall:

> *Some believe that as the marginal cost of intelligence collapses toward zero, the key value proposition of enterprise technology will shift from providing tools that assist human labor to delivering outcomes that replace it. We believe this is certainly true: Vertical AI can handle more end-to-end workflows than Vertical SaaS alone. This warrants significantly more customer value and willingness to pay, tapping into significantly larger budgets. We disagree, however, with the now-prevalent view that service delivery — a customer relationship that mirrors an external vendor rather than an internal platform integral to the business — is the prevailing paradigm of AI-powered software.
> — The Verticalist*

The most glaring question for us is that the trade-off between revenue (and, at a higher abstraction, addressable market size) and margins is not as clear-cut a bet as it might seem. We think Emergence’s concept of “Mirage PMF” nicely encapsulates several of our concerns here, namely that “strong revenue growth and net dollar retention can mask a lack of true AI enablement.” Historically, many tech-enabled service businesses have stormed out of the gate with traction (and even strong retention), trading margins for revenue growth, only to have unit economics and cash burn be their undoing at scale. The rise and fall of several well-funded freight brokers and real estate iBuyers are great examples of this phenomenon.

Of course, the key now is that, with AI, this time it’s different. In our past essay on the [AI-First Roll-Up](https://insights.euclid.vc/p/the-ai-first-roll-up), we addressed this specific point:

> *[It] remains unclear what the margin lift from AI will be—and opportunity across industries is unlikely to be universal… [Service-as-Software companies are] selling an outcome and internalizing the margin risk. I.e., they are making a bet that they can automate manual an increasing share of work over time. These have been famous last words for many startups whose margin uplift materialized too slowly because it was (i) too hard technically, or (ii) too hard to escape reliance on services once addicted to the high growth rates their venture backers demanded. — The Verticalist*

The last point is a unique and difficult challenge for tech-enabled services and can often be highly destructive to enterprise value. Managing the trade-off between growth and per-unit delivery costs presents idiosyncratic challenges for a venture-backed startup: investors paying software multiples will expect venture-like growth with software-like margins. For the operators, that means rapidly growing top line while simultaneously improving gross margins and reducing per-unit costs. There reaches a point of maturity where you can no longer trade margin for revenue, and the market is unlikely to reward those who trade margin over revenue.

The startup needs to invest in growth (sales & marketing), automation (R&D), and service delivery (human labor as COGS) simultaneously, carefully pulling the levers to manage the business. Investing incorrectly and having to iterate rapidly and reprioritize is difficult for any startup, but especially for a services firm. In high-trust markets, the cost of failure can be existential. You’re delivering an outcome, not a tool. Understaffing and underdelivering as a services business can damage a brand beyond repair. Overstaffing and failing to grow can make raising that next round even harder; meanwhile, those staffing choices increase burn and shorten the runway.

Even if the startup gets the ramping levels right, staying competitive in a market eager for AI-powered software won't be easy. Over time, the purely economic incentive to develop not just good software but industry-leading software diminishes—after all, your reward isn’t higher revenue growth as it might be with a startup; it’s gross margin improvement. Boring! It’s also not enough to help you raise your next round. No later-stage venture investors will fund a slower growth business just because they’re improving margins. Automation is table stakes, but venture funding won’t follow without venture-like growth *and* a path to software-like margins.

At the same time, not only will your automation likely be replicated by direct AI service competitors (who will aim to undercut your offering on cost & speed), but it will eventually be accessible to the broader market as pure software. The motivation to continue R&D efforts to build best-in-breed technology quickly diminishes.

#### The TAM Illusion

The largest challenge we have with the services narrative is around market sizing. Sequoia’s analysis suggests “the total addressable market for autopilots is all labor spend in a category, insourced and outsourced combined.” Of course, such proclamations are not unique. The graphic below is [from a recent Coatue presentation](https://www.coatue.com/c/takes/ai-is-hitting-a-new-inflection-point), suggesting that “by shifting the unit of value from the tool to the results, the addressable market potential expands by 25x.”

[![Figure from the published essay](https://substackcdn.com/image/fetch/$s_!Lff8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1d33fdb-c4e4-4119-95f2-d8c3968f6a07_2648x1170.webp)](https://substackcdn.com/image/fetch/$s_!Lff8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1d33fdb-c4e4-4119-95f2-d8c3968f6a07_2648x1170.webp)

These types of TAM analyses feel overly simplistic. We’ve previously discussed [our view](https://insights.euclid.vc/p/market-sizing-in-vertical-software-425) that VCs struggle with sizing vertical markets, but this kind of analysis, encompassing all labor spend, is not exclusive to vertical markets. As we explained in [our piece on agents in Vertical AI](https://insights.euclid.vc/p/we-need-to-talk-about-agents), automation has not historically led to a one-to-one replacement of labor. Similarly, calculating TAM based on potential labor offsets is not only flawed—it’s fundamentally incorrect and incongruous with every historical example of automation.

Perhaps more importantly, if the intelligence layer continues to improve and become more affordable — as many companies building and investing in AI services believe — the value of the service-level output will become commoditized. In other words, if the cost of task-specific intelligence continues to decrease, the arbitrage window will eventually dissipate as the intelligence layer approaches infrastructure-style pricing (i.e., at margins above roughly the cost of delivering it). Consequently, any traditional labor-based pricing model will fail. Pricing will be driven not by how many people can be replaced and what they cost, but by market competition. Any service layer based on labor pricing will be unsustainable. And yes, while lowering the cost of a service could increase demand (see [Jevons’ Paradox](https://open.substack.com/pub/euclid/p/who-gets-to-eat?utm_campaign=post-expanded-share&utm_medium=web)), this still doesn’t bring you back to the labor-offset TAM.

This also presents the classic dispatcher problem: performing the work without owning the workflow makes you a lower-cost version of the incumbent rather than a fundamentally different business. For example, taxi dispatchers coordinated rides but did not own the fleet, driver relationships, or customer data. When coordination became commoditized, dispatchers lost their advantage. The value accrued to the workflow owners.

If intelligence-as-a-service in a vertical market follows the expected path of commoditization, we can be certain the market will not be the same size as the current services market. It may be much larger in aggregate value creation, but the question is who captures that value — and historically, it has not been the company whose only advantage was doing the work cheaply.

In other words, the vertical AI startups — whether they consider themselves AI services companies or not — that reach early traction by capturing the surplus from collapsing intelligence costs will quickly find themselves underpriced and outcompeted if they don’t build beyond the initial service. The only long-term moat comes from [productization beyond the initial service](https://insights.euclid.vc/p/who-gets-to-eat):

> *The wedge may be a service delivered more cheaply. But the moat will be a system built on top of that wedge, leveraging their internal positioning with customers to develop moats—the proprietary data, the network effects, the multi-product platform, and the industry “brain”—that make it infrastructure to be relied upon, rather than just another vendor.
> — The Verticalist*

The other glaring question regarding potential outcome sizes is market penetration. From [our piece on market sizing](https://insights.euclid.vc/p/market-sizing-in-vertical-software-425) last year, horizontal SaaS companies often slow down around 10-20% market share. Vertical SaaS, especially in less competitive markets, may achieve much higher penetration — sometimes over 80% within focused (albeit often PE-consolidated) markets. Most large public vertical software businesses top out in the mid-teens.

[![Figure from the published essay](https://substackcdn.com/image/fetch/$s_!i9DN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad20c013-0c53-439a-ba76-a9929bb3546d_1632x1010.png)](https://substackcdn.com/image/fetch/$s_!i9DN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad20c013-0c53-439a-ba76-a9929bb3546d_1632x1010.png)

Few operating businesses, and hence fully vertically integrated startups, will ever reach these heights. Despite their incredible growth, none of Headway, Alma, Rula, or Grow Therapy is estimated to have more than low single-digit shares of the total US therapy market. Even after its roll-up of the largest legacy player in the market, the vertically integrated home health business Honor is likely to have 2-4%. The TAM may be enormous, but the path to capturing a meaningful share of it as an integrated services business is structurally harder than selling software licenses. Combined with the deflationary pricing impacts of collapsing intelligence, we feel that many of our peers may be overestimating the size of the revenue opportunity that “labor-replacement” services can truly achieve.

#### Services Aren’t More Defensible Than Software

Sequoia opens its piece by arguing that AI Services are more defensible against the foundation model labs. “If you sell the tool,” Sequoia wrote, “you’re in a race against the model. But if you sell the work, every improvement in the model makes your service faster, cheaper, and harder to compete with.”

It's worth unpacking what they're actually saying. Most SaaS companies resell compute and storage infrastructure; as cloud infrastructure has improved and become more affordable, both they and AWS, among others, have benefited. Naturally, SaaS providers offering no unique value beyond storage and compute were inherently vulnerable and would eventually face disruption and eroding market share. As Ben Evans joked on a recent [podcast interview](https://stratechery.com/), “[SaaS] is all a thin-SQL wrapper. They’re all just databases.”

The same paradigm applies to solutions built on top of LLM infrastructure. Every improvement to the model benefits both tools and services equally. Sequoia’s framing assumes LLMs improve in ways that commoditize the tool but somehow spare the service. That’s arbitrary. If the model gets good enough to replace a code-review tool, it’s good enough to replace a code-review-as-a-service offering (and arguably, the latter is easier). What’s simpler: switching IT help desks or an accounting firm, or swapping out your ERP? Model improvements only make a service defensible to the extent that no competing service adopts the same LLM advances. That’s not a bet we’d take.

So why would selling the tool put you “in a race” against the model any more than selling the work does? The strongest moats in software have always been those that are not easily replicated — proprietary data loops, workflow integration, distribution, network effects — not the infrastructure they’re built on, regardless of whether you charge for the tool or the output. The threat vector is the same for both tools and services: competitors (whether peers or the labs themselves) could leverage LLMs to commoditize your offering. Whether you’re wrapping the model as a tool or using it to deliver completed work, you need to build a business that will survive and thrive as your infrastructure improves.

---

## **The Wedge is not the Moat**

Our overall point is *not* that AI Services built on LLM infrastructures are inherently a bad initial wedge (or business model). Rather, we remain convinced that these startups must go beyond the wedge to build internal customer workflows and, in some cases, commoditize their own services to avoid the eventual disruption. For those building in the service-as-delivery startups, these businesses can be highly attractive, although it remains to be seen how many markets can support software-like margins and venture-scale outcomes.

At Euclid, questions remain whether the services-as-a-wedge model will actually prove to be a valuable long-term market entry point. Our friends at Tidemark have done great work on the [patterns of control points](https://www.tidemarkcap.com/vskp-chapter/control-points-patterns-2024) in Vertical Software. Most vertical software markets have one or two control points that serve as ideal patterns for building strategically dominant Vertical Software companies. In a past piece, we shared what we believe is the optimal control point for most AI-native vertical products: an authoring layer (i.e**., **launch point) for a valuable internal workflow that can unlock revenue and deliver immediate ROI. For services-as-a-delivery startups, there’s a strong argument that their last-mile coordination layer can serve as a useful control point into larger work-streams and revenue streams. We are, however, more skeptical that services-as-a-wedge businesses can capture ownership of a control point.

We have shared many times in this piece (and others over the past year) that we continue to believe the dominant mode of “winning” in Vertical AI will be software — regardless of the way it’s positioned or by whom it’s used. There is also a subtler strategic point here that the services labor replacement discourse obscures entirely. As AI capabilities improve, human roles won’t disappear; they migrate. As such, we have argued that the [largest outcomes in Vertical AI will not come from labor automation, but from enhancing productivity](https://insights.euclid.vc/p/we-need-to-talk-about-agents):

> *Much of the narrative around AI’s value has centered on direct labor replacement, given the immediate profit potential for buyers. But we believe AI’s greater impact—and the larger market opportunity—will be its ability to enhance workforce productivity rather than simply substitute for it. — The Verticalist*

AI-Native Services will undoubtedly produce great business & venture outcomes. However, we believe the current discourse is approaching overexuberance, where founders and (some of their) backers view it as a cure-all for the classic adoption frictions in selling to vertical industries. There’s also the risk for those following the playbook of building a good services business, but one that’s not venture-scale, unfortunately, built with VC dollars and expectations. As Emergence eloquently puts it, the trap is “that you’ve built a good services firm financed with the wrong kind of capital.” This was a similar hypothesis we outlined in our initial piece on the [AI-First Roll-Up](https://insights.euclid.vc/p/the-ai-first-roll-up). Neither roll-ups nor tech-enabled services are new concepts, and both models have been well-understood and financed by private equity for years.

The wedge that drives much of the current generation of Vertical startups is inexpensive intelligence. The trap for AI Services founders is mistaking an appealing wedge for a sustainable business. We can think of many businesses, both vertical and horizontal, pre- and post-AI, that stormed out of the gate with attractive wedges, raised at lofty valuations, only to later discover their products quickly commoditized and that there was no durable moat. Our friend Rick Zullo at Equal shared a strong [articulation of this view:](https://www.linkedin.com/posts/rickzullo_ai-native-services-will-be-one-of-the-biggest-share-7442699476038778881-1wzp/?utm_source=social_share_send&utm_medium=ios_app&rcm=ACoAAAHvP5sBnZ_qhXoe13lK-lKiU98cVFp9iSI&utm_campaign=copy_link)

> *Knowing how to win in these sectors isn't just about following the growth, it’s about navigating the industry dynamics to find long-term competitive advantage. Without that, you'll have a lot of well-funded leaky buckets. As with all services companies, the value comes from long-term FCF and we're seeing plenty of companies giving away a dollar for 20 cents to grow (and even worse, some lie about their accounting to raise capital). That's not the game we're playing.*

The companies that will last are those that capitalize on the current opportunity, when cost differences are high, adoption is still early, and incumbents are slow to embed themselves deeply in their customers’ operations. The latter outcome makes switching structurally painful rather than just inconvenient. And unlike traditional software, AI-native platforms can integrate into *every* workflow, collect data from all interactions — whether a human is involved or not — and develop growing intelligence that improves the product over time. The opportunity to build “load-bearing infrastructure” has never been greater. Neither has the temptation to settle for being a “cheaper vendor.”

We’ll end this piece with a historical analogy that bears some resemblance to the current moment: the rise of the “[Fab Five](https://en.wikipedia.org/wiki/Fast_Five_(consulting))” internet consulting firms during the dot-com era. Viant, Scient, Razorfish, iXL, and MarchFirst grew rapidly by performing the outsourced intelligence work of their time, offering services such as website development, e-commerce implementation, and digital strategy advice. They reached multibillion-dollar market capitalizations and were the darling tech-enabled services companies of the era.

By 2001, all five firms had either collapsed or been acquired. The intelligence became commoditized; building a website shifted from specialized expertise to a task any competent developer could perform. Larger consulting firms developed these capabilities internally. The Fab Five lacked workflow ownership, a system of record, and switching costs. They were service providers that successfully rode the coattails of a hyper-growth technology shift… until it became widely replicable, and ultimately, commoditized. Their early brand halo was not enough to overcome the market shift and an increasingly unprofitable business model.

The Sequoia piece ends with a bold claim: “The next $1T company will be a software company masquerading as a services firm.” We’ll take the other side of that bet. The next $1T company won't be masquerading as anything. It will have software margins, software moats, and software defensibility, even if the “product” is outcomes rather than software. That distinction is everything.

---

*Thanks for reading *The Verticalist*!*

Euclid* is an inception-stage VC built for Vertical AI founders. If anyone in your network is considering building in Vertical AI, we’d love to help. Just drop us a line via the comments below or on LinkedIn.*

[1](https://insights.euclid.vc/p/service-level-disagreement-ai-services-versus-software#footnote-anchor-1)

This figure is from the Sequoia piece.

[2](https://insights.euclid.vc/p/service-level-disagreement-ai-services-versus-software#footnote-anchor-2)

David Haber and team at a16z articulate this well in their piece on the services opportunity in AEC: “Firms of many different kinds are sitting on backlogs of work they can’t take on because they don’t have the people. AI doesn’t just help them do existing projects faster; it lets them say yes to projects they would have turned away.”

Elmgren, Goggins, Haber, Schmidt (2026). *[Every Building You’ve Ever Been In Was Designed By Software Built in 1997](https://a16z.com/every-building-youve-ever-been-in-was-designed-by-software-built-in-1997/)*. Andreessen Horowitz.
