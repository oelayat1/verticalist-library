# Verticals: $100M, Zero Churn, All Channel

Published: 2026-08-19
Type: podcast
Summary: Sahill Poddar explains Parafin's channel-led embedded capital model, platform selection, product sequencing, AI-assisted underwriting, and how financial services can deepen vertical software economics.
Source URL: https://insights.euclid.vc/p/100m-zero-churn-all-channel-sahill-poddar-parafin
Featured: Sahill Poddar
Archive episode: 41
Source file: Episode 41 - Sahill Poddar
Date note: Date of the linked published episode page, not the recording or Drive upload date.
Transcript note: Automated transcript preserved as supplied; names and speaker labels may contain transcription errors.

## Transcript

Luke Sophinos [00:00:00]:
Most VCs in the country have some sort of thesis on vertical software and vertical AI. And if we're being honest, most of them are just making educated bets. But our guest today is not. Sahil Padar is the co-founder and CEO of Parafin. It's a company that powers embedded capital inside some of the world's largest platforms— DoorDash, Worldpay, Mindbody, and more— which means Sahil has one of the rarest seats in technology. He's watching dozens of vertical software companies build financial services on top of their platforms, and he understands Better than almost anyone. The patterns that separate the ones that compound from the ones that stall. Today, we're going to mine Sawhill's dataset.

Luke Sophinos [00:00:38]:
What actually makes a vertical SaaS company great? What are the traits the best ones share? What's the right way to actually become a financial services company over time? And why sequencing matters for vertical software more than ambition? And finally, how AI is quietly rewriting the economics of underwriting, distribution, and the moats that all of us thought were permanent. If you build in vertical software, if you invest in it or you sell into it, this is the episode Not to skip. Let's get into it. All right. Welcome back to another episode of Verticals. Luke Safinos here, joined by my partner in crime, Nick Poulos. And we got a really special guest today. He's been a longtime supporter of the pod and friend of the pod.

Luke Sophinos [00:01:26]:
And he has an incredible story, but his company is absolutely ripping and it's a goldmine of data for vertical SaaS and what's working, what's not working, all of those things. So first off, I want to welcome founder and CEO of Paraffin, Sahil Padar, to the pod. Welcome.

Sahill Poddar [00:01:44]:
Thanks, Luke and Nick, for having me. I'm excited to be here.

Luke Sophinos [00:01:46]:
So maybe just to kick things off, your background is incredible. You spent time at Meta, then you jumped over to Robinhood. I'd love to just hear a little bit more about you and Specifically, like the move to leave Robinhood, you're at like this incredible company, it's ripping. And for you to say, hey, look, I'm gonna go start this thing. I'd love to just get into the mindset and what it took to make the leap there as you go into your background.

Sahill Poddar [00:02:13]:
Yeah, for sure. So, you know, I grew up in a small business family in India, was always into sort of the math and computer science and physics, did a bachelor's, master's, and then eventually a PhD in particle physics, and that's how I got into the world of data science, which led me to Meta and then serendipitously to Robinhood. At Robinhood, I met my co-founders who I started Paraffin with. And I think what was very evident while we were there was that there was a renaissance happening in consumer finance. Robinhood naturally being a huge reason for it. You could download about 5 to 6 different apps that were all at scale. From the Apple App Store, move money pretty much instantly, and start to use the best-in-class user experience that could be offered in consumer finance. At the same time, it was also evident that while there was this renaissance in consumer finance, a sector that is extremely important to the economy, which is a small and medium business one, was kind of being left behind.

Sahill Poddar [00:03:21]:
Yes, there was digitized payments. via sort of Square and the Stripes of the world. But there was so much more left to do in that space. And when you kind of look at the challenges of small businesses, you know, that effectively drive about 40% of the US economy, small and medium businesses, there's really 2 different ways in which they can invest in their growth. Either they can take their earnings or they can access the debt markets. Selling equity is not really an option for them. It is for larger companies. But when it comes to the debt markets, in our view, it was unfair, the status quo.

Sahill Poddar [00:04:01]:
And so, we decided to start Parafin to change that and took all of the learnings that we had from Robinhood, having built a large part of the growth engine, revenue engine, payment infrastructure engine there, risk management systems there, and apply that in building an SMB financing business.

Luke Sophinos [00:04:22]:
It's such a cool path and it gets me excited. I'm looking forward to digging in on it. At that time, Sahil, there was a bunch of like direct-to-SMB lenders, you know, the Cabbages of the world, like BlueVine, OnDeck.

Nic Poulos [00:04:39]:
Did you—

Luke Sophinos [00:04:40]:
what made you say, hey, we're going to go kind of partner with like platforms and basically distribute capital that way versus going direct to SMB? And a lot of those, quite frankly, are dead now, or they were sold at a discount. Like, what was the thought process there?

Sahill Poddar [00:04:56]:
Yeah, so that's a great question, Luke. And I think, you know, I'll put it even more sort of in stronger words. Silicon Valley is a graveyard of SMB lenders. And, you know, some of the names that you mentioned are poster childs of that graveyard. I think the The critical thing that, you know, the previous generation of SMB financing businesses have gotten wrong is they've been a direct-to-SMB business. That is a fool's errand in our opinion because first and foremost, it attracts a lot of adverse selection. You don't really want to— you know, the only way to like scale a business like that is to run marketing, some form of marketing. Whether it's digital or otherwise.

