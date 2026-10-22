# Verticals: Payments as a Shadow System of Record

Published: 2026-04-01
Type: podcast
Summary: Christophe Rimann describes Camber's healthcare claims infrastructure, proprietary payer data, collection-based fees, ROI-led enterprise sales, and payments as a source of workflow control.
Source URL: https://insights.euclid.vc/p/payments-as-a-shadow-system-of-record
Featured: Christophe Rimann
Archive episode: 22
Source file: Episode 22 - Christophe Rimann
Date note: Date of the linked published episode page, not the recording or Drive upload date.
Transcript note: Automated transcript preserved as supplied; names and speaker labels may contain transcription errors.

## Transcript

Luke Sophinos [00:00:00]:
All right, buckle up for this one. This guy in 2012 was building a million dollar crypto broker dealer back when people thought bitcoin was fake Internet money. Fast forward to today. He's built Camber, an AI company that's generating millions in EBITDA uplift for healthcare clinics all over the country. How well he's doing something that nobody thought was possible. He's making insurance companies actually pay what they owe. They've raised the pre seed seed series A and series B without announcing a single round. No press releases, no victory laps, just building in silen while everyone else was chasing hype. This is a fun one. These guys are trying to build the stripe of healthcare payments and it's a really a masterclass in building a real moat in the age of AI. Let's get into it. All right everybody, welcome back to the Verticals podcast. We have a very special guest for you today, Christoph Riemann. He's the founder and CEO of Camber, which is doing a lot of interesting things around RCM and healthcare financial software more broadly. He's got an incredible background that spans technology, finance, I think even maybe a little bit of like technical operations around crypto. I'll, I'll, I'll let him dig in and kick us off and give us a little background on who he is, the journey and then what Canber is and where it's going.

Christophe Rimann [00:01:20]:
So yeah, appreciate it. Luke. Excited for this? Yeah. No, it's funny, I used to not talk about the crypto side of my background that much, but I got into crypto kind of 2012, 2013 timeframe back when it was only bitcoin, so even blockchain as a concept barely existed. I think my first exposure to crypto was actually Litecoin, which was big at the time and ended up building a broker dealer that hit about a million in run rate. About seven months into U.S. building. We were on of I think very few folks at that time who actually had a FinCEN license to do blockchain related stuff. And, and it was a lot of fun. It was kind of the wild west, you know, at that point. 2012-2013-2012-2013 is when I got in, started my company in 2015 I think, or December 2014.

Luke Sophinos [00:02:04]:
Yeah, very early to that game.

Christophe Rimann [00:02:08]:
Yeah, that was a lot of fun. And so I ended up going to grad school specifically to do blockchain related research and then after that went to McKinsey and, and did a couple years of healthcare consulting. And actually the funny thing was, you know, I was one of very few people who had as much blockchain experience as I did at that point. So that's actually how I ended up in RevCycle was, you know, this kind of natural, hey, I'm already working on payments related stuff. Let's, let's see if we can combine that with healthcare in some meaningful way.

Luke Sophinos [00:02:35]:
Yeah, yeah. You went from like no regulation to the most regulation.

Christophe Rimann [00:02:39]:
I know it was, it was really fascinating to actually try and make that jump, I'm not gonna lie, is it was like an area where you actually had no idea whether, you know, regulators would crack down to like, actually, you know, exactly what you need to do and it's, you know, a massive buck and they'll throw it at you if you do it wrong. Yeah, yeah.

Luke Sophinos [00:02:56]:
Incredible. So tell us then. So you, you do the consulting, I assume you learn a ton about rcm, you see holes in the process, and that's what ultimately became canber.

Christophe Rimann [00:03:07]:
That's exactly right. Yeah. So we ended up consulting. I, I be after that kind of blockchain experience. I spent almost my entire two years at McKinsey doing, you know, rev cycle related stuff mostly for really large hospital systems. Actually almost exclusively for really large hospital systems. I got to do some really cool stuff during COVID or when, when, you know, health systems initially kind of had this massive bust because, you know, no one was going to hospitals for elective surgeries anymore. For, for those first three months. And then my last project there, I actually was able to consult for a behavioral health provider, which was something that I really wanted to do. Actually. That was the original reason that I joined McKinsey was to, to figure out how come, you know, health insurance was so difficult to get. And I, I, my, my own personal story. I, I was diagnosed with ADHD in college, but everyone knew I had it. It's just like, you know, behavioral health coverage was not the same. And all of a sudden I got on the college health plan and could get the care I needed. And it was hugely meaningful and really important. I don't think I would be here if I did not receive that care. As in like, you know, I don't think I'd be, you know, able to run a company if I did not read that, receive that care. So that was the impetus for me getting into healthcare and that, that was kind of how I realized, hey, there's actually this kind of pret shift that's about to happen and people were aware of it, right? Like healthcare was shifting out of, you know, hospital systems for, for the past two decades. That's already been a, a pretty strong secular trend. But now, you know, there was all this new technology, this was kind of 20, 21 that was coming out that would allow you to take a very different approach to healthcare. We thought if you focused on specific verticals. Yeah, yeah. So that was the impetus. Yeah.

Luke Sophinos [00:04:45]:
And so give us, like, the founding story. So you worked like, what, what gaps did you see? What was, what were the pain points?

Christophe Rimann [00:04:53]:
Yeah. So it's actually really interesting because I was so used to hospitals, right. Hospitals. It's really, really kind of. You have these huge claims, right. You know, thousand dollars claims were small, $10,000 claims were common. Right. And so what you could afford to do is if you got paid 90, 95% of a claim, you could afford to say, hey, I'm going to have a human bingo, chase that last, know, 10% of this claim, because it might be $1,000, it might be $10,000 in some situations. And so you did. You had this, like, very human process. But then you look towards, like, behavioral health and, and a lot of forms of outpatient care, and it was just dramatically cheaper per service, which is, of course, why healthcare was shifting out of hospital systems. But the result was, if you were collecting 90% of a $150 claim, you know, are you going to be able to staff a human to collect that last $15? Well, maybe you have to. That trade off is a lot more difficult. And you know, this by the thousands, tens of thousands, hundreds of thousands of claims that any, you know, provider might be submitting. And you end up in a situation where you're collecting 90% of a lot of claims that you can't actually work. And that was actually the genesis for CAMBRU is, hey, you kind of have to take this technological approach if you actually want to be able to make this claims work at this level. Right. Otherwise, we continuously would get into these provider groups who, you know, thought that they might be collecting at 97, 98%, but you look at the underlying data and it turns out, no, no, it's actually 92, 93%, and you can't staff to get that number higher. So you're leaving tens of thousands, hundreds of thousands, millions of dollars on the table.

