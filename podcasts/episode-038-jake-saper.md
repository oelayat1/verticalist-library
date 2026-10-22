# Verticals: The Open-Weight Unbundling

Published: 2026-07-23
Type: podcast
Summary: Jake Saper explores open-weight models, falling token costs, AI-native services, model diversification, fine-tuning, and why proprietary data and customer workflows matter as intelligence commoditizes.
Source URL: https://insights.euclid.vc/p/the-open-weight-unbundling-jake-saper-emergence-capital
Featured: Jake Saper
Archive episode: 38
Source file: Episode 38 - Jake Saper
Date note: Date of the linked published episode page, not the recording or Drive upload date.
Transcript note: Automated transcript preserved as supplied; names and speaker labels may contain transcription errors.

## Transcript

Nic Poulos [00:00:00]:
Is open source about to rewrite the rules of vertical AI? We're going deep today with Jake Saper, General partner at Emergence capital. He's a 12 year VC veteran, an early backer of Zoom, Viva and Ironclad, and the guy who coined AI native services. Emergence called SaaS early, they called vertical software early and they bet on open source back in 2023, including Together AI, which just raised 800 million at an $8.3 billion valuation. This episode is about the collision of three forces. Open source models getting good, tokens getting cheap and services becoming software. We get into the token maxing hangover why model labs are launching vertical app layer plays and why the sharpest teams are diversifying spend across more and more models and fine tuning their own to control their destinies. When intelligence gets this cheap, the model becomes less of a moat. This is the conversation about where value actually goes, who ends up owning it and how.

Nic Poulos [00:01:06]:
Let's jump into it with Jake Saper GP at Emergence. Welcome back everyone. Today we are chatting with an old friend, a stellar investor. We've got Jake Saper GP at Emergence Capital. How you doing, Jake?

Jake Saper [00:01:24]:
I'm great, Nick. It is fun to do this with you and it is cool to think about how long we've known each other.

Nic Poulos [00:01:28]:
It's been a while. It's been a journey and a great one at that. VC in New York in sn.

Jake Saper [00:01:35]:
One of the joys of this industry is like growing up in IT with other people and seeing the paths they've taken. And it's been really cool to watch your path.

Nic Poulos [00:01:44]:
Likewise, man. I totally agree with that. You see people at different phases. Now that I'm in sf, I can be seated next to you on Valentine's Day.

Jake Saper [00:01:55]:
That's right.

Nic Poulos [00:01:56]:
Randomly. Amazing. Well, appreciate you joining us on verticals today, Jake. I'm sure everyone's come across your work, but give us a little on you on Emergence. Kick us off here.

Jake Saper [00:02:09]:
Yeah, I'll start with the firm. So Emergence is a venture capital firm.

Nic Poulos [00:02:14]:
Did a. No, we.

Jake Saper [00:02:15]:
We aspire. It's good to know. Just to clarify that for folks, we aspire to be early experts in emerging business models. Hence the name Emergence. The firm got started in 03. The technology shift happening then was moving from on Prem to the cloud. And the business model that was emerging at that moment came to be known as SaaS. Although when the firm got started, actually if you read our founding documents, they were focused on what they called technology enabled business process outsourcing tempo, which they were right on the business Model.

Jake Saper [00:02:47]:
They were wrong on the name.

Nic Poulos [00:02:49]:
Doesn't roll off the tongue.

Jake Saper [00:02:50]:
Yeah, it doesn't roll off the tongue, but the firm obviously first investment was Salesforce and we were early investors in Zoom and Gusto and Box and others. So that was the first emerging business model. The second, which is very relevant obviously to your focus as you know, became vertical software. It was kind of the next big emerging business model that we were focused on. And as you know, we went deep there partnering with companies like Viva and others. Now that we're in this AI era, there's like a plethora of emerging business models that are getting created. It's not yet clear which ones are going to endure and it's not clear which names are going to stick. But we've done quite a bit in AI infrastructure companies.

Jake Saper [00:03:29]:
Like together AI, we've done a lot in physical world AI companies like physical intelligence. And we've done a lot in a category that I'm calling AI Native services. We'll see if that is the name that ends up sticking. But I coined it, so I'm hoping it does. And you and I have riffed a lot on that concept. I am a general partner here. I've been here for 12 years. I feel very lucky to do this job and to work with people.

Nic Poulos [00:03:56]:
I do amazing well, Incredible firm, incredible group of people. And I know we're here to learn a lot from you today. So just before this, we were talking a bit about together and really this. It's hard to say rise because it's been around, but you know, the rise of open source. Let's set the stage. Like what have you been seeing there and what do you see as kind of the emerging consideration and debate around it?

