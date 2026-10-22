# Verticals: Scaling AI Services: Zero to $15B in a Year

Published: 2026-03-18
Type: podcast
Summary: Chris Hladczuk explains Hanover Park's human-reviewed AI fund administration, proprietary accounting system, bundled products, AUM-based pricing, and trust-driven customer selection.
Source URL: https://insights.euclid.vc/p/scaling-ai-services-zero-to-15b-in
Featured: Chris Hladczuk
Archive episode: 20
Source file: Episode 20 - Chris Hladczuk.txt
Date note: Date of the linked published episode page, not the recording or Drive upload date.
Transcript note: Automated transcript preserved as supplied; names and speaker labels may contain transcription errors.

## Transcript

Luke Sophinos [00:00:00]:
What if the biggest AI unlock is not replacing humans, but it's making all the invisible behind-the-scenes work vanish so your customers get trust and white-glove service at machine speed? In today's episode, Nick and I go straight into the hardest problem in AI automation, trust. Because in finance, it's not just are your numbers right? It's when you're frazzled, can you call someone who's actually got your back? Meet Chris Hadzuk, founder of Hanover Park. He's going to walk us through his new company, which is building vertical AI for fund administration. They're AI agents that automate all the work that you don't see so real humans can deliver the advisory and the service you do. He breaks down why fund data is so stale by design, why accuracy is non-negotiable, and how their model is human-in-the-loop. AI prepares, humans review, speed goes up, trust doesn't break. And what's fascinating about him is 2 years ago, he went on a podcast and said B2B SaaS is dead. Maybe he was onto something.

Luke Sophinos [00:00:56]:
Let's find out. Chris, thanks for being here, man.

 Chris Hladczuk [00:01:02]:
I can't wait. Let's do this. We can talk about how B2B SaaS is dead again. Let's do this.

Nic Poulos [00:01:06]:
All right.

Luke Sophinos [00:01:07]:
Yeah, this report is going around and it's, it's shocked the markets. I was, I was playing paddle with my buddy just the other day who's in public equities at Goldman and he was, he was freaking out. He's like, I need to talk to you about software. What's happening? So. We'll, we'll get there, but first, why don't you tell us a little bit about you, your journey, your background, and then what you're building at Hanover.

 Chris Hladczuk [00:01:30]:
Great. Yeah, I was a Goldman investment banker, actually got into startups writing on the internet where I met Luke, built a following of a few hundred thousand people there writing about startups and tech. I was writing like deep dives on like why Disney is a cult, why every great business is a cult while I was a college kid. Um, was chief revenue officer at a fintech business, got us from like 10 to 1,000 customers doing business banking. I started Hanover Park in 2024. We just raised a $27 million Series A. Think about fund admin is like the, the thing that quietly powers $100 trillion of global assets out there. You have like the very boring financial reporting, accounting, investor portal, all the things that like make the plumbing work for the largest funds in the world as well as venture funds as well.

 Chris Hladczuk [00:02:10]:
And so our goal is replace the human duct tape with, with an ERP purpose-built for the fund that we built. AI agents that prepare work and then humans review the work. And so you got, you know, services plus software mix here.

Luke Sophinos [00:02:22]:
I love it. And I was joking before, I said this might be a pitch for Nick who—

 Chris Hladczuk [00:02:26]:
Yeah, Nick. He—

Nic Poulos [00:02:27]:
yeah.

 Chris Hladczuk [00:02:27]:
What's going on, Nick? Why haven't we switched over yet? We should keep that out.

Nic Poulos [00:02:31]:
Yeah. Well, you know, hey, we've got, got 45 minutes here to pitch.

Luke Sophinos [00:02:34]:
So, so Chris, if you can tell us a little bit about, for, you know, a lot of our listeners, obviously investors, mostly vertical software and AI founders. Like, tell us what it's like in a fund today to do this, maybe some of the workflows, and then what you're doing under the hood at Hanover.

 Chris Hladczuk [00:02:54]:
Yeah, so if you think about like something very simple like a capital call, like, hey, I'm a fund like Nick's, I want to call $10 million, 10% of my fund, that requires Nick sending an email to a human, that human then creating an Excel file, that Excel file going back over email, and then a bunch of review processes back and forth. And there's probably like 10, 20, 30 different workflows that are very similar. When you think about everything from capital activity to financial reporting to all this kind of stuff. And so our thesis was there's a lot of companies that Nick knows and, and others that are like, hey, I'm gonna just like plug an agent on top of like an existing accounting system. And so QuickBooks or something else. The problem with that approach, in my opinion, we've seen this firsthand now across, and we've probably hit 10,000 agent actions like in production with a bunch of customers on platform. Is that the core system of record, like the ERP for the fund, determines actually what the agents can do. And so if you're confused with the underlying system of record, it's really challenging to automate things on top.

 Chris Hladczuk [00:03:54]:
And so, you know, our objective was like, how do we take something that a human would do to click buttons and how do we have an agent do that to like prepare the work for like an expert fund accountant to review? Um, and so that's kind of like state of the world today, very Excel-driven, very email-heavy. Using other accounting systems and stitching together a bunch of different tools. 'Cause these businesses are primarily services, low, you know, low leverage, like high human services businesses. I mean, so we vertically integrated from like the ERP for the fund plus the agent stack plus the humans on top.

Luke Sophinos [00:04:23]:
Sounds like a good use case for, for AI, someone would say.

Nic Poulos [00:04:29]:
So Chris, tons of, tons of questions here, but maybe should we just get a little bit of backstory? Like how did you find yourself in this exciting, dynamic world of fund administration.

 Chris Hladczuk [00:04:40]:
Yeah, yeah, very, very exciting. So I have a friend in the space and he was like, hey, have you heard of this fund admin thing? I was like, no, what is this? And so I literally cold called, cold emailed, cold DM'd on Twitter and LinkedIn, and I got on calls with 50 different CFOs like this and be like, hey, what do you think about your fund admin? Was opening question. Half of them started cursing at me immediately and it was like, oh, that's interesting that you desperately hate this vendor. And I was like, oh, well, how much are you paying them? And they would say an astronomical number that you would be very surprised to hear, like millions of dollars a year. And I was like, well, that's weird that this is your most important vendor. You pay them all this money, you desperately hate them, and all of that data is 10 times more valuable with AI than it was before. Right? And so, you know, it's like own the data, own everything, right? It was kind of our thesis. And so that's kind of how we got into it.

 Chris Hladczuk [00:05:28]:
Then it was just like, how do you solve the cold start problem of convincing you know, a $500 million venture fund to leave their most important vendor that all their LPs log into every day to an unknown company called Annover Park, right? That was, that was the bigger challenge. And so it was a huge cold start problem. And now we're about $15 billion of assets on platform serving, you know, a bunch of different venture and private equity funds.