Luke Sophinos [00:06:24]:
And that's just because the long tail wasn't profitable. Basically, you couldn't put a human.

Christophe Rimann [00:06:29]:
Exactly that. Yeah, yeah. And the long tail wasn't profitable. The data quality was, you know, varying is how I put it. So, you know, the combination of those two meant, of course, there was a lot of money Being left on the table.

Luke Sophinos [00:06:41]:
Incredible. And so you guys, interestingly enough, we're in stealth for a few years, right?

Christophe Rimann [00:06:47]:
Yeah, yeah.

Luke Sophinos [00:06:48]:
What's the story about that? Because that's obviously, you know, it was move fast and break things for.

Christophe Rimann [00:06:52]:
Yeah, yeah, it's fascinating because I think we have the opposite problem that most startups have on the like, product market fit equation, right? Which is, you know, the market for a rev cycle has existed for 100 years at this point, right. Ever since insurance started, you know, popping up after, you know, in the 1940s. It ended up being the case that you needed people to bill it, right. And you needed people to adjust it on the other end. And so the market was there, right. Like it was very clear exactly what we needed to build, how we needed to build it, what we needed to, what the success criteria was, what the outcome needed to be, right. Like all of that was just very clear. The actual question is, could you build a product to do all of that? Right. Because you're competing with humans and you know, humans make mistakes and humans might be slow and, and whatnot, but humans are incredibly, incredibly resilient and can take very creative approach to doing things. Right. And so you need to build a system to be able to do all of these different things across many, many different use cases, but also across many, many different workflows. And so that was the core question that we needed to answer. And we were very fortunate that our investors understood that and were willing to finance that. Right. Where, you know, yeah, to your point, we raised a pre seed seed, series A and series B without announcing it. Right. And that was just because we were continuously building to be able to make sure that we were able to deliver this service that we're talking about. And so, you know, kind of in year one, we signed up a couple large scale clinics who were willing to take that bet alongside us. You know, for them it was just like, let me give you a couple payers. Let's, let's experiment with this, right? And you know, that gave us the kind of data and systems that we needed to understand exactly how to build this. And so we just kind of took those as a playbook, right? It's, let's actually figure out we know what metrics we're going for, we know what the data looks like. Let's actually build out the system to be able to do these and see if that's possible, validate that, that thesis. So, you know, unlike most companies, it was not the like, how do we match a product to a market it was really just the market exists, we know exactly what it wants. Can we actually build the product that we need to? So that was, that's why we took so long to build and why we never really left stealth was because for the longest time go to market was not our problem. We would kind of, anytime we had a, had to kind of test a thesis, you know, my co founder would go out there and three, four weeks later we'd had a couple large clinics that were signed up and willing to try.

Luke Sophinos [00:09:13]:
Pain was so significant.

Christophe Rimann [00:09:15]:
Exactly.

Luke Sophinos [00:09:16]:
There are other competitors chasing the long tail. Was that the opportunity or was, were they just not doing it efficiently?

Christophe Rimann [00:09:21]:
Oh no, we have a huge number of competitors, but they were almost exclusively like labor, honestly. Right. Like almost all of this at the large scale was being offshored at that time. Right. Still today actually I, I have to say, like, you know, nowadays there are a ton of AI rep cycle companies. The truth of the matter is when we are competing on big deals today, the incumbents that people were competing against are almost always BPOs but outsourcers offshoring this to, to, you know, overseas. Yeah, yeah.

Luke Sophinos [00:09:52]:
So that's so year one, you get in a couple clinics, you're learning, I assume because this is free AI. So I assume you're, it's kind of like zapier esque automations that you're experimenting with at that time or were you guys like very early to the AI party?

Christophe Rimann [00:10:06]:
Yeah, so I think that's the really interesting thing of what we kind of do. Right. Which is from the get go what we realized was this is going to be a large, there's a large amount of data. We actually have a kind of binary indicator on whether or not it's working. The claim gets paid. Right. And so what that lent it to is we basically have been building for the past five years a foundational model that's very specific. Right. It's very specific in its usage, which is it's for claims. Right. And so, you know, we all, I always say we honestly got kind of lucky. Right. Where it's like we, for, for the things where core machine learning concepts, core training concepts are most effective, we could use that from the get go because in 2021 that existed. You know, our initial thesis was we would need, you know, humans to be able to do long tail activities. But more and more that's proven to not be the case. Right. Like we have systems and agents able to do all of our mail processing for us now. Right. That was a huge pain point for time was Just the sheer amount of mail that we needed to digitize and turn into structured data, that's no longer an issue for us. Right. Like we now have agents that can go onto, you know, portals and pull information for us. Right. Because so much of this is happening on payer portals. And so I think we got really lucky in that sense, right. Where it's like, for the really, really important stuff, we were able to build out, you know, all the expertise in, into our systems. Right. To be able to do this. Well, and then, you know, for the long tail stuff of pulling more data into our systems, we've been able to adapt to using, you know, LLMs because I mean, ultimately what I'll say is, right, like most of the agent approaches, I think, to AI rev cycle rely on kind of underlying systems that were mostly built, you know, 10, 20 years ago. And so you can do what the systems allow you to do a lot cheaper and a lot faster, but you're not necessarily doing it better. Right. Because you, you are reliant on, you know, this other piece of system software versus, you know, because we've built it from the ground up, we can kind of understand exactly how, how to approach these problems. Yeah, yeah.

Luke Sophinos [00:12:02]:
So is that, and is that like the, the behavioral health clinic system of record that you're speaking of or is it more of like the 5,000 payment? Like I have, I don't even. Every time I go somewhere, got a new patient I got to pay through.

Christophe Rimann [00:12:14]:
Yeah, yeah, yeah, yeah. I mean, in most cases, like, I think that's ultimately the issue, right. Is like, and that's why it took us so long to build. It's, you know, we sit on top of systems of record in behavioral health. Right. EHRs is usually what people call these practice management systems. You know, there's, there's a lot of different overlap within these kind of healthcare clinics as to all these different pieces of software, including the patient portals. Usually the reason you see a different one is because the EHR has a different one. Right. And so, you know, people are switching EHRs a lot more frequently than certainly I anticipated. To switch your entire system of record feels very expensive, but especially at the smaller scale, providers are doing it constantly. And so, yeah, we were very surprised to hear that, honestly.

Luke Sophinos [00:12:51]:
Is that just because of an AI, like they're trying to move to something AI native and they feel like they need to? Because I feel like that for a long time.