Jake Saper [00:04:29]:
Well, I'll start with our history with it, which is back in 2023 as LLMs were first emerging, we spent a bunch of time trying to figure out how we thought that industry would evolve. And we had concerns that closed source model providers would commoditize and that ultimately enterprises would opt for open source models because they had more flexibility to customize them, more security and privacy, and potentially lower costs over time. I think standing here in June or July of 2026, we were right on one and wrong on the other. Turns out both open source and closed source have been thriving. But to your point of late, open source has really been surging. And I think that open source has been surging for a few reasons. The first and foremost is that the open source model ecosystem is just getting so, so good. So if you check out the most recent models that have been released, they are only very slightly behind the most frontier models of the closed source labs at this point and obviously it's free to fork them.

Jake Saper [00:05:40]:
You then need to run them, you need to actually provide inference to run the models which is where together AI comes in. And that segment, the togethers, the base 10s, these open source inference providers have grown insanely quickly. They've all, most of them just announced big fundraises at very high valuations to support their growth. And I think that is driven a from the improvement in the open source models that are being developed. But also there's some other kind of macro dynamics that have been driving this. The first is what I think of as the hangover from the token maxing era. Right. So there was an era three months ago when there was a lot of pride that companies would take in how much their token spend was going up as an indicator of, turns out, a very poor indicator of value created by AI.

Jake Saper [00:06:35]:
I think that the, the hangover treatment has been to more heavily scrutinize what those tokens have been spent on, what the value has been and to find effectively cheaper tokens to get the same or better outputs. And that's I think dovetailed with the rise in improvement of the open source models and has had lots of folks say oh wait, maybe I can do this with an open source model at 110 the cost. I think there's other dynamics at play. I think you've seen the federal government limit the most frontier models obviously with Fable and GPT 5.6 which I think has caused companies to want to control their own destiny a bit more, which you can do when you forked an open source model and you're running yourself. And I think lastly, as we enter this new era of the kind of AI ecosystem, people are increasingly trying to take the proprietary information they are gathering by serving their customers and embed it within the AI they are using. And this kind of gets to this ever present question of what are the moats in AI? We've talked for a long time about the possibility of proprietary data being a moat. I think you've seen companies over the past 12 months more seriously focus on trying to gather that data in the format of effectively an eval that can be used to fine tune models to be more efficient and proprietary at getting a job done. It is much easier to fine tune an open source model than a closed source model because the weights are open.

Jake Saper [00:08:09]:
And so you're seeing a lot of the leading Agentix software Companies, the Harveys of the world, et cetera, focus an increasing amount of their spend on fine tuning their own open source models versus relying on the closed source labs.

Nic Poulos [00:08:23]:
What do you think about Daria's recent commentary that open source is dangerous? You think this is a self serving comment?

Jake Saper [00:08:33]:
I do, I think it's a very self serving comment. Look, I think that we need AI regulation in general, but I think there should be regulation on both open source and closed source models. The reality is we do not want to live in a world where one or two men control everything, which I think is the world of the closed source dominant labs. I think it's a much healthier thing both for our economy and our democracy if we've got a flourishing proliferation of choices as has always been true in capitalism. And I think open source is a really compelling offering. I think closed source has to find ways to compete with that. It's likely to be true that for the foreseeable future the closed source labs will offer the most cutting edge frontier performance. And I think that's an advantage that these foundational labs, the frontier labs, can continue to exploit.

Jake Saper [00:09:28]:
What I am seeing happen though, both within more traditional enterprises that are deploying LLMs as well as within AI native services businesses, is a move towards a multimodal system where you are using the frontier closed labs for a small portion of your jobs to be done that are the highest intensity tasks and the majority of your runs you are using on cheaper open source models.

Nic Poulos [00:09:56]:
Yeah, I mean I think it speaks to the fundamentally different nature of, of the advantage that model labs have versus let's say cloud infrastructure. Right. Like that in that market developed a natural infrastructural logopoly because the benefit is scale ultimately and that scale is afforded by CapEx. And I feel like some people imagine this being a similar world where it defaults to being an infrastructure oligopoly. But even though CapEx still kind of like, if you consider all the spend in model training to be capex, like it's similar but the advantage degrades. And I think the question is, is that advantage degrading faster over time? Because I think everyone could have said even a year ago that the frontier model kind of lead is only six to 12 months, maybe 18. And is that shrinking?

Jake Saper [00:10:58]:
I think it's definitively shrunk. Like you can see, like the most recent models are maybe a handful of months behind the frontier labs.

Nic Poulos [00:11:05]:
I feel like some major net new emergent properties from whatever the next generation is. It feels like that gap is Closing and then who does that ultimately benefit? It's like, yeah, open source and then back to the cloud infrastructure providers.

Jake Saper [00:11:22]:
That's why you're seeing the togethers and base 10s benefit as they are the cloud infrastructure providers of the AI era.

Nic Poulos [00:11:27]:
Absolutely. So what do we think that, I mean, let's imagine the world in which these trends continue. What do you think that means for the model apps like the major model, like OpenAI, anthropic?