Sahill Poddar [00:05:44]:
But in reality, you don't really want to give money to people searching for money and looking for money because there's obviously very strong adverse selection there. It is also a business which is essentially marketing-led because that is your fundamental way to grow the business. And that is a race to the bottom and a fight that the marketing networks win and ad networks like Google and Facebook win. If you and I, for instance, were competing in a direct-to-SMB lending business and we both had to go and get 10,000 businesses to use our product, the only way we could do that is to run some form of advertising. And so, very quickly, we start competing on who has the best creative and the best messaging and the best assets versus actually the best product. It is a highly commoditized product, and having to put that sort of marketing layer on it is not is not really going to help us build a— and leverage all the expertise we have, which is technology and the ability to use data and data science. So, we can kind of see the outcomes as a result of the strategy of going direct to small businesses. We're not really underwriting on any proprietary data either, and you're not leading from trust, right? Like, Nick's restaurant has no reason to pick Luke's financing over Sahil's financing.

Sahill Poddar [00:07:04]:
you know, he knows neither of them, and it's the first time he's seen ads for both of them. And so for him, like eligibility and pricing are the 2 ways he weighs the pros and cons. Now, when you kind of flip that, you know, this is the model that we just discussed is a pull-based model where the SMB is kind of pulling the offers from different providers, offering it to them. When you kind of push that to a push-based or embedded financing model, you can address all of the shortcomings of the previous model. First and foremost, you can lead with a data advantage, right? Amazon knows exactly what a seller is selling on their platform, how much they're making, and what they've done over the past few years. Same for a restaurant on DoorDash, on their restaurants, Mindbody in their yoga studios, right? They just have asymmetric information about this business, highly granular transaction data, In fact, they know the exact amount of orders that led to a total aggregate sale. So, there's data advantages. You can use that data to underwrite, but more importantly, you can actually use that data to reach a merchant even when they're not looking for a loan.

Sahill Poddar [00:08:15]:
And that is what is special about the model. We pre-approve offers, and it's a push invite-based only or push-based model where despite Nick's restaurant not being you know, in the market for a loan, they— he will see what is an offer based on his historical performance every time he logs into DoorDash. And there is a non-zero probability that he will eventually take that loan because it starts to plant ideas in his mind that, hey, I know that $50,000 is a click away. 2 days later, he sees a new kitchen somewhere and he's like, well, maybe I'm going to buy this new kitchen because I know I have $50,000 a click away on DoorDash. So you start to attract a really good borrower base, which is not possible if you're direct. Secondly, you lead with trust. Trust is the bedrock of any financial transaction, especially when it comes to lending. You know, similar to how a lender is afraid of adverse selection, a borrower is also afraid of the consequences of taking a loan on and what happens next.

Sahill Poddar [00:09:11]:
What if I'm— what if I'm a little bit slower in paying it back? What if I can't pay it back? Are they going to run a collections process on me from what I'm used to seeing in Hollywood movies, or what is that going to look like? But if it's coming from a platform that is already managing a critical workflow for you, you know, DoorDash in this example of Nick's restaurant, then he's much more likely to trust it because he knows that DoorDash is a demand generation engine for him. It sits very low in the Maslow's Pyramid of Needs. They have their best interest you know, in their minds because they also want Nick's business to sustain for a very long time. And so leading from that trust drives higher conversion, but interestingly, it also drives lower loss rates. It's easier for Nick's restaurant to walk away from Sahil Capital or Luke Capital, but harder for Nick's restaurant to walk away from DoorDash. And when you start to put these things together, I mean, on a P&L, it shows up as zero CAC for a provider like ours because we're not actually spending any marketing dollars. But, you know, I think qualitatively it's a lot more nuanced than just zero CAC. It actually is driving different behavior, and that is leading to a better outcome, both from a portfolio standpoint, but also from a scalability standpoint, because, you know, one integration into a Mindbody or a DoorDash can help us get offers to all of the eligible businesses out there.

Sahill Poddar [00:10:35]:
And, you know, the focus then becomes how do we use product to drive adoption versus marketing?

Nic Poulos [00:10:41]:
So, 2 questions about that. You know, often at the earliest stages, I'm skeptical of founders who over— overweight the channel, right? And in a lot of ways, you know, your initial vision, that was kind of the differentiating factor. Like, how did you approach the somewhat cold start problem? How did you kind of validate like, hey, this, you know, this can scale. There are a ton of these to go out and capture. What was that early experience like?

Sahill Poddar [00:11:16]:
Yeah. So yeah, that's an amazing question, Nick, because, you know, the cold start problem is real for any startup. It is more so real in our business where we need to have data to underwrite loans and prove to a large platform that we deserve to underwrite loans for their merchants. By the way, we've never done that before. So, you know, how do you go about doing that? Look, the reality, and this is what I tell all my friends and family members who are not in the Bay Area or in the sort of Silicon Valley ecosystem, is that you need to find ways to get lucky. And the way to do that is to increase your exposure to the extent that eventually you will get lucky. So our approach there was, you know, let's talk to as many platforms as possible where this is a fit. Let's show up with a compelling product flow, get their feedback on it, and let's wait to see who says, yes, we are ready to partner with you.

Sahill Poddar [00:12:17]:
And we got very lucky in that DoorDash was one of our very early partners. You know, today when I tell the story that there was a company that was publicly— and it was public back then. It had just gone public, and that, you know, the largest restaurant aggregator in the world, which is public, decided to go with a seed-stage company to lend to its merchants, which is a pretty CapEx-heavy, you know, product. People find it astonishing, and I think in hindsight, we were quite relentless in making the pitch to every platform where we thought this was a good fit and really pushing them to launch with us. And making sure we have the most compelling product in front of them and really give them zero reasons to say no. You know, fun fact, when we were on a call with DoorDash, they were very close to making a decision, and then basically they made a decision on that call to move forward. We had the entire Parafern team on the call. There was 5 of us, and they asked, how big is the team, guys? And I was like, everyone's on the call.