Christophe Rimann [00:12:59]:
Yeah. So actually the interesting thing is like on the small scale, so, you know, clinics that are up to $5 million in net patient revenue. It's been happening considerably more frequently than I anticipated. In general. Right. AI has really helped. On the large scale, we're seeing adoption that we would have never expected to see. People are willing to kind of understand, you know, on the large scale we're kind of talking, you know, millions of dollars worth of ebitda, sometimes tens of millions of dollars. Right. And so like, ultimately when you're talking at that scale, all of a sudden large providers are really willing to consider it because honestly, at this point we're also fortunate. Part of the reason we're lucky is because we've been for certain large scale clinics with recognizable brand names and backed by private equity investors that are very recognizable. We've been doing this for three, four years. So we're able to go back and say, hey, yeah, for this large scale Clinic, we've generated $8 million in EBITDA and here's how. And now in this AI AI world, folks love that, right? Like, love the fact that we can point to the, the fact that we've been doing this for a while now. Yeah, yeah. But on the small scales, wild people just switch. You switch, you know, systems left and right. Yeah, yeah, yeah, yeah. It's, it's been interesting actually. Like sometimes people will switch their system of record just to be able to use us, which has been very surprising. I think one out of three deals on the small scale people are switching their system of record as well to, to use us.

Luke Sophinos [00:14:23]:
That's because the most important thing is revenue.

Christophe Rimann [00:14:26]:
Right? Exactly, exactly. Yeah. You know, it's, I all time and time again, I've just been shocked at how unstick, you know, because certainly vertical software we think of as so sticky and I think it is incredibly sticky in most other verticals. But you know, in, in, in the areas of healthcare that we operate, that's not been true at all. Yeah, yeah.

Luke Sophinos [00:14:44]:
Well, we all need to take a lesson out of your book on timing because 2020 12, 2013 to crypto and RCM and BEH Health with AI launching 12 months later was like beautiful. Beautifully.

Christophe Rimann [00:15:02]:
You know, I, I feel like I've gone lucky a number of times now where it's like, yeah, you know, it's, it's funny, it's funny now talking to like large scale clinics because they're like, oh yeah, AI recycle is a category, you know, and, and, and two years ago they were like, you want to do what with our, with our claims? Right. Like, it's, it's, it's been fascinating to See that kind of transition, honestly. Yeah, yeah.

Luke Sophinos [00:15:22]:
So let's talk a little bit about the transition from kind of pre AI to post AI. Like, what did the product look like before, what did it look like after? What did the, like the results, the data. Did you see significant uplift there? I assume you did.

Christophe Rimann [00:15:37]:
Yeah. I mean, you know, the interesting thing is we once again built on an a thesis that is now popular in AI. Before, you know, AI was really a thing, right. So, you know, nowadays you read, you know, Andreessen Horowitz has a piece on it. You know, like every major VC has a piece on how, you know, the palantirization of what we're. Of what's happening. You know, your AI is going to allow you to sell services, but really use software to provide it. Right. And so that was always kind of how we approached it. Right. Is like, you think of us as a services company. Most of our providers think of us as a services company. Like I said, we compete against mostly like outsourcers. Right. And so, you know, we were, we were lucky in that we were early to that thesis of the idea that you could replace just a massive amount of this guy, in this case offshore labor with just models. Right. And so the accelerant has more been around how we are able to adapt those models, how we're able to, you know, learn faster than ever before. Right. Like, you know, we have a project internally where, you know, every payer manual that that is provided, every new payer update, you know, gets. Gets inserted into a, you know, kind of a rag system internally that we can produce new outcomes for these payers. We can understand how payers are thinking from unstructured data far, far, far faster. So what I've really seen accelerate is the rate at which we're learning. Previously, the idea of launching three new verticals in a year would have not been possible just because every vertical we need to learn so much. Right. This year I think we're launching probably five new verticals. And it's just because you're able to learn so much faster than ever before and that' across every level. Right. And using those learnings to turn it into actual systems and software is faster than ever too. And I think that's why we're lucky on the flywheel perspective, right. Where we're able to kind of take in this learning, update our systems in real time. And we've built out the core foundation of people that very quickly and very well.

Luke Sophinos [00:17:34]:
Yeah. And you had a vast proprietary data set. Like the stuff started coming Out.

Christophe Rimann [00:17:38]:
I mean, you know, like, that's the thing is like we actually end up having a lot of parallels to like a lot of the foundational models companies. We're very, you know, we have a lot of experts internally labeling and understanding the data. We call these our insurance operations team. They're phenomenal, right? Like, they just understand our head of insurance operations loves claims like no one I've ever seen. Right. Like, I think I love rep cycle but like, you know, she will just like go and chase down what's going on at any time at any cost because it's just like she loves, loves doing that. And the result is we have all of this expert data, right? We have, we have, you know, at this point, five years, billions and billions of dollars worth of expert data that we're able to use, you know, kind of update and train the way that we submit claims, right? So, you know, very similar from a core, core foundational perspective to how a lot of the model companies are thinking about it. We just have a very specific one. Yeah, very specific model, if you can

Luke Sophinos [00:18:30]:
just walk us through is like, so for me, someone who hasn't built in the healthcare vertical, highly complicated, I've always found, you know, who's paying, is it insurance, is it the patient?

Christophe Rimann [00:18:40]:
Right.

Luke Sophinos [00:18:40]:
Like it's challenging, dynamic, always happening, especially in behavioral, because the rules, as you said, haven't been totally clear or well written like they have in, you know, traditional healthcare. Can you just walk us through like an example patient goes to this place and then talk us through like what the product is, how it works?