Jake Saper [00:11:41]:
Well, I mean, one thing you're already seeing is that they're hiring vertical specific leaders. Right. To develop vertical specific products. So my friend Jason, who is the co founder and CEO of Ironclad, on whose board I've served for a long time, recently became the head of the legal vertical at OpenAI. And you're seeing both Anthropica and OpenAI hire leaders for specific verticals, which suggests that they will be building applications that are specific to those verticals and end up competing with the companies like Harvey, Lagora, et cetera, which have historically been reliant upon them. Which is part of the reason why the Harveys and Lagoras of the world are spending so much effort on fine tuning their own models so they can separate themselves from dependency on the labs. So I think that you'll see these entities continue to develop competitive products with agentic software companies. I also think that you will see these labs lean more and more into helping BIG Enterprises deploy AI.

Jake Saper [00:12:43]:
Both OpenAI and Anthropic, over the past couple months announced spinouts where they will be using FTEs and AI to help customers deploy AI themselves. We invested in OpenAI's entity called DeployCo. And our aspiration and hope is that on a sort of meta basis, DeployCo can become a very large scale AI native service that is using AI ultimately to deploy AI for their customers. So I think you're going to see the labs continue to lean into those opportunities. I think zooming all the way out for a second, thus far, the vast majority of dollars that have gone into AI have been about developing models. Going forward, I think the majority of the opportunity ahead of us is how do we deploy this technology throughout our economy? And that could look like Agentix software companies, it could look like AI native services businesses. 80% of our economy of our GDP is services driven. So it seems to me that that will be a very likely way that AI ends up getting deployed throughout our economy.

Jake Saper [00:13:54]:
You'll see things like deployco thrive, I think, as an attempt to try to get this technology out in the world more broadly. But I think we in the Valley lose sight of the fact that the majority of our country, and certainly the world still think of this technology as like super Google and don't fully grasp the possibility. And it's certainly not integrated into their daily lives. All you have to do is just leave the Valley for, you know, you can leave for an hour and talk to people and recognize that like we are living in an absolute bubble. And the opportunity obviously is to bring this technology to the rest of the economy in a way that's beneficial. That to me is like the exciting opportunity going forward. And I think open source in many ways accelerates that because it's now faster and cheaper, more importantly to deploy the stuff than it was when the closed source models were dominant 100%.

Nic Poulos [00:14:46]:
I mean that obviously I couldn't agree with you more on you talk with most folks, and rightfully so, they still don't really understand what AI is and what it can do for them. I think a lot more people are interested, which, like in our portfolio, I'm sure yours as well, for true vertical plays is a huge tailwind. But we are in inning 0.2 of the game here in terms of adoption. This is how I think about it. If you froze model progress where it was today, we would still have 20 years of work to do to roll this out to the entire economy and reap the rewards of it. Um, so you raised a couple interesting threads there. You know, one is just regarding, you know, what the model labs do and figuring out how, how to deploy AI throughout the economy, whether that's, you know, next generation integrators, service providers, like, especially in the enterprise, like, I think that is in a lot of ways the game right now is figuring out how to, to help these folks adopt faster. But digging into your point around these kind of vertical specific plays, I do kind of see them and frankly a little bit I see this claim that the application layer is the future opportunity for the model labs.

Nic Poulos [00:16:20]:
I mean, you even see it in, even in SpaceX's S1, right? They're like, oh, 93% of our TAM, which is like what some crazy multiple of GDP is apps. Like, I, that feels, maybe I'm being too dismissive. It feels a bit desperate to me. It's like, look, you have the opportunity to be an infrastructure provider, but maybe they're feeling this open source pressure and they feel they need to go that direction. For me, it's a bit hard. Like if you look at why vertical software was successful in building moats and being sticky and they built these workflows that served unique audiences and ecosystems retain them, and that's what gave them the right to absorb the proprietary data. The workflow know how is because they focused on. And now you have these companies that are basically saying, hey, we're going to do this for everyone, and they're hiring incredible people.

Nic Poulos [00:17:26]:
But I look at anthropic science, Claude for science or whatever it is, right. And it's pretty cool, but it's basically Claude self. Admittedly, it's not a new model and a bunch of connectors. And I don't think that really mirrors the hard work that kind of vertical platforms of the past have put into really building unique workflows and going deep. So do you think it's enough? Do you think that they'll actually be able to carve out kind of application layer spend from these verticals? Or do you think this is kind of a bit of a grasping at straws moment for them?

Jake Saper [00:18:11]:
My guess is it'll be some of both. I think that there will be some verticals that they dedicate enough energy and resources to and they build a robust enough product that it will take off and there'll be a lot where it feels more like straw grasping. I think there's also a little bit of wariness happening right now with enterprise buyers around being fully too dependent upon the labs. I think the idea, both because the models may be gated, but also the fear that they're seeing these labs expand into what they're doing. And the labs are. If you're a pharma company and you give OpenAI all of your data, your IP, your value is in that data is understanding how these molecules actually work and what's worked historically and what hasn't, et cetera. That's the value of Pfizer or any of these companies. And if you're fully reliant on one of these labs and you've given all of them your data, you have to think through how defensible am I going forward.