Sahill Poddar [00:13:20]:
And, you know, they kind of laughed at it, but kind of got nervous at it. And after the call ended with the team, I remember speaking to their decision maker and saying, look, I know, you know, that we are a small team and that should give you a pause and will. And naturally, it's like, you know, it is a consideration for you. But what I will tell you is that you can treat us like the DoorDash capital team. We will do everything possible to make this product successful for you. Having a financial services background and knowing, you know, sort of the— having the ability to draw a through line from compliance to risk management to payments naturally helped. That was the first filter that DoorDash applied, like, do these guys even know what they're talking about? And then after that, you kind of have to just show the speed at which you're willing to move and a desire to make the best product for their merchants. There was another joke in there, or which, you know, it's true, but it was kind of very, very humorous at the time, was this partner of ours at DoorDash was the first person we chatted with as soon as we woke up every morning and the last person we chatted with before we slept every night.

Sahill Poddar [00:14:34]:
And so, you know, my wife and the same for my co-founders, like, you know, their partners were all like, what is going on? Who is this guy who you're like DMing all the time? You know, you have to move fast, you have to show that you understand what you can do, and then it's a matter of getting as many people, having a huge top of funnel, and then eventually you'll be surprised who says yes.

Nic Poulos [00:14:57]:
Without dwelling on that for too long, I'm just, I'm really curious because I've seen it in our portfolio too, and our founders struggle with how to approach it when on one hand, I mean, it's just this godsend that you have one of your biggest possible customers you know, leaning in, in, in day one. But, you know, at the same time, it's like, man, this is, this is one of my biggest potential customers. Like, I've got a Mac, like, I can't give this away for free. I can't, like, let them completely take over the product. Like, did you balance that? Or did you just say, I just got to do everything, pull out the stops?

Sahill Poddar [00:15:35]:
Yeah. Um, Look, I think you do have to do everything to pull out the stops, but at the same time, we also had to try to balance it as much as possible. So, you know, DoorDash was not the only platform that went live around then. We had other platforms and they all, you know, we've had basically zero enterprise churn since the start of the business. And so, they all are very happy customers today. And we were very intentional about not getting platforms in the same vertical all at once. And I can dive a little bit more, you know, why that is important, but we ended up getting like Mindbody, another, which is naturally a big vertical SaaS in the gym and fitness studio space, a payment processor in the auto shop space called 360 Payments, all as early customers. And so that helped us kind of, you know, make sure that we are not too single-threaded and we don't have like too much of a point of failure.

Sahill Poddar [00:16:33]:
And if one platform's being slow, like we're not sitting idle. But yeah, you have to try to run on both of those axes and make as much progress. And I guess that's where having like good co-founders is.

Luke Sophinos [00:16:50]:
If you want to inverse of that story, I signed a massive customer who was almost $1 million of ACV early on, promised them the world. did not deliver them the world. And it took us many, many years to rebuild trust with them. So, as he puts it eloquently, it is very difficult to walk that balancing act. And you got to be really careful when you bring on someone of that magnitude because I have battle scars from it for sure.

Nic Poulos [00:17:20]:
Luke, would you, doing it again, would you have scaled up the team faster or would you have waited on that customer? Like, what's the learning?

Luke Sophinos [00:17:29]:
You know, the learning for me was I was probably— not that the age is an excuse, but I was like 19 or 20 at this time, and I just oversold them. And I think Sahil didn't, from what it sounds like, right? Like, they bet on him, his background, he had already had the experience. I basically just listened to what they wanted in the product, and I said, we'll go build it for you. Right. And that ended up— what they wanted was like a true enterprise thing that was going to take a long time for us to get to. And I just didn't— I don't think I had the battle scars to connect those dots at that time. So don't oversell was my learning.

Nic Poulos [00:18:09]:
Yeah.

Sahill Poddar [00:18:10]:
Yeah, I think the, you know, to kind of maybe extend that idea, our key learning was sell, always sell the minimal viable product from a sales perspective. Like if they're willing to buy this, everything that I add to this is only going to delight them. And, you know, kudos, kudos to the entire Parfen team back then and even today that we have that ethos where, you know, we don't try to overbuild but really push ourselves to ask what is the single biggest value prop that is selling. And if that alone is not worth it, then, you know, maybe we need to go back to the whiteboard.

Nic Poulos [00:18:47]:
I love it.

Luke Sophinos [00:18:48]:
So, this is a good question for both of you guys because, you both are underwriting businesses, albeit in a little bit of a different way, but Sahil probably has one of the best datasets on vertical software companies because he's literally underwriting them and giving their customers money. So, I'd love to just hear what makes— what are you seeing where these companies are absolutely crushing it? Your whole audience here is going to be vertical software founders, operators, investors. So, if there's any kind of similarities or threads that you see the best ones doing, I think that'd be awesome for the audience. And then I'd pose the same thing to Nick. What is he seeing in his universe? He's taking pitches every day, right? Of who's growing the fastest, who's growing the most efficiently. I think that's a fun one for both of you.

Sahill Poddar [00:19:39]:
Do you want to go first, Nick?

Nic Poulos [00:19:41]:
Yeah, sure. I mean, I think it is Probably fundamentally different, right? I mean, like, in a way, the folks who, you know, you're partnering with, like, your kind of primary level customers at vertical software businesses, you know, maybe that looks like what I might have invested in a few years ago. And kind of the, you know, the, but at the end of the day, the person you're underwriting is kind of that operating business, you know? And so I think, look, from our perspective, at the stage we operate, You know, it's very much driven by the founders, their character, their experiences, as well as, of course, as vertical AI investors, our view on the market and the approach to that market. I feel like there is data that you can apply and we do, but, you know, I don't think we could build the, you know, pure Euclid version of, what is it, Paraformer? Like, it's not quite as deterministically data-driven. That's my sense, but yeah, Sahil, how do you guys think about it?