Nic Poulos [00:05:51]:
Very interesting. So Chris, one, one challenge I think about in this world is something I think about is the trust problem. So if you guys think about, you know, why you pay your, you know, your accountant, your private wealth advisor, your tax guy. Yes, of course you want it to be accurate. You know, you want all the numbers to be right, but you also want somebody who you trust, who you can call, you know, when you're not tracking the numbers and you're frazzled, you know, you can call up Joe or Kim or whoever it is and you know, they've got your back, right? And in a lot of ways, I think that's been a challenge for some other areas, right? Like at the end of the day, it can get in the way of distribution, but like, in a world where, you know, you're at Hanover Park trying to automate everything, how do you, how do you deal with that?

 Chris Hladczuk [00:06:38]:
Yeah, I kind of think about it as automate the work you don't see so we can provide high-level advisory work and white glove service for the things you do see. And so, you know, there's a few structural pieces today. If I think about the average fund admin, they are literally reconciling cash, which is the simplest and like most transactional layer, on a monthly, quarterly, maybe even longer basis, meaning like the end result is your data's super stale and you have no idea what's going on in your fund, right? You literally have no clue what your performance metrics are after you get a 10x markup from the deal you did 2 days ago, right? So our goal was how do we build AI agents to automate that core work? And so our team isn't scrambling around saying, hey, I didn't reconcile cash for that specific day, month, week, or quarter. What that enables us to do is say, okay, now because I don't need an army of humans clicking buttons to reconcile cash, I can have higher quality people in your account. I can pay them more structurally. I can give them equity in the business, whereas a lot of other fund admins don't. And that enables us to have a higher caliber accountant. Since it's like, you know, we've had a customer say, hey, it feels like I have 25 people on my account when they have like 2, right? And so the goal is not replace the human.

 Chris Hladczuk [00:07:45]:
It's like do all the low-level work you don't see to unlock value for the end customer and then have, you know, the well-trained human on top that is a CPA that can think deeply about the problem.

Nic Poulos [00:07:56]:
Do you, I mean, to that end, I, you know, what I, what I have seen as a problem, you know, specifically as a, as a fund manager who's used fund admins, is sometimes when these models try to scale and they get rid of the, hey, you know that Joe personally, and you switch it out with you, Claudette, whatever, it becomes a little impersonal, and for context, there's lots, I, I do you guys just look to build trust with an individual or there are no names?

 Chris Hladczuk [00:08:28]:
I have a lot of thoughts on that. So we have a dedicated team on your account, which I think is relatively rare, right? We've done a few things that have been critical. One is we've been very, you know, customer selection focused. And so today we're not really taking funds sub $100 million. Obviously the ACVs are relevant there when you can actually make the model work. If you're a $500 million fund paying X dollars, so One being like mid-market enterprise focused on customer selection side and being super thoughtful about that. And that, that's kind of been like a huge component of it. The second piece is we want to be where our customers are.

 Chris Hladczuk [00:08:58]:
I think, you know, there's a lot of other providers out there that say, hey, I'm going to force you into a 2018 SaaS product to make you click 7 buttons. I don't think that's what the CFO wants. Right. So we've built a lot of things like email agents where you can basically delegate to us like you're delegating to a human. and then our agents are actually actioning on creating tasks, proposing journal entries, executing on top of our ERP for the fund, which actually makes the customer like, literally someone called me who switched over from a previous fund admin and was like, how did that happen in 6 minutes? That was crazy, right? But a human literally had everything queued and all the human did was approve and reply back automatically. And so it's a win-win both from our services delivery side as well as better for the end customer, which is kind of the, the Goldilocks zone that we're looking for. So I think those are the two buckets. Customer selection be where your customers are in terms of being able to delegate to us.

 Chris Hladczuk [00:09:47]:
Because at the end of the day, like what they care about is like the 1 or 2 people where there's a complex edge case where you're like, this weird LPA term that our lawyers thought, what do you think? That's what we're trying to like add value on, on the services side.

Luke Sophinos [00:10:01]:
Is, is, can this be, so can this be venture scale? I'm sure you get that question all the time, right? Like that's one of the biggest problems all of our listeners who are founders going after, you know, one market with their, offering face. And when you slice up to, hey, we gotta just do mid-market and enterprise funds, like talk to me about kind of the business model and how that leads into, because I know Chris and Chris is like, you know, I'm taking over the world mentality.

 Chris Hladczuk [00:10:26]:
He's been that way.

Luke Sophinos [00:10:27]:
And I know you are for something that isn't multi-asset.

 Chris Hladczuk [00:10:30]:
Uh, I, uh, SS&C is a $20 billion public company today, right? There's many, many players over a billion dollars of revenue. There's $100 trillion of global assets, call it $50 billion of revenue out there. And that's just getting started. When we think about the core fund out and execution, then when we think about all of the other adjacencies, owning all the software tool spend for the investment firm, owning tax and all these other modules, like this could be a $50 billion plus company, right? And so we, we, we raised a $27 million Series A led by Emergence Capital. Jake Saper joined the board. Jake's been like the guy who invented AI-native services, which is why we picked him as a partner in the space. And they, you know, their investment thesis was this could be a Viva-like opportunity if executed correctly. Obviously Viva being the largest vertical software player, they invest in the Series A, uh, Viva.

 Chris Hladczuk [00:11:16]:
And so that's kind of how I think about it. Obviously it's a crawl, walk, run though. I do not have, like I tell the team every day, egoless execution. I, you have to have some sort of ego and confidence to think we can build something that big, but low ego in terms of like day-to-day execution. And so that's why we started with venture and we're obviously expanding to other asset classes.

Luke Sophinos [00:11:33]:
You have this, this very controversial, it's, well, I guess it's not controversial now. It was controversial when you, when you told, told it to me 2 years ago, which is like B2B SaaS is dead. Like unpack that for me and then unpack that within your specific model.

 Chris Hladczuk [00:11:47]:
So, so in September '24, I went on Turner Novak's podcast, The Peel, and I literally said B2B SaaS is dead. Here's why. And everyone told me like, you're an idiot. Do not say this. What are you talking about? All this kind of stuff. And now it seems like with Claude Nanthropic that I'm not an idiot, right? That this actually makes a lot of sense. And so what I kind of think about is What are the model providers not going to do? And how, if the ability to build software becomes easier, how do you not commoditize the layer that's an application layer? And so there's a lot of verticals that I'm not going to point fingers at where it's finance or some other adjacency where it's really just Opus 4.6 to Opus 5.6 away from execution, where it already has context in memory. And so for us, the way we thought about like the competitive positioning here was I am quite confident, and maybe I'll look dumb in 2 years, that OpenAI or Anthropic does not want to build a fund admin services company that does accounting for Nick.

 Chris Hladczuk [00:12:39]:
Pretty confident of that. Even if they can do the core, like, I don't think they want to be a services business that does fund accounting work. I don't think they want to build an ERP for the fund because a lot of the value, in my opinion, like the vertical integration of owning the core ERP, like AI agents are just clicking buttons on top of it, right? Like that's not the value layer in my opinion, right? Just enables us to scale a little bit way more efficiently. And so that's kind of how I think about it of like the, the AI native services trend of like sell outcome, meaning like do accounting, not sell software to accounting firms, I think is more interesting and less potential disruption risk.

Luke Sophinos [00:13:12]:
You get value then, like that's, that's one thing I know a lot of people are grappling with. I think wrapping services around, you know, AI and technology and specifically making that vertical focus, and then you add in this compliance layer, that's probably a huge value prop on top like that. That's a, I think that's the right kind of thinking around moats in, in this new world. But the question I always, you know, get asked founders and I have a hard time kind of thinking through is, is, okay, are you valued like a services firm? Are you valued like a software firm? Like how does this play out?

 Chris Hladczuk [00:13:44]:
I think scalability and gross margin is really the way I think about it. It's like if we have gross margins at the limit that are akin to a vertical software business or equivalent, like we should be valued as such. If we do not and it's not as scalable, right, it's not a repeatable motion, then it's obviously more of a service business. So I think those are like the bifurcation in my head of like, okay, what does this look like at scale? Like Hanover Park at $10 billion of revenue, what does that look like from a scalability perspective? And so that, that's kind of how I think about it. And then for us to like part of the key value prop is like And I'm— Nick, Nick said he just switched recently to a fund admin. I'm not going to name names here on this, on this call, but like, I'm— the, the just selling fund admin standalone, I think, is not a compelling pitch after I've talked to hundreds and hundreds of CFOs. It's how do I bundle in these things alongside fund admin, weaponizing the data that only I have access to. And so anytime Nick does a deal, he's going to give it to us because we have to book the accounting.

 Chris Hladczuk [00:14:43]:
We get— we can AI parcel the legal docs, the cap tables, the KPIs, the board decks, and all the data that we can weaponize around the core system of record layer. And so that means now we're bundling in 3 tools you buy separately that aren't very good anyway in for free alongside core fund admin services. So that's kind of how I think about this like bundle approach, but like with the weapon as you're going to pay a fund admin anyway.

Nic Poulos [00:15:04]:
I would add that I would, I would almost add, Chris, a third leg of that. So, I mean, you mentioned scalability and margin profile, very important. I think revenue quality also really matters in terms of how these businesses are valued.

 Chris Hladczuk [00:15:16]:
My number one North Star is not actually around NPS. Yes, it's around every customer being what I call a raving fan. Um, that's insanely hard in our space, by the way. Nick is going to hate me very quickly and very easily. And like, making sure someone's a raving fan is very challenging. So that's why I've been super disciplined, I think, versus typical vertical software. You can be like, just sell it a million times, have a million customers. I'm actually not doing that.

 Chris Hladczuk [00:15:38]:
I'm turning away people left and right that aren't the right fit. I'm being super disciplined about customer selection given how critical it is there.

Nic Poulos [00:15:46]:
I think that's smart because it's somewhat like the CISO problem. It's like when you're doing your job really well, I probably don't think about you that much. You know, when you're doing your job poorly, I hate you passionately. You know, like it comes at the worst times.

 Chris Hladczuk [00:16:04]:
It's actually funny you say that. I have a bunch of thoughts on it because that's the problem with fund admin, right? It's like basically it's like offensive line in football. No one cares about you until someone gets sacked legitimately, right? And so what we basically said is the 3 elements of raving fan is incredible onboarding. That's very challenging given how, you know, complex data is. Second is like 99.9% accurate, super fast services delivery. And then the third is like jaw-dropping AI-native product experiences. And I actually don't think you can get away with two without three, given that like we're gonna launch an MCP server next week where literally you're gonna have every single piece of data in your firm's history and you'll be able to generate any sort of customized PDF report, anything when you go pitch Harvard for the next the next fund, right? So that's magical, right? No other fund admin can offer that. And so how do we deliver those tied to the core data that we control?

Nic Poulos [00:16:55]:
What did— so before we kind of move on from the, the, the kind of margin business model piece, like what, what margin do you target and how do you think about balancing, you know, humans versus automation?

 Chris Hladczuk [00:17:09]:
Yeah, I'm not going to say that one publicly.

Nic Poulos [00:17:12]:
Well, fair, fair. Well, I guess any broader thoughts around like, you know, in this world of AI services, what's healthy? I mean, even pure application layer non-services are probably, you know, looking at at least 5 to 10% that's going to go to the model companies. So what's reasonable these days?

 Chris Hladczuk [00:17:32]:
I think about like, what's the combo of like, obviously like high quality, like I call it like white glove service model, which is very like the old school way, which is like high-quality services with like amazing fund accountants. Like I say, we're building the Navy SEALs of fund accounting. I don't think those 4 words have ever literally ever been said together in the same sentence. And so it's like Navy SEALs of fund accounting meets like a bunch of agents that are doing core work that you don't see in the background. And so we're, we're seeing a lot of pull from, you know, like I tell the team all the time, like I don't care what our Anthropic and OpenAI bills are this month. I care more deeply about like, is this the scalable thing that's going to enable the better customer experience? And so we're like pretty experience focused, not margin focused right now.

Luke Sophinos [00:18:14]:
Chris, can we unpack a little bit of, of, of go-to-market and what that looks like? Because it's, you know, this is obviously a kind of a big switchover situation, you know, to move off of a fund admin. So I'm just curious, like, how do you think about growth rate? How fast are you guys growing? If you're willing to share that, um, it'd be super helpful for the audience.

 Chris Hladczuk [00:18:36]:
Yeah, we went $1 to $15 billion of assets in the past 12 months. And so that's kind of the headline number on assets, which we're sharing publicly. I joke with people when we're on like a first call, I'm like, it's not like I'm asking you to get married on the first date. It's actually crazy to switch to me, especially like when it's 1 or 2 funds, it's actually not a big deal, right? Like it's, it's not that big of a switch when it's, hey, I'm going to rip out 7 funds with 22 entities with 37 this and then 10 SPVs on top and then all this fun stuff like You have to look me in the eyes and say like, do I trust this person? And like that from a migration implementation perspective is critical. And so I think it's, it's less selling and more expectation setting of just like, here's what we do have and here's what we don't have. And the last, like I tell people all the time, I'd rather you not become a customer than become an unhappy customer in 4 months. Right. And so we've been pretty laser focused and that obviously builds a lot more trust than like randomly saying, join my thing.

 Chris Hladczuk [00:19:34]:
And then, you know, them thinking it's AI, but it's not AI if it's overpromise, underdeliver.

Luke Sophinos [00:19:39]:
Let's go deeper here because you're like, you're the maniac on the mission, which is what I've always loved about you. Like, you know, you tweet about sleeping at their offices saying, I'll come move in for a week until this thing is launched. Like, tell the founders listening like what this actually takes and how long is the founder-led sales motion going to be running here?

 Chris Hladczuk [00:20:01]:
Yeah, we need to get out of founder-led sales motion. I'm on 7 jobs right now at this point. We're a little too big for this, honestly, but I like staying close to that. So, so a few things. One is like, I literally, at the drop of a hat, I will get a text message from a CFO being like, hey, my GP Nick, Nick is telling me like, I don't know about Hanover Park and I don't know about this whole thing. I'll literally call him immediately, pick up the phone today and book a flight and I'll be there tomorrow morning. Um, and then we'll go lock ourselves in his office for 4 hours and we'll get to work. Right? So I think like when it's this critical, like it is the most important vendor from a dollar perspective, from like any metric that a firm has.

 Chris Hladczuk [00:20:37]:
If I'm not willing to get on a flight to talk to you and spend 2 hours in a room, like why would you— I be the right partner for the next 10 years really, which is how long these decisions last? And so I think, and you always get on the plane, which I think I coined on Twitter like 2 years ago, and then everyone else has then said always get on a plane. So I think I can say I'm the inventor of that phrase, but I think the, the core, like, always get on the plane. This is a long sales process that's like very, very high stress for the buyer, which is the CFO, right? Typically I'm not selling directly to GP like Nick, depending on the size, right? So it's like buyer, CFO, CFO, their job is on the line. This is obviously critical for them. And so the like, I'm going to get on the plane and fly to you today for the next 4 hours, um, is fun. I have a few fun stories on that.

Luke Sophinos [00:21:25]:
How do you—

Nic Poulos [00:21:26]:
so maybe going back to the AI services, and by the way, I think we glossed over it, but congrats on the Series A. Jake is, Jake is a great partner. I mean, Emergence is great, but you know, I've known Jake and his colleagues there for a long time, so kudos. And he has done a lot of great thinking around AI services. I, you know, A challenge I sometimes have with AI services, or at least some conception of it, is the following. If you are viewed as a third-party vendor and AI allows you to cut out some sort of internal costs, recapture margin, grow faster, that's all great. But that same cost advantage can apply to anyone else who does want to provide that service. And so eventually, will will the, the kind of pricing power that you have get competed down? Or in your case, it sounds like maybe there is some other aspect of defensibility under the hood there.

 Chris Hladczuk [00:22:30]:
Yeah, I think a lot about this actually, all the time. It's like, as AI is doing more work, what happens, right? So the, the approach we've taken, which is definitely evolving in real time, is I am going to bundle in more products, right? Which is what we currently do today. And so Every single firm on the planet at scale has a portfolio management tool and a portfolio monitoring tool. I need to figure out how my companies are doing, right? And you have evaluation service, then you have a tax provider, then you have an LP portal. I mean, you just got like pick names out of a hat, which is like the bunch of things that you have. And so what I've said is, hey, we're going to be 10x better at fund admin. Here's how we do it, right? Like, here's actually what we're doing under the hood. Give me everything end to end.

 Chris Hladczuk [00:23:09]:
And then also because of this advantage of like the ERP for the fund. This is why I like disagree with any approaches that are like using another ERP, white labeling something else on top and then trying to say AI is on top. I don't think that works. And we can talk about that, which is like I'm going to just bundle in more, right? And so when you think about like your overall cost across all of your vendors, the ROI on dollars is massive, right? It's kind of how we've approached it.

Nic Poulos [00:23:33]:
How do you view, you know, one thing we were talking about in I think our last, our last pod is really just the kind of decline of switching costs, right? And in a world where you can export your data and reformatting your data to port it into a new system is trivial with cloud code. What do you guys see as switching costs outside of, of course, you're the best product and you have good loyalty?

 Chris Hladczuk [00:24:02]:
Yeah, I love the Jeff Bezos quote, which I'm going to butcher here, which is like, I live in constant fear of my customers, not, you know, that they're going to leave me for somebody else. And like, you know, I actually think every single— like, I literally told our team, I said, I don't even care if we never get another sale. I just want every customer to be a raving fan. Like, and that's a little bit exaggeration, but not crazy, right? In terms of how we think about it. So I think it's like, assume my customer can leave me instantly, but I am in a place where, you know, there is obviously higher switching costs and, you know, it is a massive move over to, to a place like Hanover Park. And so I don't know, I'm like healthily skeptical. I don't know how that impacts the long term. Say I can click two buttons and migrate everything, what happens, right? Obviously we have an LP portal that people are logging into.

 Chris Hladczuk [00:24:45]:
All of your LPs are also logging into Hanover Park. There's about 10,000 today, including a lot of large institutions. And so that's like, are you going to tell them you're switching next month? That would be another entertaining kind of piece, but I live in the healthy skepticism and fear of, you know, someone else building something better that my customers will get more value from. Yep.

Nic Poulos [00:25:03]:
No, totally fair.

Luke Sophinos [00:25:04]:
Have you felt that impact at all, Chris? Like, have you felt any sort of churn impact since the CloudCodes of the world have come out? I, I assume not in your specific vertical, but—

 Chris Hladczuk [00:25:15]:
Up— or like, not, not yet. Yeah, it, it's diff— I think it's more like If we were just building software, right? It's like there's software plus services plus output plus the accounting deliver— like there's a lot there where I haven't— like I've seen all the Cloud Code stuff and I've been like, oh, this is amazing. Our team is using it all day long. Literally, I have ops people who've never written a line of code in their life, literally like building stuff in Cloud Code. But I think more about how does that enable us to supercharge migration in a way that changes things because of how painful this is. Like For audience context, I'm basically telling someone, take the most complex financial institutions in the world, take 20 years of data that's completely terribly kept, and move all of that to— that's insane. So like the ability for on our side to reduce switching costs for people that if I could tell a CFO, click this button and move over, they would, right? That, that's kind of how I think about it on offense versus defense.

Luke Sophinos [00:26:07]:
All right, we're gonna take a short break to give a big shout out to our sponsor, Parafin. They're the ones who make Verticals possible.

 Chris Hladczuk [00:26:14]:
Possible.

Luke Sophinos [00:26:14]:
If you haven't heard of Parafin, go check them out. They build embedded finance tools that really help your merchants grow. They're the leader in vertical software and embedded finance. And so if you're building in the space, haven't explored Parafin yet, go check them out. They've got embedded credit, embedded spending, a lot of different tools to really drive revenue growth, drive TAM expansion, and really improve retention. So big shout out to Parafin. Go check them out. Now back to the episode.

Luke Sophinos [00:26:41]:
Yeah, we had an interesting founder a couple weeks ago who literally has created an AI agent that goes into whoever they're, when they're on a sales demo, they're on Zoom and they literally say, hey, download this AI agent on your desktop real quick. And it goes into the freaking legacy system of record, pulls it out into their UI, and then they can see, hey, we've solved the, the rip and replace thing that you've been scared about for decades at this point. and they can actually see their data like in this, you know, beautiful kind of AI native application. And it blew me away. I'm, I'm sure that's harder in your world, but most creative kind of, you know, action I've seen to pull out, the legacy vendors.

 Chris Hladczuk [00:27:21]:
I, I love this. And like, we've, this is something I'm investing heavily in right now, which is like, how do we build? I, I've been saying this for literally a year. My team laughs at me, by the way, when I say this, 'cause no one believes me. But I say I'm building a one-click migration feature. Now you can say offense or defense, right? In a lot of ways, but like offense, if I could click one button and migration, we would not have $15 billion. We'd have many, many multiples of $15 billion of assets on platform today, like $100 billion probably. And so it's like, it's really a constraint. And I'm like, just like pure Elon, what is the limiting factor in the business? It's like, this is a massive limiting factor for us.

 Chris Hladczuk [00:27:55]:
And so we're investing right now. We've tried a bunch of different tools that do this. No one's been good yet. Given the complexity of the data, but we're trying to build our own right now.

Nic Poulos [00:28:04]:
Yeah, I think it's interesting because historically people look at systems of record and say, well, the defensibility is that getting your data off of there and moving it somewhere else is going to be difficult. It's too much of a pain. You know, I, I think now it's really more so this decision layer. Some people are calling it the context graph where, you know, like what matters to me as a manager is that like very small chance that an LP has a terrible experience or they get wrong numbers or, you know, something is incorrect on my taxes. Like that's unforgivable and worth every penny that's paid to a great service like Annover Park. LP portal, like I could see a future in which I would want an API to Annover Park so I can build my own. And the fact that you enable that, like, I'll give you an example. I just switched CRMs.

Nic Poulos [00:28:57]:
I won't name names, but specifically because one offered like really strong open APIs and the other didn't. I wanted that. That doesn't mean I didn't value this, the, the new CRM, right? It just means like, you know, switching costs are changing. So like, I think you guys have a really interesting opportunity on that context graph, uh, you know, kind of barrier of like, I want to know what I should be doing with my LPs or filings or whatever.

 Chris Hladczuk [00:29:24]:
So excited about MCP, right? Like no one in our space has even considered launching this 'cause it's so old school, right? We have, we have, they call engineering IT in my industry, right? Like they, they really, it's like so old school. It's crazy. Like literally people call it, they don't call it a product or a platform. They call it a system, like literally, right? And so because it's that old school, no one even has APIs. And so MCP is like groundbreaking because it gives a GP, it gives a CFO like the creativity to take action on core data that sits inside Amberpark. And so we're pretty excited. We're going to launch that in the next like week or so. And so by the time this airs, I—

Nic Poulos [00:29:57]:
so that's a, it's a good segue. I wanted to, if cool by you, Luca, I want to talk about tech stack for a second because I think this is actually a really interesting, you know, kind of foil for talking about the hallucination question, right? So I feel like with you guys, one, you need to abstract a ton of information. It's very complex and sometimes bespoke. You need to have an ontology for what that information means. But then you also, you know, in the case of your MSPs, you need to be able to provide inference, whether that's for your own, you know, employees that want to answer questions Right. And like one error along the way would be devastating. So how do you guys, like, where do you involve LLMs? Where don't you? Are you involving any more traditional, like enterprise schemas or, you know, enterprise search?

 Chris Hladczuk [00:30:53]:
Yeah, great question. We have like a traditional search and we also have like kind of like the AI search in different ways. But, but like the way I kind of think about it is like for things that are critical action, it's the paradigm is AI prepare, human review, right? And so if you think, let's take like something super trivial, right? Uh, Nick sends a bill that he wants to pay for Goodwin Legal invoices. He forwards that bill up. Other providers would say, I'm going to force Nick to literally log into some platform to do some work. I think that's insane, right? And so you can delegate to me like you're delegating to a human and say, hey, you know, whatever at hannoverpark.com. AI agent reads the email, AI agent does a bunch of work in the background, human reviews it. And so you get best of both worlds where you get speed and accuracy increase because you don't have a human running around doing manual work input.

 Chris Hladczuk [00:31:36]:
And so I kind of think about that paradigm, right? Because we're obviously delivering the services, right? Not just the software. And so we have the liberty, I call it, and like the freedom to have a human in the loop, but still deliver the better customer experience on that side. But given like what we do is trust, right? Like the worst pitch ever, and trust me, is literally like, hey CFO, it's AI. That's not a good pitch. Trust me. I don't actually say the word AI very much. And so I think that's the critical paradigm of like, depending on what it is, where it's speed versus accuracy. And in our industry, mostly accuracy matters.

 Chris Hladczuk [00:32:11]:
There are places where speed matters. For example, you forward a board deck to us, we parse it in real time versus something that's accounting focused.

Luke Sophinos [00:32:20]:
On that thread, Chris, I'm curious, and this is just from the, like a, the founder seat, is I remember at my company I would get hit up every quarter by you know, the CFO asking and he would reach out to my CFO and then my CFO would be busy and then he'd eventually reach out to me after he tried my CFO 2 times. And we had that across like 8 different venture funds that had backed us. Right. And it was a total pain in the ass from the, from the founder seat when we're like, just look at the, like we send the board decks out, like just look at the board decks. I, I, I, on your website, you guys are doing some, some of this, like how are you automating that piece of it?

 Chris Hladczuk [00:33:00]:
Yeah, we built— so the way I kind of think about the portfolio tooling stack, and this is nitty-gritty, every listener, you can turn your headphones off right now. This is the most boring thing ever. I love it though, so it's good. The 3L fund—

Luke Sophinos [00:33:11]:
our listeners love boring, by the way.

Nic Poulos [00:33:13]:
They would.

 Chris Hladczuk [00:33:13]:
Yeah, this is, this is— I know it's not flooring software, but it's, it's a step above. So two things I think about, I think there's like, I call it like old school 2018 SaaS paradigm, which is what you get asked. Hey, here's a form. It's a glorified Google form. Put numbers in. That turns into something that you can analyze your data by. That's super old school. I think that's kind of going away, but some people still do it that have more control.

 Chris Hladczuk [00:33:36]:
Like if you're a private equity firm or you're— you own 40% of a business, for example, versus like a seed check, then I call it the new school way, which is like, hey, you just send whatever founder email update you send every month or every quarter or any board deck and you just send it to your investors. And like Hanover Park KPI reconciliation agent is what I call it, which basically pulls out context from the board deck or the email update or any of the fun stuff there. And then all of that then pre-populates and then cross-references again against the old school SaaS version that we also offer, right? So it's like multiple different sources running reconciliation against. And so I would say a good chunk of our customers, like they don't even do the KPI forms anymore. They just like have someone send them an email and call it a day.

Nic Poulos [00:34:20]:
Chris, how did you— so, and I'm maybe going a little bit back to go-to-market. Like in this world, as you said, it's not necessarily a, we want to adopt it just because it's sexy AI, right? Like how did you get trust initially? Because this is very much a thing where, you know, again, speaking as a fund manager, you're kind of just like you're asking friends, you're trying to like suss out their backgrounds, but you really don't know until you start using it. And so, you know, you said you went $1 to $15 billion. Like how did that happen? Was it referrals?

Luke Sophinos [00:34:57]:
So what's the $0 to $1 story on this?

 Chris Hladczuk [00:35:00]:
Yeah. Funny. Handful of customers, one being obviously our seed investor became a customer. And so I'm not going to, you know, that, that was like critical day zero, you know, customer base.

Nic Poulos [00:35:09]:
You got to just keep raising money is the answer.

Luke Sophinos [00:35:12]:
Yeah.

 Chris Hladczuk [00:35:12]:
By the way, that keeps happening, by the way. People are like, I'll become a— I was like, come on, guys, I don't do the quid pro quo game. So, so, so, so it doesn't happen. So yeah, a little bit of the Cold Star was, was the seed customer, but like honestly, until probably customer like maybe, maybe like 5 billion, it was still very uphill and it was like very, very uphill, meaning like very challenging. So much embedded trust, you know, LP institutional. Like I can go detailed on operational due diligence calls, which are Nick would find entertaining, right? Like I'm on these calls, right? Like this is, and for Luke's benefit, like this is when LPs are diligencing whether they're going to invest in your fund. A fund admin is actually a core piece of that, right? In terms of like, what is your core accounting stack and accounting layer? And like, how do we ensure that, you know, your PCAPs and financials are delivered properly? So we've gone very deep on that front and kind of think about that stuff. And so the zero to one was get a few core investors, convince people to take a chance.

 Chris Hladczuk [00:36:08]:
Right on what we're doing, which was, hey, I need a wedge product that's super interesting, not just fund admin. That's why I'm— Nick switched. I don't even want to talk about this on this, on this call. But like, you know, the wedge product for us was the portfolio tooling, right? Which is like, I can offer a venture fund a portfolio management that AI doc extracts when none of my competitors even think about that.

Luke Sophinos [00:36:25]:
It's actually such a good wedge product because it's so simple and it's a pain in the ass for all of them.

 Chris Hladczuk [00:36:29]:
But we actually didn't unbundle it though. That's what's actually interesting. So like, I am Mr. Bundling, like I literally hate the word unbundle. I will literally never sell the standalone product of Portfolio Tools, which is probably surprising and pretty contrarian because my, my thesis on this is that when you unbundle, the products are actually worse. And so now I'm going to just deliver you a bad portfolio experience. That's not going to be great, right? You're not going to switch over fund admins now versus everything works better together.

Luke Sophinos [00:36:55]:
Well, let's pause on that because I'm, I'm, I disagree with you. Like I feel like, sure. Why, why would it be worse? I mean, that's, that's a pain in the ass problem. Could, like, couldn't it, wouldn't it be valuable to have every single fund on Hanover Park and then you're just cross-selling them over time into, it's funny, my one, um, yeah, one of my best friends is, uh, the founder of a company called Prepare911.

 Chris Hladczuk [00:37:16]:
They just sold to Axon for $800 million. Um, Mike Chalmers, like one of my best friends, and they did this approach, which is what you're talking about, which was like, I'm gonna give the freemium away and then I'm gonna cross-sell across everything. And I think that's, valid for us. It's very specific to industry. The reason why people don't like the other portfolio tools is a lot around not having the core source of truth data that lives in the accounting system. So it's like, it's more nuanced for us, I'd say, than like a generalizable lesson of just like diagnosing that there's a problem with like this idea of a standalone tool and it can't drive the value that people really want. And so that's why we had to integrate together, because I think we'd fall into the same trap as why the standalone tools aren't as good.

Luke Sophinos [00:38:00]:
Yeah, it'd be easy to turn them to— I'm sure you could just move to the next one and race to the bottom in terms of pricing.

Nic Poulos [00:38:07]:
There's also like, if you— if the offering is based on information context you guys already have and it's a matter of like packaging and providing interface, there's an opportunity to say, well, X competitor offers this as an expensive add-on. Like this is part of the bundle and like, yeah, we're not cheap, but like we give you everything, right? So like the fund model, that's exactly what it is.

 Chris Hladczuk [00:38:31]:
Like the fund modeling. Yeah, that's exactly what it is.

Nic Poulos [00:38:33]:
You know, like that's like you said, the modeling, the fund modeling itself, is that something like Opus 7 is gonna be able to do? Probably. But like, again, that's not your moneymaker. That's just like a signal that like, We're premium and you don't have to like, we don't have to nickel and dime you. Now if you guys go into like, hey, we're going to give you like credit cards and banking and money movement, then sure, that's probably an upsell and you probably don't want to do that.

 Chris Hladczuk [00:39:00]:
But we're not doing banking. I'll put that on the record. We do do a lot of money movement though already. And so that's actually like a whole separate fun conversation, which like we're not making money on this purely for customer experience and we just think it's a better experience to have native in-app money movement than it is standalone. And that's more of like my every customer's a raving fan North Star versus like, yeah, what are like we don't we bundle everything today and that's been like a core focus.

Luke Sophinos [00:39:26]:
So Chris, are wedge products dead in the age of AI?

 Chris Hladczuk [00:39:30]:
Oh boy. I think like there's so many, there's so many products and features and companies in general that are just like features on top of core thing. And I'll be honest though, like my thinking has been pushed on this because like someone I would deeply respect, like a Brett Taylor, Right? Like what Sierra is doing is actually the anti-system of record. It's like, you don't need it. It doesn't matter. The agent can talk to any system of record and you happen to be the one that we are like, and like, by the way, he's a thousand times better of an operator than I am. And so what do I know? Right. And so like, you know, if Brett Taylor is thinking this way that like the system of record is less important, it's like what the agent context has, like that pushes my thinking on like how we need to think about this in terms of being intellectually honest.

 Chris Hladczuk [00:40:11]:
And so. That. But I think like the wedge product that like can be built quickly, that like might sell like a certain SKU and then be like something that people churn off of in 6 to 12 months, it just isn't the game that I think I can play well.

Nic Poulos [00:40:24]:
But like on the agent point, I mean, I buy that in a long-term sense, but I think anyone who has played around with agents that are handling complex multi-step decisioning, I think would probably agree that at this point in time, they're not to a point where they could handle something that is as, has as low of fault tolerance as fund admin. Do you agree with that or not?

 Chris Hladczuk [00:40:51]:
Fully agree. This is why, like, I think it's so funny and we're coming out with a launch video in March when this airs, which is me like duct taped to a chair, by the way, disrupting something with human duct tape, which is kind of entertaining. And so we're going to be a lot louder in March, part of, part of this release, but like, What's been interesting is I've been like, okay, every single person when we started the company told me specifically, hey, Chris, don't build a general ledger from scratch for the most complex fund accounting in the world. You're an idiot. Don't do this. You're dumb. Whatever. Every smart investor.

 Chris Hladczuk [00:41:20]:
I told them you're wrong. And because a lot of the value, in my opinion, is like really solid foundational ERP for the fund, and then the agent is like the cake on top that does the last 10% to click the buttons or do whatever the core work is. If the ERP can't do the core action though, it doesn't matter. Right? I mean, you talk like 100 examples on like the accounting front, but like that's kind of how we've approached it. And so for us it was like, without the ERP for the fund, what are you? You're just a UI on top of somebody else basically.

Luke Sophinos [00:41:50]:
Did you guys read this Sassini Twitter article that went crazy viral and it basically fast forwards in the 2028 and it just plays like I like, I didn't actually read it.

 Chris Hladczuk [00:42:01]:
I just saw 50 tweets that made me wanna throw my phone at the wall was basically how I was thinking about it.

Luke Sophinos [00:42:06]:
Yeah, basically just the summary is all the value gets moved into like the, a few, you know, AI companies and everything else is dead and white collar jobs are, you know, every, everybody's lost their job. It's basically like a doomsday view of what, you know, what could potentially happen. Like, less about the article, but more about just your specific view. I mean, it sounds like your view is like, hey, system of record is important, but it's probably not as valuable. What's more valuable is wrapping some level of services around it, some level of agents around it, some level of human in the loop to actually go and click the buttons. And what the customer really cares about is just the outcome. Like, is that a good summary of your view?

 Chris Hladczuk [00:42:53]:
I, I, yeah, I think software plus service. That's why I've been like AI-native services is the future of like what the next generation of great companies are. I think this is the business model shift, not, you know, a slightly better AI plus— like AI software companies are just software companies. There's nothing different about them, right, than any other company aside from they have more AI than anybody. Like, that doesn't seem different to me, right? So that's why I think like the disruption surface area in this is this wave is all around this AI-native services and like At the end of the day, what I tell customers all the time is like, I'll show them the GL and I'll be like, you don't care about this. What you care about is because I have this, I can automate all this stuff that makes your life 10 times better, gives you real-time data access and can act on all these other things. Like that's the outcome. But like the outcome starts from a bunch of like really boring core stuff that you don't actually see.

Luke Sophinos [00:43:40]:
So maybe the, you know, the AI rollups in buying services businesses you know, may have been the right, the right bet. I mean, not, you know, it doesn't—

 Chris Hladczuk [00:43:49]:
I actually have a lot of thoughts on that. We can talk about that. That's interesting. I have like, given our space, obviously there's a lot of activity in M&A in our space. I can, I have a lot of thoughts there if that's useful.

Luke Sophinos [00:43:58]:
Yeah. If we take out, well, let's take out the roll-up for a standpoint, but what if the software companies just eventually become AI-native services businesses and, and the services businesses, you know, who in a lot of industries are, are typically kind of more mom, mom and pop right? They're not running as intensely as like a venture-backed company or like maybe they're, they're at the most risk if you have AI, if you have the typical software company kind of moving downstream to, to take that on.

Nic Poulos [00:44:25]:
I don't know.

 Chris Hladczuk [00:44:27]:
I don't know. Like I'll say, I'll put my hand up saying I know very little. I don't know anything. But what I, my, my hot take behind that is like, I am very doubtful that like traditional B2B SaaS companies will become services companies. The entire way in which you approach the market is different. Like, I have fund accountants sitting 10 yards from me in New York City. Fund accountants have never joined a startup before, period. That is a very, very different recruiting function, operations.

 Chris Hladczuk [00:44:53]:
Like, it's so different than I have a bunch of engineers, salespeople, and designers in a room, right? And so I think like that would be very surprising from a cultural perspective if like now B2B SaaS companies have like a bunch of domain experts that they're hiring. Maybe though, I could be wrong.

Nic Poulos [00:45:09]:
I think it's like, like anything else, sometimes this argument around software versus services is a little bit more semantics than anything else. Like there's a lot of nuances here, right? Like the, the service you guys are providing, like it's, it's very nuanced. There's a lot of add-ons that you can have. It's, it can be very sticky based on like the lifetime of funds. That's very different than let's say like, here's a service where I'm gonna like create DEX for you or something, which like has no defensibility at all, right? So it's like sometimes I feel like this bifurcation is a little bit false where it's like, okay, I mean, sure, there are services that are completely indefensible. There's software that's indefensible. It's really more of a matter of like, you know, the underlying detail.

Luke Sophinos [00:45:55]:
Yeah, the world's trying to put everything into one bucket so that the public markets can actually understand it and their stock doesn't get hammered.

 Chris Hladczuk [00:46:01]:
Right.

Nic Poulos [00:46:02]:
Yeah. And I mean, like, also I would say you, while you have heavy services components, you do also have software elements in which you are like deeply ingrained internally within a business. And that's different than a lot of very external AI services, if you know what I mean, where, you know, you don't have that lock-in.

 Chris Hladczuk [00:46:25]:
Yeah, I have a lot.

Nic Poulos [00:46:25]:
I mean, yeah, I mean, I, I think, I think we're all in agreement, so I don't know, we're, we're appreciating—

 Chris Hladczuk [00:46:32]:
debate it out. Yeah, yeah. I agree with you.