Jake Saper [00:19:05]:
And if you've seen these labs start to do more of the job to be done and expand, I think for good reason, people are increasingly wary. And that's again another reason why open source is being utilized. So people can kind of keep their data within their house. As I think more broadly about the opportunity for vertical software vendors going forward and really technology more broadly, my view of technology is that the arc of technology history will bend towards outcomes. If you think about the history of technology from the wheel, the wheel existed and was created to get A job done. It was like obviously to move stuff, you fast forward all the way to sas. SAS is another form of the wheel. Like SAS was created to help humans do a job.

Jake Saper [00:19:52]:
SAS doesn't have any inherent value in of itself. It is only a value insofar as like it's a tool that helps people get a job done. With AI, we now have technology that can do a lot of the job. And so we are moving towards a world where the technology vendor is not selling a tool, but selling an outcome. Or what we say with AI native services, you're not selling the pole, you're selling the fish. So the opportunity I think for any of these technology vendors going forward is to figure out how can I own and warranty more of the outcome. Another interesting thought experiment to think through is imagine a world for a second where code is fully commoditized, where everyone can have the same CRM for construction because you could just ask an app to build the latest and it's the best and it's at par with everyone else's. By the way.

Jake Saper [00:20:46]:
I think that is not the world we live in, despite the what some people may believe, but let's just assume it is for a second. What is the value of the technology vendor in that world? The value of the technology vendor is being a throat to choke. It is being an entity that will take on the burden of updating this thing with all the recent technology and as AI is moving so quickly, it constantly has to be updated, fixing it when it's broken, and most importantly, guaranteeing an outcome. There's been a lot of talk about the shift away from per se pricing, which is very clearly happening and needs to happen and towards outcomes based pricing. It is a complicated road. We've hosted a bunch of sessions in our office on AI pricing and outcomes based pricing. There's lots of learnings there, happy to dive in if it's helpful. But the idea that we are shifting towards delivering outcomes as technology vendors I think has to happen.

Jake Saper [00:21:44]:
I think that will be what survives. I think the thing that gets me excited about AI native services vendors is that by definition they are delivering outcome. They're not selling technology, they are selling some sort of service, fund administration, insurance, brokerage, whatever it is to a customer and they are buying that outcome. The customer and I like the fact that the technology vendor has to stand behind and warranty that what they did is good and correct. Back to the foundation labs. I think one of the things they're going to struggle with is this warrantying and guaranteeing element. Let's say for a moment that Anthropic spun up an accounting firm and using Anthropic's proprietary technology, decided to offer accounting services instead of selling this as a technology to others that are doing the same. The odds that Anthropic is willing to stand behind all of the accounting work they do and go through all the audits that are necessary for their clients, et cetera, like all of the stuff that is about standing behind and guaranteeing the work are infinitesimally low.

Jake Saper [00:22:47]:
Like that's just, that feels like a crazy business model shift that they would go through. Which is why again, I'm bullish on this concept of like if you own the outcome, even if the code is commoditized, which again, I don't think it is in most cases that helps differentiate you from the labs.

Nic Poulos [00:23:03]:
Yeah, I mean, to your point, sure. I mean Anthropic and OpenAI certainly have enough money to do something like that, but it's just a separate company, right. At the end of the day, that's what it is. Like that's, it's a, it's a completely different specialization. Completely different. You know, probably capitalization team, like so sure, if they want to become incubators of separate companies, they can. But like right now, outside of the fact that they have near infinite capital, doesn't really, they don't have an advantage to do so per se. You know, like anyone can use any model to do that.

Nic Poulos [00:23:44]:
Right.

Jake Saper [00:23:45]:
I guess one important caveat to this, which is a little ironic, you know, both of them did spin out a company with a completely new cap table and new structure to do this deployment work. I think that's a little bit different because the deployment work is so directly related to their core product.

Nic Poulos [00:24:01]:
Yeah, right.

Jake Saper [00:24:01]:
Their core product is selling tokens and getting a company to adopt AI is in the interest of the core product. And so I think companies like DeployCo make a lot of sense for OpenAI. I think OpenAI spinning out an accounting firm feels unlikely. I think there's also value in the data that these AI native services companies are gathering themselves, which helps them, hopefully with the help of an open source model, you can fine tune, actually deliver an AI service that is better than what the foundational model labs could deliver. So I think about this is actually something I've been thinking about recently but haven't been able to write up yet or think through enough in detail. So I'll spitball with you since you're one of the most thoughtful theoretical people I know. I think that there is a argument to be made that an AI native services business has a better data moat than an agentix software business. In other words, if you were to build an AI native law firm, you potentially would have a better AI moat than Lagora or Harvey that are enablers selling agentic software to these places.