Sahill Poddar [00:20:51]:
Yeah, so I would say, you know, there's sort of— there's 2 parts to your question, Luke, and correct me if I'm wrong. Like, you know, what are we seeing in terms of data? What separates best-in-class vertical SaaS from your median vertical SaaS? And the different ways we can use data to underwrite both the platform and the small business. So, on the first question, one key learning has been that the best vertical SaaS are, they operate as collective bargainers for all their businesses when it comes to negotiating with their vendors for services. And the harder they bargain, the better they get. for their businesses, right? When it comes to, for example, you can think about a vertical SaaS going to Stripe trying to negotiate payments, payment terms, payment products, you know, they're not just negotiating for their own business, but really for the end merchants that are using them because they're going to be repackaging that and selling that as a key service to their small business. The same with when they come to ParaFin for lending and so on and so forth. Another key learning has been that while every vertical SaaS gets a foot in the door with one aha moment, one wedge or key feature, in order to really build a fort, you have to be solving for many different business needs over time. And, you know, there's obviously a winning sequence, a winning way to sequence that versus not, but it has to be many different things that you're doing for your business, so much so that you eventually become the operating system for that business.

Sahill Poddar [00:22:35]:
And I'm sure, you know, you guys have already debated that a lot in past episodes and discussed that, so I won't go into that. But those have been 2 key learnings. We typically look at data both at the platform and individual business level. When we're looking at data at the platform level, we're really looking for 2 things. So, The way our go-to-market works is we typically go to a platform, we talk to them, we learn more about them, we ask them from an anonymized dataset, an anonymized and randomized dataset, and we run that through our underwriting model. That tells us very quickly the quality of and the robustness of the platform via their merchants, how large is the lending opportunity, but even before that, How quickly are merchants churning? How quickly are they acquiring merchants? How quickly are these merchants growing? And does it make sense to give credit both from a credit quality standpoint but also an economic opportunity for the platform standpoint? We try to create as much economic opportunity for the platform as possible by minimizing the amount of work they need to put in to offer embedded financing products. But that also means having to turn away a lot of platforms that are either not, you know, where the platform is better off focusing on its core business today and then attaching lending later. Roughly, it's like, you know, if you have less than $1 billion of payments, it doesn't quite make sense to do lending.

Sahill Poddar [00:24:02]:
Beyond that, it does. There's naturally exceptions to that rule. And, you know, sometimes we've had to turn off large platforms because maybe their merchant churn was too high, and we can just see that in a few years they're not going to be where they are today. So, that's how we try to underwrite platforms. And you start to learn very quickly about like, you know, what are the pockets, how quickly are merchants growing, etc. And then at a merchant level, there's a lot of innovation which we've done in being able to right-size the offers for businesses, both highly seasonal and non-seasonal, use AI to, you know, we've built our own transformer model, which Nick alluded to called Paraformer, which is a state-of-the-art in time series analysis. And most recently, we published a bank transaction AI system that we built that looks at a PLAT token and is able to assign a credit limit based on just that. And so that's the kind of innovation that we're doing at sort of the SMB level.

Sahill Poddar [00:25:02]:
But when you kind of add that up and look at the platform level, we're looking to both understand the health of the platform, the scale of the opportunity, And by just having worked with many of these platforms at this point, I've realized that the best ones are collective bargainers for their merchants. And they often have a plethora of features that they've built a fort such that the consideration for leaving the platform is very high when it comes to each individual merchant. What is also true in both data that we see across our partnerships, but also reported by Square and Shopify, is that your highest LTV merchants, you know, if a merchant starts to use financing, it is a really good stepping stone into using other products in the ecosystem. And you either have merchants using just 1 or 2 features or merchants using 6+ features on these platforms. And the latter obviously are the higher LTV for the platforms. And there is almost like 2 clusters forming where some people are just using the bare bones, some merchants are using the bare bones. But once they start to use a few different features, they very quickly migrate into maximizing the number of features they're using from the platform.

Nic Poulos [00:26:09]:
What are the— like, if you're just looking at pure volume of transaction data, right, there are, you know, there are much broader-based platforms out there, but you guys have a very interesting and sounds like potentially differentiating data point in like, hey, what software ecosystem are they operating in? Like, what do you require from partners in order to underwrite? And how much does the kind of vendor partner play into it versus just, hey, here are the cash flows of the underlying operators, yes or no?

Sahill Poddar [00:26:45]:
Yeah, so the way we— the sort of the minimal dataset that's required to go live with ParaFin is the platform has to share sales data. So maybe taking a step back, actually, before that, there's Today we have actually 3 different products and they work a little bit differently to one another. The core, or rather the oldest, most tenured product is the working capital product. For that product, step 1 is to ingest data from the platform where the merchant is typically a seller. So restaurant on DoorDash, e-commerce seller on Amazon, gym and fitness studio on Mindbody. They're using those platforms for generating demand, processing payments. And then eventually that payment shows up in their bank account. We're using that transaction data, you know, historical in order to underwrite.

Sahill Poddar [00:27:35]:
And then on an ongoing basis, that data is shared with us such that we can service the loans. And this is what is important, also an important distinction to, for example, Kabbage in the past. Kabbage was also doing some form of quote unquote embedded lending, but their embedding was a referral link on Airbnb. And then you had to go and click on it, apply, and only to get rejected. And at that point, you've created a tension between the borrower, which is an Airbnb host, and Cabbage, and Airbnb. And no, no, neither of the 3 parties is happy about that transaction or that experience. But a true embedding in, you know, what we like to think of it, there has to be some data going into our systems that is being used to provide an experience which is otherwise not possible. And that data is transaction data at a merchant level going back several years that is used to underwrite the merchant, create an offer, and once they click on it, they should be able to go through it in a few tens of seconds and get funded pretty much the same business day.