Christophe Rimann [00:18:59]:
Yeah, yeah. So you know, you go into a provider's office, usually what the first thing that happens is, they'll do what's called an eligibility check, right? So they'll take your insurance card, look at the information on it. You know, honestly, it's one of those things where it's like, like I think if you ask most people with health insurance to explain all the numbers on an insurance card, you can't do it. Like I, I certainly could not do this, you know, when we started this company and I'd been a rev cycle consultant for a few years at that point, right. And so, you know, but, but what's happening behind the scenes is they'll call the number on the back of your insurance card, they'll ask, hey, is this person eligible or not for this, these services? Right? I'm about to do this. Is this, is this, you know, kind of legitimate or not? Can, can, will you pay me? And you know, lots of providers will do that. Hopefully most providers will do that. Not all providers will do that, especially in behavioral health, because you're seeing the same patient so frequently, it doesn't really make sense to do an eligibility check every single time this person comes in. But, you know, that's how it typically works at a provider's office. They'll capture all the information on the card, put it into their system. You go into a session, a visit, a clinical visit, and you know, they'll render some services. They'll capture that in their ehr. And you know, you, it depends on the service that's being provided. But you know, they might at that point actually do what's called medical coding, right? And actually pick, you know, what services were being rendered and do that in a structured data format. Not always, just sometimes that's another team. It depends on the complexity of the healthcare that's being rendered. And then, you know, they kind of send it off. And what by send it off, what I mean is like they usually sign, sign it, right? They, they lock the session in some way, they sign it in some way to basically attest, yes, I provided these healthcare services, right. Typically what then happens is a back office team will look at that data and turn it into a claim. Right? And it depends on the sophistication of the healthcare provider. But oftentimes that just means like, hey, let's map all the stuff that we have today and put it on the, on on the claim digitally. I don't, I don't want to, you know, pretend that they're writing out, writing out these claims. Although actually, you know, a fair, a larger number than you would expect are writing out the claims, right? But you know, digitally kind of put all the data over there, click a button, submit it to the insurance company, and then, you know, depending on the vertical, anywhere between 20 and 40% of the time the insurance company will say, no, you didn't do this. Right. For these reasons, right? And then you'll take those reasons, update the claim, resubmit it, and then you kind of go through this loop, right? And this loop usually lasts anywhere from 180 days to three years, right. Of like, you know, whether or not you get paid. Right. What we've done is we basically have reverse engineered this lease loop, right? So, you know, we understand before we submit the claim, okay. You know, 20 to 40% of the time the payer will actually deny it for these specific reasons that we see on the data. Right. This is why we have to be so vertical specific because we have to understand what the insurance company is doing in that vertical to get paid or not paid. Right. And so let's understand it and then, you know, let that data flow back up to our systems and then submit a really good claim. Right. And so, you know, typically, typically we see pretty good first pass claim rate in our core verticals of like 80 to 85%. Right. So you submit a claim.

Luke Sophinos [00:22:03]:
So that's. They would do without you guys.

Christophe Rimann [00:22:05]:
Wow. Yeah, yeah, yeah. So you know, that. That's good. The lowest we've seen. And, you know, for these are for clinics that are like 2,300 million plus the numbers that I'm referencing. So pretty large businesses. I mean, I've seen a clinic that was 500 million plus that got paid 60% of the time they submitted a claim. Right. So you can imagine those numbers are quite poor. Right. And in the best case, you're seeing 80 to 85%. Right. With us, you typically see about 95%. Right. So you can, you can kind of imagine the sheer amount of time that's required to get paid. The sheer amount of effort that's required to get paid drops dramatically, sometimes orders of magnitude. And then what that means is we can spend the time and effort to get you from 95 to a higher percentage of collections overall. Yeah, yeah. So, and then we'll handle all of that automatically. Right. There's no humans that we need to kind of submit claims. There's no humans that we need to kind of in. In most of the cases now where we get a denial, we can automatically fix that denial.

Luke Sophinos [00:22:55]:
No human in the loop at all. It's all agentic.

Christophe Rimann [00:22:57]:
So we do have some humans in the loop because we need. In the cases where we actually think that there's a lot of learning opportunities, we do have a human actually go in to update the system. Right? Because like I said, what agents do is they do the existing process faster. Right. But what we can do is if we understand, hey, there's an opportunity here to improve our system upstream, right? We'll have humans go work those claims because what that allows them. What that allows us to do is make sure that problem doesn't happen again. Yeah, yeah. They catch it, they fix it, they make sure it never happens again. Right. And so that's why I actually think, we actually think that having humans in the loop is important for us. In the same way that, you know, an LLM company will thinks that having those experts is really, really critical. We actually think it's really important that we hire, you know, people who love claims. Right. Who want to understand how these things work to update our systems. Yeah.

Luke Sophinos [00:23:47]:
How does that hit like gross margin? Do you? Yeah, because you're, you know, you have this services element that's obviously becoming incredibly popular in this age. And then you, the, the SaaS element, like are you in between two.

Christophe Rimann [00:24:00]:
Yeah. So actually part of the reason we stayed in stealth is the only number we really focused on during that period is contribution margin and gross margin. And so what, what I did during that period is I, I said we are not going to offshore, right. So we are going to set a gross margin target and a contribution margin target and we're not going to offshore because explicitly if you do that, then it's pretty easy to hit mar. You're not going to automate and it's going to be really, really hard to go back and automate. And so the explicit mandate that we had was we're not going to do that, we're going to, we're going to do it the hard way. Right. And that it took a very long time as a result of that. The result is actually we, we see, we see gross margin. I mean, I don't want to get into specifics yet, but you know, our gross margin is, is actually pretty standard SaaS, if not upper, upper, you know, quartile SaaS. Yeah. Yeah.

Luke Sophinos [00:24:41]:
That's incredible. So super, you know, obviously super competitive market, even pre AI, now very competitive market, post AI. Have you found that like specifically honing in at behavioral health or like these, these more micro verticals within healthcare is, you know, the competitive advantage, like are most of the new entrants just broad and wide and they can't go as deep as you or like how do you think of your guys, competitors and specifically your moats?

Christophe Rimann [00:25:08]:
Yeah, no, I mean, I think that ultimately that data and specifically that human label data is our moat. Right. And that's why I think, you know, now at this point, you know, behavioral health was our first vertical, but you know, we're in a number of others as well. You know, we're doing kind of physical therapy, neuropsychology, we're doing, you know, ent, we're doing some cardio. So, so, so we're in a number of verticals at this point. And you know, the results have been we're just able to drive outcomes that, that other folks aren't able to because we stay so focused. Right. And so, you know, certainly our ambition is to do, you know, most of certainly outpatient healthcare over the long term. But today, you know, in any verticals where, where we spend a lot of time. I mean we, we actually price on the, for, for larger clinics, we price based off of outcomes. Right? It's not like, hey, there's a, there's a software fee and a, and an agent fee. It's like, hey, we know we can drive these results, like put us to the test. Right? If you want to put us head to head with someone. So far, I mean we've been fortunate, but we've never lost a deal head to head because like, you know, ultimately the outcome is the outcome. Right? So, and I, I, I, I think, you know, that that's been. The interesting thing is like there's two ways to think about these problems in rev cycle. You can either think about it as just purely cost savings or you can think about it as yield. Right. Uplift in the amount of your collections. And so when we work with large scale providers, we target both very explicitly and I think most agentic companies today that we would view as competitors target primarily that cost component. And so you're able to see cost savings. But yield kind of doesn't necessarily improve that much versus we target really just ebitda. That's the number that we care about when we talk to large scale providers. Let's just make that number go up as much as possible. Let's agree on it and let's figure out how to make this happen. Yeah, yeah, yeah.