Jake Saper [00:25:13]:
And the reason I think that's true is that if you're an AI native services vendor, you own the full outcome by definition. And the value of that is not just what I talked about before, it's also that you are gathering eval data. Like, you know, so like I think you guys had Chris from Hanover park on a while back. Hanover park is a fund administrator. That's an AI native service that sells basically accounting services to private equity firms. What is really cool about what he is doing is that every time they deliver some sort of piece of work for their private equity firm, you know, and they're doing constantly delivering work, right? Because they're constantly updating the numbers and such, there's a feedback cycle, right? There's a human being who checks the AI and says yes or no, and that helps improve the AI. And then obviously the customer also gets it and says if there's an issue or not, then we go through an audit that we defend and all that. And so we're constantly gathering basically eval data on all the performance of the AI that we built.

Jake Saper [00:26:13]:
And so that process of actually doing the whole job to be done, owning the whole outcome, affords us effectively an eval data set that a software vendor who is, let's say selling software into a fund administrator would never have. Because the software vendor's view is truncated. You don't actually get the full lifecycle of the transaction.

Nic Poulos [00:26:38]:
Yeah, we'll come back to open source. Obviously open source would benefit either model. I think that in a lot of ways the game has become who can build up a better, more efficacious and defensible data asset that drives whatever AI workflow we're talking about. And I do think, by the way, this is also probably the best argument for why the model labs are spinning up these vertical plays, even if they're kind of these not that sophisticated. I don't want to say that, but you know what I mean, like Claude for science, like, okay, it's some connectors, but if they can get a lot of people using it, they're getting a lot of usage data. I agree with your point as well that like, look, it is all about evals. At the end of the day, there is a question in my mind of like, do you necessarily need to be guaranteeing a particular outcome, delivering a particular service as an external vendor in order to capture those evals? Right. Because there's plenty of agentic software that still has access and is driven by the outcome.

Nic Poulos [00:27:45]:
And maybe in some ways this is honestly where my head has been going with this AI native service stuff. I don't think we've caught up since is that the line is very blurry. At the end of the day, there are a few of our portcos that wouldn't in some ways consider themselves a service. And it's just kind of more of where you draw the line of being. I think I've mentioned this to you before, but like internal versus external to the company. And if you're internal, I think about that as having access to as many data points as possible on how their people are doing it today, how it turned out for them. You know, my biggest worry about some AI native services, if you're totally external and like Hanover park wouldn't be a good example of this, they are internalized because you need to be internal in some ways to provide that sort of fund admin service. But you know, my worry is if you're somewhat external, like, hey, we're delivering these like blueprints to you, you don't really see the inner workings of the company.

Nic Poulos [00:28:53]:
You don't. Maybe you don't get. Maybe you get one eval, like, hey, was a blueprint good? But you don't get like how it was used or what was the next step after they got the blueprint. So that informs our next product. So I don't know, it's blurry.

Jake Saper [00:29:10]:
For me, I think that's a great concern and it reflects how we've been thinking a bit about what are the most interesting AI native services markets to go after. I think being an external vendor who is deeply embedded with your customer has so many benefits. Like, one is obviously the eval stuff we're describing. Two is like, generally it's harder to rip you out. Like in the case of handover, their customers are running on their gl, so they're both a service and effectively a software vendor. So it's super hard to think about switching. The other thing that's cool. Which isn't necessarily true in all these businesses, but in some of them is that you can be a bit more in the funds flow.

Jake Saper [00:29:51]:
Like you think about how you get paid. The challenge with selling a blueprint is like, okay, I got a blueprint and it was 20 bucks and I generally pay 20 bucks for blueprints or whatever, 200 bucks. I don't know what the price for blueprints are. It depends probably on the situation. But like that is a little bit like more of a commodity than like oh, I'm in like I'm a BIP space business. Like I charge on a percentage of AUM or I charge on you know, some transaction that I do or I like I have some sort of directly tied financial benefit to the service I'm providing and I think that can happen. You know I actually, I don't know, I don't know if that happens more frequently internally or external. But I think that in general if you're an externalized service that is deeply embedded with your customer, it is a better situation than if it's more of

Nic Poulos [00:30:38]:
a transactional thing because that's ultimately the question. It's like okay, so open source or just generally the cheapening of tokens over time benefits and I think in some ways is probably required for the AI native services bet to kind of work out to its full potential. But at the same time I think that probably like if this, if, if kind of the cheapening of tokens accelerates, so does the ability for external services to get commoditized, right? I don't know. In some ways Jake, do you see it as like it's a, it's somewhat of an arms race to get in the door and start building hopefully that defensible data asset that makes you non commoditizable?