Sahill Poddar [00:28:40]:
So, that's the key data point. While the merchant is in the flow, we are also collecting information about their other business practices, like how much debt do they have, We are able— we have an AI agent that runs in the background and checks on all the liens. And so they need to verify some of that information if we ask them for it. We have another agent that's going and doing adverse media selection. And so what we've realized is if a business owner has previously filed for bankruptcy, they are more likely to file for bankruptcy in the future. It's a pretty simple observation, but the way you can act on this insight is you can actually run an adverse media check. You can have an agent that does that and see if Nick from Nick's Seafood Restaurant has filed for bankruptcy in any one of his past entrepreneurial endeavors, and if so, we likely need to take a deeper look. So there's a bunch of different AI agents.

Sahill Poddar [00:29:41]:
I just gave you 2 examples. that are going in the background and checking that. And the merchant is also providing us with an open banking token, which we use to kind of look at their sales from other sources and build a debt-to-revenue ratio for each individual merchant, and then which then, you know, helps us decide whether or not we should extend this loan. We naturally don't want to overextend ourselves on even a single obligor basis. So that's how it typically works. Our second product, which is a buy now pay later product, does not rely on that platform data because the buy now pay later product is not meant for a small business seller, but rather for a small business buyer on a platform. A small business can defer the expense, any expense where Payoneer is integrated using a buy now pay later product construct. And our first partnership that is publicly announced and live is with Gusto in order to enable small businesses to defer their payroll expense.

Sahill Poddar [00:30:42]:
What we realized from our core working capital product was payroll was one of the most top used cases for working capital because we asked the merchant what they plan to use this money for. And so you can essentially highly contextualize that product at the point of expense in Gusto. So today If you're a merchant on Gusto, you have to approve your payroll every couple of weeks. In that approval flow, you can either choose to continue to pay with your bank account or you can pay with Parafin. If you pay with Parafin, we will send Gusto the money, Gusto will process the payroll, and we'll collect it back from the business. So, the money movement also works in a buy now, pay later mechanism where these are non-fungible dollars. They are only— they are deterministically being used to that payroll run. And we've seen great success with that.

Sahill Poddar [00:31:29]:
This is our fastest growing business line, growing 3x faster than anything we've shipped before. So there's a lot of excitement around that and a lot of different use cases we're looking to enable in the near term. And that's using the open banking token only. And our models basically got intelligent enough over time that we could use the sales-based data from the platform and open banking data from the from a Plaid token, and we can have the same performance for both of them. So, that's what got us really excited, and we shipped that. And, you know, I think there's still a— these are like some early wins we've had using AI, and that's gotten us very excited about what's in the future.

Luke Sophinos [00:32:11]:
What is in the enterprise sales motion DNA over there? Because you guys are knocking off some big dogs. Like, What are you doing? What's the sales motion?

Sahill Poddar [00:32:23]:
Yeah, I mean, we have a great team. I think that is first and foremost, you know, has led to good outcomes. Our head of revenue, our head of sales, our head of platform growth, they all are fearless and, you know, very compelling. But when I look at what is true about in the history of Paraffin, and I think what will be true in the future, is we have a very cerebral way of selling. It is a very non-salesy sales process. We are almost trying not to sell, and we're trying to just make them understand what is the opportunity that exists if we were to partner together. And at the same time, also being slightly skeptical that this partnership may not make sense because maybe You're better off focusing on your core business and coming back to us 6 months down the line or 12 months down the line. Believe it or not, a very intellectually honest sales process like that where we're not being super aggressive in selling but rather very cerebral, leading with a lot of data, with a lot of analytics, being very transparent about the opportunities we've created for other partners leads to these outcomes.

Sahill Poddar [00:33:41]:
At the same time, enterprise sales is not easy. It always takes longer than you expect. The integration always takes longer than you expect. The activation always takes longer than you expect. And so our teams have been doing a really good job in having a very healthy top of funnel so that we can still continue to beat our goals as we execute along the way.

Nic Poulos [00:34:01]:
So I just kind of wanted to shift to, again, with your guys' corpus of customers, you have a pretty interesting perspective on, you know, how AI is diffusing throughout the vertical software ecosystem. Have you seen any kind of secondary effects or changes in the way you're thinking about Paraffin as a result of some of these more, you know, kind of AI-forward product lines or businesses?

Sahill Poddar [00:34:31]:
So we've debated this a lot. My co-founder and I have debated many ideas. And I can tell you what our framework is. We think what is most important is to have AI actually go and do a task for a small business that is saving them time and/or money. If that is not true, it's likely not a good idea. So I can tell you some of the bad ideas which we discussed and we thought, hey, this isn't— there's no— we don't think this is very valuable, is providing financial insights, right? Like using AI to provide financial insights. This is not meant to be a dunk on anyone doing this, and I'm sure there's versions of this that work well. But in our opinion, providing the insight itself is kind of It's not enough.

Sahill Poddar [00:35:28]:
You need to do the action that the insight has revealed in order to create real value. And that's what's different about AI is that it can actually go and do the action for you, right? It has, with all the tool calling and all the MCPs available today, you can actually go and like do the task wholly and you can, you know, use agentic payments to pay for things. You can browse, could use computer use to browse. any website, and so on and so forth. And so, until we feel very compelled that there is a meaningful action that we can take, and we have a right to win when we take that, we're not necessarily going to make a new product category, but rather, we are seeing so much lift from AI in just improving our underwriting models and our operational getting operational efficiency, that that's where the biggest value add, at least in the near term, is being created for us. While we continue to think what else we could be doing. So, the ways in which we are using AI very effectively is, you know, I already mentioned like 2 different underwriting models, one looking at the bank transaction data, tagging it in real time in a matter of 10 seconds and coming up with a credit limit. And I can explain to you what the biggest challenge AI has solved there.