Luke Sophinos [00:26:53]:
So you were early to the outcomes game too. Have you not charged any, you don't charge any sort of SaaS fee today still?

Christophe Rimann [00:26:59]:
So we don't charge a SaaS fee, no. Yeah, yeah. So we do charge a base fee, Right. Which is a percentage of your overall collections. But that base fee ends up being almost always cheaper than whatever you're paying today. Right. By a reasonable amount. So you know, that's the goal is like, hey, on the large end and if you're willing to give us your business, you're guaranteed a savings. Right. And then if we are able to do what we say we can do, we will participate on that. Right. But basically like from day one, you're going to have some sort of impact on your bottom line and then that impact should scale as our relationship kind of continues. Yeah, yeah.

Luke Sophinos [00:27:34]:
And what's the success rate in getting to outcomes? Because one thing I talked about recently, recently on the pod is most founders think of outcomes as like a revenue lift or an EBITDA lift. And that's fantastic. The only challenge is it takes, it could typically, I don't know if it's your case it takes a while to see that.

Christophe Rimann [00:27:51]:
All right, we're going to take a

Luke Sophinos [00:27:52]:
short break to give a big shout out to our sponsor, Paraffin. They're the ones who make verticals possible. If you haven't heard of Paraffin, go check them out. They build embedded finance tools that really help your merchants grow. They're the leader in vertical software and embedded finance. And so if you're building in the space, haven't explored Paraffin yet, go check them out. They've got embedded credit, embedded spending, a lot of different tools to really drive revenue growth, drive TAM expansion, and really improve retention. So big shout out to Paraffin. Go check them out. Now back to the episode.

Christophe Rimann [00:28:25]:
Yeah, yeah, yeah. I mean, we usually see the first pretty significant lift in 60 days. And, and the reason being that's when the first insurance claim claims, you know, when we have a big enough cohort of claims coming back. Yeah, yeah. So, you know, like, honestly, when we do a pilot, usually about 60 days in is when the pilot converts for us because, you know, you're pretty much immediately able to see, oh yeah, like we're performing much better than we did without Camber. And so, so, yeah, I mean, outcomes for us, usually it's a, it's like a quarterly process. Right. It's not like a multi year process, but it's not immediate. It's like, hey, you know, by the end of the first quarter, you know, we're, we're, we're typically going to see some pretty significant uplift in your outcomes. Yeah, yeah, yeah.

Luke Sophinos [00:29:01]:
So every quarter you're basically going back to each customer and showing them, hey, here's what we did, here's our percentage. Contested, but yeah, exactly, exactly that.

Christophe Rimann [00:29:10]:
Right. It's like, you know, you're doing $150 million worth of revenue, you know, this year we expect you to collect $4 million more. Right. And so you can imagine for, for some of these healthcare businesses where margin is quite, Quite tight, like 4 million, 150 million is pretty transformative. Right. And that's, that's been the really cool part is, you know, honestly, when we started, we didn't even realize that the, the outcomes we were driving were as kind of transformative as we expected. Like, it's only been in the past couple of years where we're talking to these people and they're like, oh, wow. Yeah, like there's, I would do almost anything to increase by a hundred basis points, let alone, you know, 300. Yeah, yeah.

Luke Sophinos [00:29:44]:
You have any issue in like attribution, like people saying, hey, this didn't come. This came from. We, we, you know, increase marketing spend by this much or.

Christophe Rimann [00:29:52]:
Yeah, I mean, so that's the thing is like, for us, it's, it's the, the nice thing is it's very objective. It's collections. Right, right. It's like, here's what you were called, like the number that we're really focusing on. So we don't, we don't take credit for the overall increase in ebitda.

Luke Sophinos [00:30:04]:
We just take on that.

Christophe Rimann [00:30:05]:
Exactly. Just on the collections. Right. You were collecting a 93% before, now you're collecting a 97%. Like that 4% is pretty clearly thanks to us. And that's why we want to own that whole process is like we want to be able to showcase that to you. Yeah, yeah.

Luke Sophinos [00:30:19]:
Interesting. So, you know, one of the classic debates in vertical software and I'd love to get your view on this, and there's a new debate that we'll talk about too after. But the first one is, you know, do you need to become the system of record, avoid getting eaten, you know, or is this just so complicated that it has been, because there's been RCM companies forever, that it's not going to happen? Like, I'm, I'm sure you thought about that problem deeply for a long time.

Christophe Rimann [00:30:48]:
Yeah, I mean, ultimately our perspective is like what we're building is much more akin to a stripe. Right. Like we, we think of ourselves as a payments network. What we need to prove out is that it's actually really hard to do this. We, we think that, you know, the fact that no one's built it for quite some time and even now we're able to drive results that other folks aren't able to is kind of proof of that. But I mean, you know, for. Certainly we see a lot of systems of record try to build competing products. To us today, our thesis is what ends up happening is you're able to demonstrate just purely from a pure numbers basis that our process, because we're able to see way more data than any individual system of record in our core market, actually we now see about 25% of all the data that flies around on a daily basis. You know, certainly no system of record is able to see that amount of data. We're just able to automate far more of this. And so what we believe is it's actually very much a vertical SaaS play in that sense. Right. Historically, a lot of vertical SaaS has seen a lot of their margin come from the payments layer. Right. But the payments Layer has been complicated enough that it's required a dedicated solution. Stripe, Adyen, whatever you want to call it.

Luke Sophinos [00:31:57]:
I buy that in healthcare.

Christophe Rimann [00:31:59]:
Yeah, yeah, yeah, exactly that. Yeah. And so what we really believe is, you know, over time, if we're able to truly build this product in the way that we want to. Like I said, you know, first, first claim submission, we're getting paid 94, 95% of the time. That's close to, it's not quite there yet, but it's close to credit card rates. Right. And so, you know, that's, that's the notion is, you know, we are actually the horizontal layer that vertical software should use and we have a couple of partnerships that we haven't announced yet. Actually there are a couple systems of record and we were doing a kind

Luke Sophinos [00:32:31]:
of an embedded business model on top as well.

Christophe Rimann [00:32:33]:
Exactly, exactly that. Yeah. There's a couple systems of records in our space, vertical software in our space that already use us as their payments layer. You just, you, you just wouldn't know. Yeah, yeah.

Luke Sophinos [00:32:41]:
Is that the longer term vision to kind of move into that direction or you think we doing both indefinitely?