Jake Saper [00:31:28]:
I think to some degree, yes. But I think that there's another important aspect of this which we alluded to before, which is that outside of tech circles the pace at which this stuff is moving is glacial. And what's interesting about these AI native services businesses is that generally speaking they're competing with other services businesses which aren't necessarily people that are moving at the speed of light. As an interesting anecdote, as a company I talked to a couple months ago that had been selling Agentix software to investment banks last year and at the beginning of this year they decided to pivot and become a mid market investment bank basically to use the software they had built, to use the ad they had built and deliver the service versus selling it to someone else. So to go from being a genting software provider to being an AES business. And there was a bunch of really interesting reflections in talking to this founder, perhaps the funniest of which was his zoom background was really notable. It was a super August library thing and I Commented I was like why is your zoom background? He's like, well I'm now a banker. And I was like, so was your zoom background different when you were a software provider? He was like, yeah, totally different.

Jake Saper [00:32:38]:
So it's interesting to think about the zoom background shift when you go from being a software provider to an AIMS business. A couple other things. One, he said that when he started to use his own AI to deliver the service himself, his first emotion was embarrassment. He felt embarrassed about the product he had built because that's actually one of the cool things about becoming an AIDS vendor is you are the user and so you really understand the process much, much more intimately than you would as an externalized vendor. So I thought was really interesting. But the last one and the last point he made, and perhaps the most relevant to your question is he said that my competitive set went from the smartest, best funded people who are building AI for finance to sleepy mid market investment banks. And so I think the same is true across AINS businesses. While I have incessantly been talking about this now for a while, this is still a very tiny portion of companies that are pursuing this strategy.

Jake Saper [00:33:38]:
And so if you choose a service that is interesting, yes, you may have other a businesses that come after you over time, but these industries move much more slowly than software. And so I think that they're. I have less like near and medium term existential dread around like this is going to commoditize, price is going to go to zero, et cetera. Just because I think that there's so much friction in deploying this stuff in the economy more broadly. Yes, of course over time that will happen. There will be downward pressure, which is where this question of evals and proprietary data come in. How much better is your service than someone else? And that'll probably be a function of how much better the data you have gathered and implemented into your system is, which will ultimately provide some pricing leverage. But my sense is in most services contexts, the world of commoditization is fairly far away.

Nic Poulos [00:34:34]:
Yeah, we wanted to take 10 seconds to call out our partner and supporter on verticals. Paraffin. You already know why embedded finance is important. You want to power all the ways your customers make money and grow their business. But you don't want to be a bank, you don't want to be a credit card company, you don't want to be a lender. Paraffin can help you with that. They help portfolio companies of ours, friends of ours, hundreds of other vertical founders, increase retention, increase revenue, grow their tam. So if you don't know paraffin.

Nic Poulos [00:35:04]:
Please take a second to check them out. You can go to parafin.com that's 1F or the link is below this video. Thanks for listening and back to the show. I agree with that. It'll take time and frankly, like in a lot of these domains it's going to take time to build really impactful data moats and to figure out even where to build them. Because honestly, it's not even like in a lot of cases, even if you ask the top experts in a particular operating industry, like if you ask them what are the top three data sets that drive your success? It's probably impossible for most humans to say that if someone asks you or me about our funds, you would have to think about it and probably could come up with some good answers. But a lot of this is buried in, you know, pretty shitty, clunky human organic hardware that we don't understand. And it's gut driven.

Nic Poulos [00:36:00]:
And so figuring out how to abstract how humans make decisions is, I mean, I don't know, that's probably like a multi decade thing we're all going to have to see if we can even do. Well.

Jake Saper [00:36:09]:
I mean, to that point, I actually think some of the best aims businesses today do a phenomenal job of basically creating, you know, the sops for the service by understanding the process and psychology of the people that are currently doing the service. Because you're right, like if you ask someone like how do you do your job? They can't tell you because there's so many things they do without recognizing it. You have to observe them and you have to observe them in all of the various EDGE cases to have a chance of starting to build an sop. That's fantastic.

Nic Poulos [00:36:38]:
You can't even ask them because they probably don't know. They don't know, which is understanding.

Jake Saper [00:36:44]:
This is why one thing, I don't know if Chris shared this with you when he chatted with you, but one of the reasons why Chris makes this commitment when he is onboarding a customer that he will sleep in their office until the onboarding is complete. Part of it is because he's insanely intense and that's just like how he, how he works. But part of it is like you just observe so many things if you are physically present watching the job get done, that asking someone to explain or whatever is never going to get you there.

Nic Poulos [00:37:15]:
I think also there's another, I explained a little bit the internal external framework I like to think about. The other is just whether something is a core peripheral competency for that company. Because ultimately something like fund admin, an investment fund is almost never going to think about that as a core competency. In fact I think I can definitively say no one would ever think about that as a core competency. But blueprints could be. In which case any forward thinking business leader might think like this is cool, do it maybe for now, but long term, whatever knowledge. Exactly. And so being able to position yourself as, look, if I'm that business owner and I can leverage how this model is learning, maybe even have my own, I don't know, version of the model or something, great.

Nic Poulos [00:38:14]:
But if I'm just training this model so you can resell it to my competitors and I think that's probably small percentage that are even caring about it. But that's the concern with the model Labs is like look, I mean it depends on your contract, but that may be what ultimately you're doing is putting yourself out of business.