Sahill Poddar [00:36:47]:
So, if you think about looking into a bank transactions, a few different things are tricky there. Firstly, using sort of the older methods, which was regex and maintaining a dictionary and saying, okay, if I see AMZN, it's likely Amazon. I don't know whether it's a credit or a debit. If it's a credit, is it for a return or is it because I'm a seller on Amazon? Like, it's hard to know that. But I also need to codify that AMZN means Amazon. And so on and so forth. With AI and LLMs, you actually get entity resolution as part of the LLM intelligence, right? Like if you give it a set of bank transactions and say, tell me the entity, the counterparty for each of these transactions, it's able to do that very, very quickly and get it right. And so you can all of a sudden start to get entity resolution and the ability to basically back out into a P&L using a bank transaction history, you can categorize what is debt, what is expense, what is revenue, what is a mispayment, and start to build a very good understanding of the small business, which then flows through our next layer of intelligence, which is the Paraforma model, which kind of takes that sort of data which we have transformed into time series and then starts to project what the future cash flow of this business would look like.

Sahill Poddar [00:38:12]:
And so, in doing that, we've seen a lot of good wins. I spoke about the 2 agents. There's many others that we have. These agents are checking for fraud, for the debt load on the business, checking if a business is open. And if they are and we're not seeing any data come into the platform, we still have some rights to go and collect some funds from them. And so, it's being used a lot for our funding, risk management, and our servicing processes. And I think this is like, I would say, in the bucket of low-hanging fruit. Despite a lot of effort going into it, it is relatively low-hanging because it's just so adjacent that it just strengthens the core and helps us be more efficient and do more.

Sahill Poddar [00:39:00]:
And then the next set of questions is like, okay, what is the product experience we can provide given that we have compounding advantages in capital markets, data, underwriting, deep platform relationships? And so, we've tinkered with ideas. I think, you know, they all sort of fail the test of whether it is saving the business both time and money, and paraffin has a right to win in that category. There's definitely many that fit in the former bucket, but we don't think we necessarily have a right to win in that category. The moment we do, you'll see that as a new product line from us.

Nic Poulos [00:39:39]:
And have you seen, I mean, you know, on the pod, we've talked, I think, ad nauseam about, you know, SaaSpocalypse and people's view, hey, is what's more exposed, horizontal or vertical? I mean, have you seen any shifts in the kind of health or direction of your vendor partners as a result of AI? Or, you know, given your targeting, larger, more stable platforms, not as much.

Sahill Poddar [00:40:08]:
Yeah. So I think what is observing and just about the market environment today, I have friends at the 2 labs and just kind of thinking through how they're thinking about things. They actually want every single workflow to be in the chatbot. They want everything connected through MCPs and you're just doing all of your workflow. You're talking to Slack and, you know, your marketing tool, CRM, Google Drive, Notion, all at once in one session. And it's able to take information out of all of those systems and add the intelligence and then take some actions based on that.

Luke Sophinos [00:40:54]:
So in effect, they are kind of Their goal is they're the only UI layer. Everything else is headless.

Sahill Poddar [00:41:01]:
They are the only UI layer and every other platform is just a database. They're effectively rendering all of those platforms to be a database only where today, like, I don't know whether like a Google Drive interface matters to me anymore or not. I can do the same thing in my Claude session. I can write the doc, take Claude's help to write something, and I can push it to Google Drive and it's created there. Right. And so They're trying to push those businesses to be database only, the intelligence and the UI to be owned entirely by Claude and OpenAI. And actually, the question for these businesses is, how do you prevent that from not happening? I think there's not a lot of good answers that are out there today. And while, you know, I'm saying this while we live in a time where the single largest venture exit is a vertical AI company, which is Cursor, right? That's the single largest venture exit in an M&A capacity, of course, not public, but not in a public capacity.

Sahill Poddar [00:41:55]:
But, and we're seeing like some very large businesses being created in the legal space, in the healthcare space. So the question is just like, you know, how does this pie get divided? You know, does Anthropic and OpenAI and maybe a third lab like win a lot of this, or does the pie get split? And I think the honest answer, I think how this would play out is the markets are just big enough that there can be multiple winners across multiple areas. And for every user who's using Anthropic or Claude to do their legal work, there's going to be one more who's using Legora and one more who's using Harvey. And then the pie will likely get divided for some of these markets. And for others, it won't. In my own usage, I have to say I am more and more only using Claude as the only UI layer. Like, having to open a web page to go to a different website is, at this point, it's like a bug. And so I'm happy just passing on all of my interactions to the one app and that being connected to all of the different data sources, because it just increases efficiency to a different level.

Sahill Poddar [00:43:04]:
Now, naturally, it is scary because it also makes me dependent on them. And, you know, as we all know, Fable 5 tokens are not cheap. But it's just so intelligent that the dependency is worth it, at least for now, for us. The other way I would say is like for vertical software to differentiate is to move away from being pure software. Now, it's easier for others versus not. Like, you know, we are not vertical, we are a horizontal business, but we have such a huge CapEx and our GTM is so nuanced that it's very difficult for an AI-only company to compete with us. Like, we are a business where the history matters, scale matters, having a relationship with Goldman Sachs matters, taking 6 months to raise a massive debt facility matters. And having like $2 billion of capacity versus $20 million of capacity to fund loans makes a big difference in the market.

Sahill Poddar [00:43:56]:
But I think this is less true for some pure software businesses. But look, challenge is also opportunity. At the same time, you have a Cambrian explosion of capabilities and the speed at which you can build things. And so, yeah, I don't have any— very definitive outlook, but I can tell you that my own session, my own workflow is very much very cloud heavy today.