Nic Poulos [00:46:35]:
That's awesome. Well, what would you say to a, like, I guess if there were, if you were giving advice to, to a new founder thinking about, you know, let's say going to a new category that is dominated by a legacy services provider, how would you think about, is this compelling or is this not?

 Chris Hladczuk [00:46:54]:
I literally, like, the only antidote I think is like upset, like the first 100 days of the company, right? Was literally like, obsessively talking to unlimited people in ecosystem. Like there is no antidote to talking to 1,000 CFOs. Literally, like, I don't care what shortcut you're trying, but it's like if you haven't talked to the customer obsessively over and over again, deeply understand what they hate, what they like, what is compelling. And like I call it like tap dancing. You're basically just stress testing an attempted assumption that I'm making about a market or about a product or like any time we launch something new, right? It's like what we talk to customers about. So I think that was one. The second is I talk, like, talk to a lot of people who it hasn't worked very well before, or like a lot of people in the ecosystem that don't think it can work and like, what are their underlying assumptions? And so like, it's more like a canvassing. It's like customer canvassing, previous attempt canvassing of why it didn't work, then canvassing of like current players and be like, why can you build something more compelling? Like, I'm not just like a guy who just sleeps in an office.

 Chris Hladczuk [00:47:52]:
Like, that's not that compelling over time though. It's pretty entertaining sometimes, but like, you know, that's kind of the, the canvassing. And so once I decided this was what I wanted to work on for the next decade plus, it was like I had 65 pages on every single competitor, every single thing they had, every single thing I thought I could do differently. And it was like a holistic sense of market. And so that was to me like what got me to conviction, just like an investor, right? But like I only have one thing to work on for 20 years and I don't believe in angel investing. So that's, that's the other thing.

Nic Poulos [00:48:24]:
I love it. I got you.

Luke Sophinos [00:48:25]:
We're running up on time here, so let's move to some rapid fire if we can, Chris. I'll kick it off, Nick, and then you can take us out. I've, I've got two quick questions for you to, to close out my Q&A here. Number one, biggest win so far, and then number two, like biggest mistake, something that, you know, you, you didn't do that you, you could do over again.

 Chris Hladczuk [00:48:49]:
Biggest win is basically when there's this massive institutional LP, uh, that I can't name obviously on this, on this, but like LP for the listener, limited partner, they invest their endowments, their, their banks, their et cetera. They, they called the CFO after they switched to us and said the CFO was scared. They were like, oh my God, why is this LP calling me? You know, Nick's going to be upset or whoever the GP ends up being. Literally they were like, I love this Hanover Park thing. I'm so glad you switched. That is like, just keep putting that in my ear over and over again for the rest of my life and I think I'll be fine. Um, is, is it, 'cause like my job is to make the CFO look good and special, right? And like, that is my customer. That's who I'm obsessed with.

 Chris Hladczuk [00:49:27]:
And so that was huge. Biggest loss, or what was it? Biggest like failure or loss? What was the exact question? Biggest mistake you made? Yeah. Mistake. Before we worked on Hanover Park, we worked on a completely different idea, uh, for like 2 months. And I basically realized this was the worst idea ever. Uh, and me and my co-founder were literally looking at each other 2 months in and be like, what are we doing? It was like completely different. What was the idea? Awful. Um, it was really like, and I've never said this publicly, it's like AI creator, like stuff with like videos and stuff like that.

 Chris Hladczuk [00:49:56]:
Like basically like I was a creator. I'd built a big following, obviously, where I know Luke from, from Twitter, LinkedIn, et cetera. And I was like, okay, I think like AI creators can be a thing with get and get views. I think that's actually not the worst idea. I was just the worst person in the world to execute on it. Like, it was literally awful. Like, I'm not a consumer guy. Yeah, yeah, exactly.

 Chris Hladczuk [00:50:15]:
So, so yeah, that was, that was an absolute failure. And we decided in 2 months it was the worst idea ever. I'm glad we did.

Nic Poulos [00:50:22]:
Can always bundle that in with fund admin later. Yeah, just toss it. Natural adjacency.

 Chris Hladczuk [00:50:26]:
Trying to market your new fund, right, Nick? This is it.

Nic Poulos [00:50:29]:
You're the king of bundles, right? Absolutely.

 Chris Hladczuk [00:50:32]:
Mr. Bundle. That's good.

Nic Poulos [00:50:33]:
All right, last, last rapid fire. What do you, like, as somebody who, you know, is building this, you know, software plus services plus AI business, what do you think right now is the, like, the biggest limitation of AI as it pertains to your business? Like, what would, if you could change one thing overnight tomorrow about the tech, what would it be?

 Chris Hladczuk [00:50:57]:
Yeah, I'm actually super excited about, like, long-running, long-horizon agents, which I don't know if you guys have followed this in the market, but it's like this concept of an agent that could run for hours and hours and days and days and like how that impacts for me specifically around how that impacts migration for us.

Nic Poulos [00:51:11]:
Right.

 Chris Hladczuk [00:51:11]:
So this is like very frontier of like basically take all the most complex financial day in the world, come back to me a week later. That as an idea of like a limiting factor right now, there's a lot of like frontier work that's being done there that we're monitoring pretty closely of like how we think about this could impact us in terms of being a big bottleneck for us in the next, call it 3 to 6 months.

Luke Sophinos [00:51:31]:
I agree with you. There needs to be the ability to run it for like a day or two and, and see if the outcome—

 Chris Hladczuk [00:51:36]:
and just see what happens.

Nic Poulos [00:51:37]:
Yeah.

 Chris Hladczuk [00:51:37]:
And like, for us too, like I'm pretty excited about it because like I know what the outcome should be. Now there's a million ways to get there, right? It's actually pretty hard. It's very hard, but like I know what the outcome should be.

Nic Poulos [00:51:50]:
Yeah. I mean, topic for another pod, but yeah, we, we need some, some new approaches to memory and, and context.

 Chris Hladczuk [00:51:58]:
Amazing.

Nic Poulos [00:51:58]:
Well, Chris, you, you, you have me, you have me sold. Maybe some of our listeners too.

Luke Sophinos [00:52:05]:
Did he get the deal, Nick? Did he get it?

 Chris Hladczuk [00:52:06]:
Did he? Yeah. Whatever. Oh yeah. Do we, do we get it? By the way, I show you the product. I show you the product. It's over. I don't know why we haven't even gotten there yet.

Nic Poulos [00:52:13]:
Seriously, man. Seriously. But this is a lot of fun. So congrats again on the, the A and congrats on you. Thanks for joining, man.

 Chris Hladczuk [00:52:20]:
Thanks. Awesome. Thanks, guys.