Jake Saper [00:38:34]:
We talk about this internally as going after tasks that are critical but non core. So if you go to Pfizer and you say I want to do all the AI for your drug development stuff and research, they're probably going to say no, I want to own that because that is core to me. And so they're going to probably use, over time they're probably going to use open source models because they're going to feel more comfortable owning that themselves. But if you go to Pfizer and say hey, I'm going to do your accounting for you, that's critical non core. And if you figure out some way, some service that does accounting for pharmaceutical companies in a better, faster, cheaper way than legacy incumbents, you'll probably make a lot of money.

Nic Poulos [00:39:10]:
I think the other thought around kind of the confluence of, you know, kind of token price changes and open source and native services is really the profile of the a business itself. Right. So like let's go back to that investment banking example. As someone who you know did it, I can say like it's not the quality of the comps that you spread that ultimately determine whether or not you're successful. Right. It's a very relationships driven game and frankly even a lot of the reason people select investment banks is brand is that I want to be able to go to my board and say oh I hired Goldman, even if they fucked up, you can't choke my throat because I hired the best McKinsey. Same thing. I mean there are analysts out there don't work for McKinsey that are just as good, sorry Mackenzie.

Nic Poulos [00:40:07]:
But like you know, it's, it's the brand. So is that ever a worry for you that like even if you're doing 10 out of 10 in terms of the product that it's just kind of like the brand thing changes slowly? The relationships are so important to winning the contract. Is it going to ever be like software was where you know, you can get month long sales cycles and PLG emotions?

Jake Saper [00:40:36]:
Well, the first I'd say is it definitely depends on the service. There are some services that are more transactional where you can just try it and see and if it works great, the ones that are more judgment based, more nuanced, longer term services, the relationship and the credibility becomes really, really important. I have this concept in AINS that we talk about as borrowing credibility. Like you've got to find a way if you were in one of those types of services to very early on borrow credibility because you don't have the credibility yourself. Now there could be a situation where you as the founding team have some stellar, super impressive, experienced person from the industry in which case like you do have some of that, although you don't have the brand, you have the person, but often you don't have that level of gray hair from the service that's on the founding team. So how do you borrow credibility? One is you can hire it, right? You can hire that type of person ideally in a go to market role so that they're customer facing to help build the credibility. Sometimes in an advisory role. But I don't like the advisory stuff as much because it just feels flimsy and often customers won't think it's real.

Jake Saper [00:41:45]:
But if the person running your sales team was the person that you used to work with because they used to sell it to you at the legacy provider, you're probably going to have more trust. You can also find ways to partner with your frenemies. And that's like a really interesting and messy dynamic in ains, but an important one to the very point you described. Like these legacy providers have manpower and they have brand. What they don't have is AI and speed. What you have is those two things. So how do you do some sort of deal where you each get a little bit of the other other person's thing and that deal probably won't last forever, right? Because there'll be some changes, right? You will either outgrow the need for them or they'll try to compete with you. Who knows? But when you're getting off the ground, I have found that a lot of these Legacy service providers are willing to do partnerships with these kind of emerging ains vendors because they know they need to go to their customers and say, hey, I've got the flashy AI thing and this impressive team.

Jake Saper [00:42:50]:
And so they're willing to do some sort of rev share. And in some cases if the service is still partially manual, you can have the legacy vendor provide the manpower and you can have the AIMS provider provide most of the technology and then people get paid for each of their respective things. These are messy and nuanced and I've worked through a few of them now, so I have some reps. But it's still early days. But in general, like there are ways to borrow credibility. I would say the last way to borrow credibility and perhaps the most expensive, both in terms of costs and potential downside, is acquisition. You can acquire a legacy provider that has some sort of credibility. I think there are situations where that makes sense, particularly in situations where there's some sort of like license or regulatory hurdle you have to get over.

Jake Saper [00:43:40]:
There are certain businesses where like, you know, it takes three years to get the license you need to perform the service. So acquiring someone who already has it could make sense to jumpstart it. And perhaps they also have a reputation. It helps you manage the credibility issue. I am not however a fan of the kind of acquire a bunch of companies, slam them together and then try to inject AI into that entity. That has been a popular strategy. I've heard some people describe it as cosplaying private equity. And look, I think there'll be situations where that succeeds.

Jake Saper [00:44:14]:
But I think that the challenges with that strategy are many. A, you're distracted, right, With a whole massive integration project versus building AI and having the service truly be AI first. By definition it won't be because it will still be legacy people doing it the same way they used to do it. You have to convert all those people or fire a bunch of them while still maintaining the customer service somehow. It's just, it's a really complex thing. I think it sounds better in theory than in practice.

Nic Poulos [00:44:41]:
Three, three businesses in one got to have an operating business, AI business and a PE business.