Luke Sophinos [00:44:24]:
Okay. This is fun. This is like getting into what's going to happen in the future, which I love. And so, I don't know if I, I think I've shared this with Nick before, but I did a write-up on this because I'm obsessed with where the world's going. And it's interesting to hear your perspective, but if for our Game of Thrones fans out there, It's my view is there's 7 kingdoms of AI, right? And so, how I'm thinking about it is there's a consumer winner, right? And we're talking about like the AI UI, who wins that? And the consumer, it's OpenAI. I think Google probably comes up in there. Maybe Meta is dark horse. And then you go into like a business AI, more general business, which everybody on this call is probably all in on a Claude or an Anthropic or Perplexity or something, or an OpenAI or something along those lines.

Luke Sophinos [00:45:18]:
But I think where this fragments and why I think Paraffin is in a really good spot, and obviously we're all biased because this is the Verticals Podcast, but is I don't think that necessarily proliferates down into all the independent kind of verticals. I think it's going to get really hard to actually build and, you know, Sahil said this, like you see that in the legal tech space, you see that in healthcare, but those are big and broad, right? And so there's 1,000 other niches that are even below that, that I don't even think it necessarily makes sense for the big dogs to get into. So Nick, what's your view? Like, do you agree with this view of the world?

Nic Poulos [00:46:03]:
I guess what I'd say is, yeah, I mean, look, the value of UI, I mean, UI has become more or less fungible. I mean, I, some things I use only Claude for, other things I have built my own UIs to interface with because the truth is like text is not a great interface for everything. In fact, it's a really bad interface for a lot of things. And so, you know, like that.

Sahill Poddar [00:46:29]:
Yep.

Nic Poulos [00:46:29]:
For SMBs, I mean, there's like, honestly, Like even voice is not, I mean, there's a reason why we developed UI in the first place, right? Because you can't fly a 747 through a text window, right? And like, so I think like if your platform is predominantly just UI and database and that's all you got, well, yeah, it's probably gonna be a tough road once your users get sophisticated enough to get on one of these platforms. I don't know that I feel like it's gonna be one or the other because the truth is like, Okay. Today it's Claude. Um, 2 years ago it wasn't. And now we just had Kimi K3 that came out and, you know, the, the kind of frontier open weight gap is like 4 months. So I don't know. I mean, I love Claude, but—

Luke Sophinos [00:47:16]:
The cost, by the way, 90% cheaper.

Nic Poulos [00:47:18]:
Right. And so like, I, I love Claude. I think it has the best like disposition and the harness is nice, but like, How much am I like 10% price difference maybe? So I think like it's very uncertain to me right now who owns the infrastructure layer, and I question that the outcome of this infrastructure landscape looks exactly the same as it did for cloud. But on the application layer, I think it's going to drastically expand the opportunity. I think just like with cloud, internet, PC, mobile, it's going to be diverse. But yeah, like Sahil said it best, like, you got to figure out ways to add value to your customer over and above the like baseline generalized intelligence that these platforms can offer. Whether that's lending or proprietary data or abstracting, like just abstracting what humans do and isn't written down is like enormous.

Luke Sophinos [00:48:19]:
So that's kind of the through line that I'm picking up on from this conversation is Sahil said 2 things that I think are really interesting. Well, he said more than that, but 2 that really marry these together. One being, hey, our best customers, the ones that are ripping, are basically collective bargaining agents for their consumer, and they almost look like franchises, right? And then the second piece of it is, hey, they're trying to do more than just software, right? They're offering services. They're offering I mean, Slice, they're offering pizza boxes, right? Like they're, that's, that's how you just wrap this moat.

Sahill Poddar [00:48:58]:
Yeah. That last point, Luke, I think is a very interesting one. If I were to generalize it in, in, with, you know, with AI, if it's white collar, AI is coming for it in a very hard way. But if it's a, if it's a platform meant for, you know, what typically would be blue-collar businesses or that industry, it's very difficult for AI to come for it. Because if it's white-collar, you know, like legal is a great example, everything that is worth knowing is written in some document that AI can read. But when you kind of look at the traditional SMB segment, like you mentioned the pizza boxes, like that's something, that's an insight that only a person who's actually observed a pizza shop will learn over time that, hey, this matters to these guys. And if I can provide a good experience, I've created a valuable service for them. Another example that I learned from our partners at Jobber, which is in the home services space, is that guess what? A lot of home services businesses, they miss appointments because they are doing things with their hands all the time.

Sahill Poddar [00:50:02]:
So they're not picking up their phone. And so they created a bot, AI bot, that just helps them confirm appointments. So people can call in, there's a bot that will look at their schedule and confirm an appointment, keep adding them to the calendar. Very easy way to increase revenue, get more bookings which will otherwise be lost, and just a much more powerful bot than a traditional voicemail would be. And so that's again an insight you have to be operating in the home services business to know that, and then to kind of parlay that learning into a feature that is adding value to the customers. And so the, the— I think traditional, if you're building in the traditional small business space, blue-collar space, You know, AI is a huge tailwind, but if AI can learn everything by reading a document about the industry that you're in, then, you know, there's going to be a considerable headwind.

Luke Sophinos [00:50:49]:
I almost look at it like a screen time axis, like less blue collar, white collar, and more screen time because we had the founder and CEO of Magic School on the pod, teachers, right? One of the biggest, fastest growing AI companies out there. He scaled to like 4 million teachers. And I would have thought that, that like, why can't the teacher just use ChatGPT? Right. And, and his view was like, look, teachers are on screens for like 30 minutes a day, 60 minutes a day. They're in front of the class the rest of the time. And so just basically tailoring AI to be directly correlated to what a teacher is doing has created like massive tailwinds for them. So it's an interesting like thought process. Like where does it help? Where does it hurt?