Christophe Rimann [00:32:48]:
Yeah, yeah. And so I think that's been a really interesting question over the past, you know, six to 12 months, actually. Believe it or not, we started as pure vertical SaaS that wanted to monetize via the payments layer and end up having to build the payments layer that didn't exist. Right. So, so, so, you know, like we, we, we find ourselves in a very different spot than I think are, are. Funnily enough, Rev cycle was a appendix slide for us in our seed deck. Right. Of like, here's how we're going to monetize. Here's all the, the numbers. Like, you know, we're, we're, we're starting to see this become a, a thesis like that's, that's what we're going to do. Obviously that turned out to, to, you know, we, we ended up having to build it ourselves. And so certainly I do expect, you know, more and more folks to, to, to especially on the small side of the market. I think from the small side of the market, you know, charges and, and systems of record is, is the ideal case for us on the large scale. I think, you know, in the same way that, you know, any very, very large merchant on Shopify will have their direct relationship with Stripe. I expect that to be the case for us too. But, but you know, on the small scale, like if you're using Shopify and you're using Stripe, you don't really know or care in most cases. Yeah, yeah.

Luke Sophinos [00:33:52]:
So what, what keeps you up at night in terms of like, is it stripe coming into healthcare? Is it. It's, you know, Claude, like if you've been active on X, like I have the world's panicking. Is it COD code is doing what we're all doing. Like what's your.

Christophe Rimann [00:34:08]:
Yeah, I mean I certainly believe that, you know, over the next 18 months the landscape is going to change so dramatically and that is actually what keeps me up more than anything else. Right. It's like, you know, we are building based off a lot of first principles that we believe will remain, will adapt to an AI first world. And you know, some of those principles are like, functionally we are, we believe that a specialized system and model is going to be able to beat out a larger language model in kind of most cases head to head, whether that be on cost or that be on quality. This is particularly true because I'm sure, you know, but most large language models have not been able to access underlying healthcare data. Right. That's been one of the primary areas. So we actually think there's like some regulatory tailwinds for us there where it's ago we just, we've been fortunate to have access to a lot more healthcare data than, than most and, but you know, I think the uncertainty is what scares me the most. You know, that's, that's what keeps me up at night is like ultimately, you know, will healthcare claims look the way that they do today in, in, in a 18 months is an open question. Right. We, we talk to providers and insurance like, you know, we, we're enough, we're the counterparty in enough healthcare transactions now that we have a large number of conversations with insurance payers and regulators as well. Right. And we know that they're adapting and changing things faster than ever before. And so whether or not the landscape is the same in 18 months is completely, completely open. And that's why we spend so much time there is. We want to make sure that we can then adapt and change our own business model. But ultimately I think the only thing that can be stable over the next kind of 18 months is some sort of network effect. And for us, we think that's why the data mode is so important. You're able to just have more data on more providers, you're able to label that better than anyone else and that should, should be a sustainable note in this environment. But, you know, who knows what happens in 18 months?

Luke Sophinos [00:36:05]:
Yeah, yeah, the ground is shifting. I mean my view and I, I've had a lot of discussions and I've gotten phone calls from every direction on what's going to happen. My view is like horizontal software is in a really tough spot. I think point solutions are in a really tough spot. I think, think, I think real like real moats today are proprietary data sets that don't make them into LLMs that don't get trained on. You know like look at open. What open evidence has accomplished by training on a very specific like healthcare approved data set and not the vast open Internet doesn't mean that you know those guys won't come out and do things. I know Chat GPT launched something healthcare but it's always going to be very broad. And so my second piece is beyond the proprietary data set is like focus and the Nichier the focus the more likely you are to just you know, be able to own that market and that system. And then the third is like how do you wrap services and you know, more value around, more like industry specific value around the offering And I think there's like a ton of examples of that but you know, outcomes based billing like an company is never going to do. I doubt like a healthcare based billing like they just are money, they don't need to. So that's, that's kind of my view of like what's safe and what's not. Do you disagree with any of that?

Christophe Rimann [00:37:26]:
No, I actually fundamentally think almost all of that I agree with pretty strongly and I think that's the thesis that we're built around, right? It's like we need to be able to have these core data moats. We need to be able to have like honestly like I have to say probably like 30, 40% of the value that we provide on the enterprise side is change management. Right. It's that services layer that you're talking about, right? It's like it's really to adopt like the truth is if you are a true outcomes based company, the only way to drive an outcome is to actually adapt the workflow to this new model of working and the only way you're actually going to be able to do that is, is to get on the ground and do that change management with folks. Right? Because if you don't do that you have the best technology in the world. But you know, if it's deployed even 10% incorrectly all of a sudden it doesn't drive any real impact. Right. And so I mean I think yeah

Luke Sophinos [00:38:12]:
around this is what's missed on X, right. Is like people that aren't in the Field aren't on the ground, don't understand the change management piece, which is significantly harder than people realize. That's number one. And then number two, it's like they're not opening up Claude code in, you know, these verticals. Like that's. They. I think they will, but it's so, it's, it's still such a foreign. Like the 99% of the, the, the population today thinks that AI is a Google replacement and it's a much better.

Christophe Rimann [00:38:44]:
No, I think that's exactly right. I mean, you know, like anecdote. I mean, we've seen one CEO actually that, that does use cloud code and honestly he's, he's really cool. He's doing a great. Sorry. Yeah, he's doing phenomenal. Like, that clinic is like, that provider group is awesome to work with. Right? But then we're seeing a large number of our provider groups. Like ask us, you know, literally what Claude is actually right, like, you know, top, top 10 provider groups with, with the CFO asking us, oh, you know, what's the difference? These two AI tools where one is just doing your accounts, literally accounts payable, and the other one is Claude. And so the gap in knowledge is still very, very large. And I think ultimately in the space that we're talking about, it really depends on like, hey, if you have human providers, you're going to need change management at the end of the day, right? And the question of course then becomes, will we always have human providers? But for now it seems like the answer there will be yes. And so you definitely need that change management aspect. And yeah, to your point, that's been absolutely true. Most of our, most of our clients absolutely see Claude as a better search agent or search tool. Yeah, yeah, yeah.

Luke Sophinos [00:39:49]:
You know, I think the. When, when founders, like, ask me what, you know, when everyone's freaking out. I mean, my view is like, if you go vertical and you focus enough, like the goal you should have is to become the AI arms dealer that's, that's protected and then build, you know, if you can access proprietary data set or you have a proprietary data set, like you can be the AI arms dealer and bring that in and like that. That's going to be the next generation in my view, of like vertical winners.

Christophe Rimann [00:40:18]:
Right?