Jake Saper [00:44:48]:
Yeah. And I think just, just doing the, the, the speaking of like businesses in one, like just being an AI native services business and I named it AI Native service to distinguish it from the roll ups. Like native is like starts with this. That's hard enough man. Like you have to build both McKinsey and Stripe simultaneously and you have to have them talk together seamlessly because the interface is that is the value. It's so hard to be a great professional services firm and deal with all the customer stuff and be responsive and deliver what they want and continue to be a platform technology first company that's steering the direction for the longer term versus just constantly responding to whatever your customer is demanding in that moment.

Nic Poulos [00:45:27]:
Totally. I can't believe it, but we're almost at time. I don't want to take up your whole day. I wanted to touch on some of the more kind of regulatory stuff, but we'll save that for another one. I wanted to wrap up with a couple of maybe just like rapid fire questions, close us out if you're cool with that.

Jake Saper [00:45:49]:
Sure.

Nic Poulos [00:45:49]:
So one, just kind of riffing off what you said for the founders out there who are building innovative services or something peripheral to it, what are the top three or so differences in terms of how you're seeing these companies get built in the really early days versus traditional software?

Jake Saper [00:46:09]:
Oh man, there's way more than three. I wrote a whole playbook on all the ways in which it's different. So it's definitely worth checking out the playbook. Just some very quick ones. We touched on this earlier, but like you need domain credibility on the team, which is not necessarily true in certainly in horizontal SaaS and even in some vertical SaaS situations it's less important. But in this situation it's critical because like people need to believe you're selling yourself, you're not selling a product. How you think about going to market and growing is very different. There's a huge danger in AI native services around Mirage product market fit.

Jake Saper [00:46:46]:
And what I mean by mirage product market fit is you're growing really quickly, you've got great customer retention, customers love you, but you don't actually have product market fit because the service is still being primarily delivered by humans. If it is that situation, you're just a services business that's taken the wrong type of capital. The only way to find product market fit as an AI native services provider is to find a way to deliver the service at a high quality way, primarily by AI, and importantly to have that service be increasingly performed by AI over time. What I'm seeing instead is many companies get very quick revenue traction because if you go sell an existing service faster, better, cheaper than incumbent, of course people are going to want to try you, but they have not figured out how to get AI leverage in it yet. And that's like the biggest risk I see in AI native services right now. Is that dynamic. Some of the best founders I work with actually intentionally slow growth. In the case of Hanover Park, Chris has a ton of demand because he's selling a service that's like way faster and better than a legacy service provider.

Jake Saper [00:47:46]:
But he's trying to grow intentionally to make sure he's got the right people and that the AI platform is mature enough to handle all the customers he brings on. So since I have invested every other quarter, he stopped selling. He just stopped taking customer conversations to ensure that they were delivering against all of the commitments they had before in a high quality way. I love that discipline because it means that you're actually building an AI native services business with high gross margins and technology delivering high quality versus solving for consistent skyrocketing revenue growth, which I think is what software vendors tend to do.

Nic Poulos [00:48:18]:
All great points and yeah, we'll link to the full playbook for those of you who should check it out. Number two, you said you guys are constantly thinking about what markets make sense for aims. Are there kind of two to three that are top of mind where you would love to see more right now?

Jake Saper [00:48:37]:
Yeah, we actually have like a massive spreadsheet that we're constantly evolving where we're trying to sharpen our thinking here. I think there's a lot, I think that like the, the MSP space is still really interesting. There's been a lot of roll up work there, but I think there's opportunity for AI native services in that space. I think the customs brokerage space is pretty interesting. It's a license based business, but one that's really dynamic and where AI obviously could, could be well suited. I think there's a bunch of legal services, there's been some contract focused alienative services, law firms. I think there are a bunch of other opportunities that are slightly further afield. All sorts of paralegal services, et cetera.

Jake Saper [00:49:14]:
So there's a bunch. That's why I think we're in such early days.

Nic Poulos [00:49:17]:
Early days man. Opportunities in front of us all. Okay, we'll close out with just a fun one. You don't have to take it too seriously. But setting aside ability to buy or personal desire, would you be a buyer at current valuations? Any of the following companies? OpenAI, Anthropic, DeepSeek actually, I still don't

Jake Saper [00:49:41]:
know what DeepSeq's valuation actually is.

Nic Poulos [00:49:43]:
It's like 50 to 60 billion.

Jake Saper [00:49:46]:
I probably would not buy Deepseek just because I don't have enough conviction as to how they are different from the other open source model vendors over the long run. Anthropic and OpenAI. Yeah. Because I think they'll both pop in the ipo. The question is like, how long do you hold it? I think, like it's. I think it's not a bad trade of buying now and then potentially selling shortly after you get the kind of retail pop. Yeah, the long term hold. I.

Jake Saper [00:50:11]:
I don't know.

Nic Poulos [00:50:12]:
Well, we'll see. We'll save that one for next time. But Jake, this is awesome, man. Really appreciate you. You coming on and taking the time and always good to see you.

Jake Saper [00:50:20]:
Yeah, thanks. Nick. Sam.