Nic Poulos [00:51:37]:
Yep. Yep.

Sahill Poddar [00:51:38]:
I think screen time is a great way of putting it. Written knowledge is a great way of putting it as well. If that knowledge is written versus just in the practice, then it's going to be difficult for AI.

Nic Poulos [00:51:48]:
I really like that lens. And I think it's also instructive that, you know, legal and finance are the 2 verticals that the model labs have at least either gone into heavily or rattled their sabers around because it's theoretically a known system. All laws are written down. Accounting is a visible system. I do think that even within white collar, there are a lot of functions that even if there is kind of a visible corpus of information that like the nuance that determines winners and losers still kind of lives in like, you know, know-how, if you will. And that hasn't fully been abstracted yet. Like, I think compliance is a pretty interesting one. I mean, Norm AI just raised a big round.

Nic Poulos [00:52:38]:
Like, compliance is very deterministic theoretically, but what actually gets enforced and what the outcomes are, maybe not as much. So yeah, it's interesting, but I really do like that. You know, is the knowledge institutionalized and publicly available? If so, that's probably not your moat.

Luke Sophinos [00:52:59]:
Kudos to Paraffin though, because Sahil predicted it perfectly, you know, 6 years ago that said, I'm going to be the embedded finance for verticals because now verticals are all the rage.

Nic Poulos [00:53:11]:
Yeah. I mean, you guys are also on the forefront of like, with all this open weight stuff, I think you're going to see a lot more people I know you guys have more than just language models, obviously, in what you're doing, but yeah, like playing around with fine-tuning and trying to own at least slices of the model layer.

Sahill Poddar [00:53:29]:
No, for sure.

Luke Sophinos [00:53:30]:
For sure.

Sahill Poddar [00:53:31]:
And I think just to add to your white-collar, I think the hardest white-collar job that remains is sales. It's difficult enough to sell as a human, let alone AI trying to do that. So that's what I tell my go-to-market teams is like, in the business, they're in the business of building relationships and nurturing relationships, and that's not going anywhere.

Nic Poulos [00:53:53]:
I think that's a good point.

Luke Sophinos [00:53:55]:
Let's wrap it up with a few rapid fires here, if you don't mind. I can kick us off, Nick, if that works for you.

Nic Poulos [00:54:04]:
Yeah, let's jump in.

Luke Sophinos [00:54:06]:
So first question for me, and then we'll go to Nick, is favorite vertical right now?

Sahill Poddar [00:54:13]:
So, in terms of favorite vertical, look, it's difficult to pick. You know, at Paraffin, we touch pretty much every major US vertical, you know, relative to its distribution. So, for instance, restaurants are a massive vertical. So, I'd probably go with that.

Luke Sophinos [00:54:28]:
It was a loaded question because I wanted to figure out which company was ripping the best with Paraffin.

Nic Poulos [00:54:36]:
All right. I'll—

Sahill Poddar [00:54:38]:
Yeah, it should be studios, but it is restaurants. So, that tells you that I need to work out more. And eat less.

Nic Poulos [00:54:47]:
Good advice for us all. Okay, I'll end on a more open-ended one. What would you say are like the biggest learnings or benefits to having a particle physics background to being a founder? Biggest overlaps, biggest differences?

Luke Sophinos [00:55:06]:
Common career track, by the way. Super common.

Sahill Poddar [00:55:09]:
Yeah, so pros and cons. Pros, I think experimental mindset. I think having done a PhD, my threshold for pain is very high. So, you know, you can endure the pain of an early-stage startup, although we're not one anymore. Looking at the world from just a very highly analytical worldview is probably another pro, especially in our business of giving credit, taking on risk. Cons, you know, in physics and in PhDs in general, perfect is better than done. But in startup land, it's the other way around. You'd rather ship and learn versus wait forever.

Sahill Poddar [00:55:53]:
Not everything is going to look completely right. But in the scientific world, like, you are trying to discover the truth. And so you want to make sure that everything is right. So that was a big adjustment for me.

Luke Sophinos [00:56:05]:
Okay, and then I got one more. Competition that keeps you up at night, is it the actual kind of end, you know, vertical software customer offering capital on their own? Is it, you know, the Stripes of the world kind of moving into your lane? What kind of competition keeps you up at night?

Sahill Poddar [00:56:24]:
Yeah, look, I think for us, competition is a lot more than any one platform doing this. Today, community banks are doing this, not embedded finance, but they're also in the business of lending money. Large banks are in the business of lending money. But what we've noticed is that they actually just waste a lot of time for small businesses. They make them run in circles and fill out forms only to reject them and use their personal credit scores to underwrite business credit. Naturally, no business owner wants to commingle the two. It also leads to a lot of biases. So, it's not so much competition, but we are trying to create access in a system, in a place where historical systems have not done so.

Sahill Poddar [00:57:09]:
And so, we just want to make sure that we are good at that.

Luke Sophinos [00:57:13]:
When's the IPO?

Nic Poulos [00:57:16]:
Awesome.

Sahill Poddar [00:57:16]:
No plans currently, but someday for sure.

Nic Poulos [00:57:19]:
Beautiful. Well, lock in our allocation. No, so pleasure to see you, man. Always enjoy chopping it up with you and really appreciate you taking the time to join us and to make what we're doing at Verticals possible.

Sahill Poddar [00:57:35]:
Absolutely. Thanks for everything you do, Luke and Nick. It's been a real pleasure.

Luke Sophinos [00:57:39]:
Thanks, man. Appreciate it.

Nic Poulos [00:57:40]:
Likewise. All right, cool.

Luke Sophinos [00:57:43]:
That was fun.

Nic Poulos [00:57:44]:
Yep.