Luke Sophinos [00:40:18]:
You're going to have companies that are the most valuable companies in the world and then have a. Just like we see in VSAAS today. Like instead of the system of record being the dominant player, it's like. And I think some system of record will evolve into that, but there'll be no new companies that just become the AI arms dealer of that. And they look, you know, they're healthcare folks specific, they look like Claude. But it has all the workflows built in. It has the financial capabilities that you're talking about that are incredibly complex, that don't, you know, that stripe can't do in healthcare because it's pay this, pay that. Right. That's my view.

Christophe Rimann [00:40:53]:
No, I mean, I think that's like, for me, at least from where we sit, I think we absolutely agree with that. Actually, funnily enough, I was talking to a CFO right before this and, and we were talking about this concept and that is exactly how we think of ourselves. It's AI arms dealers. Right? Like that. I actually used that word for word like, like we. You know, the truth of the matter is like you're going to see things evolve a lot over the 18 month, next 18 months. Do you want to pick a vendor right now that is going to lock you into one way of doing things or do you want to pick someone like us who we can be the ones to think through, you know, okay, you know, for this specific use case of calling this pair, this is the most effective way to do it. Right. For this specific use case of interacting with this portal, this is the best way to do it, right. Like you could, you can pick 20 different services and then lock yourself in and you know, they might be pretty generic. Right. Or you can pick someone like us who can adapt based off of where the world is pushing.

Luke Sophinos [00:41:46]:
Yeah. And this is another piece that I think people that like a lot of investor sentiment and I can't poke at Nick the investor, that's. But like the investor sentiment I think misses the, that vertical services. Businesses want to work with one company and they're like, I like, they don't want to work with vendors, they want one that they trust. And a new kind of area of trust is, does this guy know AI? Can he help me fill in all my gaps with AI? Can he actually. Is, is he actually improving my revenue and my Eida with AI? Like that's, that's so important. And a million companies are going to get left behind because they're not, not thinking like that.

Christophe Rimann [00:42:25]:
Yeah, no, I, I think that's absolutely right. And, and certainly in our cases, what we're seeing on the, on the ground is, you know, the main difference right now is that people realize their outcomes can change. Like most of our providers, if I'm being honest to myself, do not care if you're what you're doing to make the outcomes change. Right. They understand based off of the news that they're reading that outcomes that you could previously expect now you could expect something far different and far better. Right. And so they want to be part of technologies. Yeah, no, they don't at all. Yeah, yeah. It, in fact, they would prefer not to think about it in many cases. Right. They want to just know.

Luke Sophinos [00:42:57]:
Scary to them.

Christophe Rimann [00:42:59]:
Exactly. Yeah. And, and, and, and, and what's more is like their businesses are so complex in the, in the healthcare space that like adding this as another element is kind of wild for, for, for like, I don't think they should be thinking, I mean, you know, if you think about the way credit cards worked 20 years ago versus the way they work today, like people knew far more about credit card regulations in the 1990s than they do today. And that's a good thing. Right. People should not have to think about, you know, know, hey, this individual, you know, issuing bank is going to do this kind of kind of process. Right. Like that's all been abstracted and obfigated away. And I think it's kind of ridiculous that in healthcare we expect, you know, small business owners to not only run a small business with all the same complexities of every other small business, but then tack on, hey, you need to know every single thing about every single insurance company that you're working with that seems.

Luke Sophinos [00:43:46]:
I, I hope you solve that problem because it's such a, I mean, my fiance broke her elbow last year and, and yeah, it was 12 months of like, like this portal, that portal rejection. You owe $100,000 now, you owe $2,000 now you 50 right back to 2. It's like, oh, I mean, yeah, people

Christophe Rimann [00:44:07]:
forget when credit cards first started, it's, you know, for any big purchase, someone would be going into a back room and calling the issuing bank and being like, hey, is this a legit, you know, can I actually trust this person? Right. That's what's happening in insurance today. Right. It's, it's, it's the same process. Yeah, yeah, yeah. It's.

Luke Sophinos [00:44:23]:
There's going to be like a checker for every single person who walks into

Christophe Rimann [00:44:26]:
a. I mean, that's the hope that is. Yeah. Yeah.

Luke Sophinos [00:44:30]:
Fascinating. Well, let's, let's wrap on Go to Market then, because I know we didn't get into. And I'm curious. That's always really helpful for all the listeners. Like, talk to us a little bit about the Go to Market. I assume it's a lot It's a lot less lengthy than I would have presumed given the outcome space. And so talk to us about like sales, how that works and then, and then let's bleed in that into customer success implementation.

Christophe Rimann [00:44:52]:
Yeah. So we have two books of business, right. On the SMB side and on the Enterprise side. The Enterprise side, you know, to your point, it's been way faster than we anticipated on the Enterprise, I think, because all they care about is the outcome. So if you're able to demonstrate that quickly, like we do what's called a diagnostic, so we'll come in, hook your data up to our systems and just say, hey, here's what we think is possible and here's why. Right. And as a result, here's how we're going to price the outcome. Right. And if you, you know, that, that, that ends up being a pretty convincing case. And actually like kind of one time out of ten we end up saying, hey, there's probably not an outcome here. Right? And because there's not an outcome, we're not going to try and sell you something because, like, it's not going to be good for our business. Right. And so that's the way it works on the Enterprise side. SMB, they're building, buying a service, they don't really even think about the technology component of it at all. It's just like, hey, you're, you're buying a service that is better and faster and cheaper than, than before. Right? So yeah, that, that's kind of the two different, different processes and they've just been, especially on the Enterprise side, it's been much faster than expected and is fast.

Luke Sophinos [00:45:46]:
60 days, is that like 60 days? Like 90 days?

Christophe Rimann [00:45:48]:
I wouldn't say it's like 60 days. I would say it's closer to like a quarter or two. But you know, like previously these. That's unheard of.

Luke Sophinos [00:45:54]:
That's unheard of in that world.

Christophe Rimann [00:45:55]:
Yeah, yeah, yeah. RFIs would be 18 months, right? Yeah, yeah.

Luke Sophinos [00:45:59]:
Is it outside sales? Is it, is it feet on the street?

Christophe Rimann [00:46:03]:
Yeah. I mean, on the Enterprise, on the SMB side, yeah, it's, it's all, it's all kind of on the street, the, on the Enterprise side, it's much more, you know, making sure we're in front of every major decision maker. Right. Like we, we work a lot with a lot of the larger providers. And, and honestly, that's very much a, a network that we're fortunate to have broken into. That's part of the, honestly, part of the vertical specificity is also for that purpose. Right. Like, you know, when we're in a vertical and we have, you know, the top five logos in that vertical, it becomes pretty easy to sell the other ones. Yeah, yeah.

Luke Sophinos [00:46:31]:
And you've had a lot of, there's a lot of tailwinds too with just PE roll ups in these space soon. Working with a lot of funds.

Christophe Rimann [00:46:38]:
100%. Yeah, yeah. So I mean, you know, at this point one of our most common go to market strategies is to, to talk to the private equity first. Yeah, yeah. Because they, they're the ones that are most eager to make sure that they're,

Luke Sophinos [00:46:48]:
they want to buy it and then put you in and then see the.

Christophe Rimann [00:46:50]:
Exactly, exactly. Actually, we've seen an increasingly number of pes bring us, bringing us in during the diligence process. So before you buy an asset, bring Camber in, understand how their books look and then if, if, if there's a, if there's a Y there or if there's there a. There's their leverage camper.

Luke Sophinos [00:47:04]:
Yeah, that's awesome. Well, you got to get some equity from them on those deals.

Christophe Rimann [00:47:08]:
Honestly, I wish, I mean the way we're sharing in the upside. So that's my justification there. So. But, but yeah, no, honestly, I wish.

Luke Sophinos [00:47:16]:
Awesome. And then, and then customer success. Like what's implementation, what's rollout?

Christophe Rimann [00:47:20]:
Yeah, yeah. I mean, you know, like I said, change management is tough. It's really tough. And, and so we have, you know, a pretty large team that, that's related to, you know, kind of implementations on the enterprise side and then we have a separate implementation team on the SMB side as well. Right. And they're, they're, you know, different processes, different, different kind of onboardings. And then, you know, I think the truth is because we're replacing services businesses, we're able to have a much closer touch point to our customers than, you know, most SaaS companies. Right. You know, our contract sizes are probably about 10x what equivalent SaaS SaaS contract would look like. And so we do check in very frequently. We know, we know, you know, our CX associates know, know the businesses that they're working with very, very well. And that's been really cool. Right. You're able to use the data that we have to actually help them grow revenue.

Luke Sophinos [00:48:04]:
Right.

Christophe Rimann [00:48:04]:
And, and then, you know, when the revenue grows like because of the way that we're structured, that's more revenue towards us too. Right. So we have this very, very aligned incentive to help them grow as much as possible. Yeah.

Luke Sophinos [00:48:14]:
Do you have to hire those CX folks from industry.

Christophe Rimann [00:48:17]:
So we actually typically don't. Mainly because the way we do things is so different than most, you know, billers. Right. So we actually typically find that people with limited healthcare experience succeed best on the CX side. Yeah, yeah.

Luke Sophinos [00:48:33]:
You ask anybody in any vertical and it's a different answer. And so this is like the org chart structure on that side of the business. Is it basically like CX and then they're a bunch of agents below them and that's kind of your process or is it?

Christophe Rimann [00:48:44]:
Yeah. So CX is mostly people today because the question, the things that we're working on, like most of the stuff below them has hopefully, hopefully been helped.

Luke Sophinos [00:48:53]:
They're not managing a team of agents.

Christophe Rimann [00:48:55]:
No, no, no, no, no, no. They're, they're there to own the, the change management, the relationship with the provider. Right. They're not that way. We can kind of make sure the, the goal here being every single learning that we have applies to all of our providers. And so we actually explicitly chose not to do that because we want the learnings to happen upstream to that. Right. If you're using, I mean, certainly our CX team uses agents in all the ways most CX teams use agents today. Right. But they're not like literally having those agents, agents, you know, run up a claim themselves. Yeah, yeah, yeah.

Luke Sophinos [00:49:22]:
Well, this has been awesome, man. Let's, if we can, we'll wrap on a, on a quick, rapid fire. So first, first question, you know, and it, it can be quick, but where are you guys in like five years? What's best case scenario? What's. What's worst case scenario? What's. What's the conservative estimate for the board?

Christophe Rimann [00:49:41]:
Yeah, no, it's, it's a good question. Five years, you know, best cases, we're a payments network. Right. You adopt Camber because, you know, that's what you do. You, you don't even think about billing as an option. Right. Worst case, we continue to be a billing BPO that you think of us that way. Right. And we're in an increasingly competitive market. We hope we can continue to demonstrate the outcome. Right. But that's kind of the worst case here. Mid case is like we're making that transition between from a outsourcer to a true payments network. Yeah.

Luke Sophinos [00:50:09]:
The credit card heuristic is really interesting because it's so on point.

Christophe Rimann [00:50:14]:
I think that's what most people don't realize is because we only interact with, with good credit card processors now. You don't realize how complicated it was 30 years ago in, in, in behind the scenes. Yeah.

Luke Sophinos [00:50:26]:
Head of sales. Industry focused or not, what's your preference or from the industry?

Christophe Rimann [00:50:32]:
Yeah, yeah. Our head of sales is, is it has both done industry stuff and non industry stuff. Yeah, yeah, yeah, yeah.

Luke Sophinos [00:50:39]:
In all technology companies or they've been

Christophe Rimann [00:50:41]:
on the, the all technology. All technology. Yeah, yeah.

Luke Sophinos [00:50:44]:
But well, this has been awesome, man. And then, and then let's just wrap with any sense of like scale, capital raise where you guys are at, where you want to go.

Christophe Rimann [00:50:53]:
Yeah. So we've raised about 50 million. We're about 90 people today. Almost entirely based in New York, Andreessen Letter, Series A and series B. And you know, I think kind of over the next 18 months we have a lot to prove on the scalability side. Right. Like, I think that's really kind of where we're very fortunate to be working with a lot of large providers in our core spaces. And now it's like, okay, how do we add more spaces? And increasingly aggressively we've, we know the tech works. That's been really cool to see the tech works in, in, you know, very, very different spaces. It works. And like I said, ENT cardio in addition to behavioral health, we, we've proven that out. But now the question is like, can we scale the go to market motion? Yeah.

Luke Sophinos [00:51:27]:
Right. So. So the next whatever 12, 24 months is about understanding and executing on go to market. Go to market in these new verticals.

Christophe Rimann [00:51:35]:
Exactly, exactly that. Yeah.

Luke Sophinos [00:51:36]:
Fascinating. Well, I'm, I'm, I'm rooting for you. I'm sure all our appreciate it too. It's a big, it's a big hairy problem and all of us it in some way shape or form. So yeah, I'm excited to see you guys, see you guys take it on.

Christophe Rimann [00:51:49]:
Thank you so much, Luke. I really appreciate it and thanks for the time as well.

Luke Sophinos [00:51:52]:
Awesome. Thanks for being here, man.