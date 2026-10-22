# Verticals: Forward-Deployed Everything

Published: 2026-09-03
Type: podcast
Summary: Quinn Litherland explains forward-deployed AI implementation in home services, balancing deployment, maintenance, expansion, product learning, and the risk of becoming a custom-services business.
Source URL: https://insights.euclid.vc/p/forward-deployed-everything-fde-quinn-litherland-revin-ai
Featured: Quinn Litherland
Archive episode: 43
Source file: Episode 43 - Quinn Litherland
Date note: Date of the linked published episode page, not the recording or Drive upload date.
Transcript note: Automated transcript preserved as supplied; names and speaker labels may contain transcription errors.

## Transcript

Luke Sophinos [00:00:00]:
AI is eating industries, but most teams ship software and wait for adoption. The best operators are embedding forward-deployed teams directly into the businesses they serve. But there are traps, a lot of traps. Done wrong, you can become a costly services shop, or you can have people running around with their heads cut off. Chaos, no ownership, no product. This week, Nick and I sat down with Quinn Litherland, founder and CEO of Revvin, a company building verticalized automation for the home services industry. They serve HVAC, plumbing, roofing, remodeling, and more. And we went deep on how Forward Deployed actually is working in practice and where AI in the trades heads next.

Luke Sophinos [00:00:39]:
Let's get into it.

Nic Poulos [00:00:40]:
Welcome back to Verticals, everyone. We are excited for a show today with a fairly old friend in a sense, Quinn Litherland. He is the founder and CEO of Revan. Quinn, what's up, man? How you doing?

Quinn Litherland [00:00:51]:
Hey guys, thanks for having me on. Excited to be here.

Nic Poulos [00:00:53]:
Thanks for joining us. We're dropping on a Wednesday but recording on a Sunday here. So, you know, Quinn is in the office jamming on a Sunday, you know, 996. Dude, good on you. Of course.

Quinn Litherland [00:01:05]:
Yeah, thanks for having us. Yeah, love the podcast and listened for a while. So, this is cool to be on the other side of it.

Nic Poulos [00:01:11]:
Amazing. Well, you know, we expect you to ask us questions too. Keep us on our toes here. And I know it'll be a good one. But for our listeners out there, why don't you just bring us up to speed on what you've been up to, Revvin, what you're building?

Quinn Litherland [00:01:24]:
Yeah, totally. So, Revvin is really deeply verticalized. automation for home services. So think really large HVAC, plumbing, electrical, roofing, home remodeling. We're starting to break out into a few kind of smaller tangential industries like pool services, but really our bread and butter is HVAC, roofing, and home remodeling. Around 2 years old, based here in New York. We've raised just over $10 million so far. And yeah, it's, I mean, as you guys know, it's such a cool space.

Quinn Litherland [00:01:53]:
Such a huge industry, like $650 million plus. And there's just so much change happening. So I'm, I'm, yeah, excited to dig into all the crazy things that are happening in our industry and yeah, excited for the chat.

Nic Poulos [00:02:03]:
Amazing. Well, we were chatting a little bit before this about just how the structure of startups are changing in this, in this AI era, maybe as kind of an entree into that. And then I know we, we all have some questions for each other, but as an entree, could you give us a sense for like ACV, like what kind of sale you're making just so people can kind of Yeah, totally.

Quinn Litherland [00:02:26]:
So again, let's do like a quick history lesson on home services. There's like 2.5 million home service providers across the US. Of that, of course, there's a massive long tail that we don't service today. We probably eventually will, but for us, what matters most is like building our internal automated workflows. And we found that the best place to do that and embed really, really deeply is mid-market to enterprise. So, I mean, our ECVs are anywhere from $1 million to $10 million. $70K to $250K. And then our customer sizes, yeah, range from your $25, $30 million mom-and-pop business that's just been around for 30 years, is servicing their kind of wider regional homes or even their state as they've just now grown.

Quinn Litherland [00:03:04]:
Maybe they've done some early acquisitions, especially if like the kids of the owners have like stepped in or like, hey, let's see how like big we can take this. And then we also service pretty large private equity platforms. So the Vertexes of the world who will do $600 million plus and have 25, 26 different underlying brands and portfolio companies that we work with. And so yeah, for us these are big, big operations. And so that's honestly like the fun part of building super verticalized workflows into this space. Like we talk about it all the time in the office of like we get to partner with these incredible operations and with these incredible operators and like help drive millions and millions of of like net new revenue to their bottom line that they're either missing or they're not able to go after it because they don't have the resources or just like leaking within their funnel. And so, yeah, it's pretty cool to be jamming with an operator and they're like, wow, like we have $5 million more to play with this year because of you guys. And it's pretty cool to see the impact.

Quinn Litherland [00:03:57]:
Again, it's, yeah, the whole other thing we should talk about is like pricing because right now it's like, all right, if we're driving $5 million to your bottom line and we're only charging you $70K, you're like, okay, maybe we should be charging more. And so, We're thinking more and more around what that looks like. We charge based off of workflows and then volume. So of course, like, as an operator scales on Revvin, they're buying more workflows and they're buying more volume. And so like, we are definitely incentivized and like paid really, really well as they expand on the platform. But yeah, as we start like shifting more and more towards like an automated linear workflow to really what we're doing, which is, okay, how do you sell a $30,000 roof over a 4-week period? period across an omnichannel experience, across SMS, email, and voice, that you have to maintain memory and contacts. And that's a really, really hard problem. That's what we've solved really from the get-go.

Quinn Litherland [00:04:44]:
But that's much more like a human and an employee than just an automated workflow. And so as we're getting more and more towards like, hey, we are your autonomous AI employee stack, we're starting to see our LTVs continuing to grow. And yeah, I think we'll be at a point where our LTVs will be, for some of our customers, $1 million plus. just as we start like becoming their full end-to-end action layer across the front office, which is pretty crazy.

Nic Poulos [00:05:05]:
Question for both of you guys, like how are you seeing, you know, the structure of an early-stage startup, like who you need to prioritize for hiring, who you look for in those roles? Like what do you think are the biggest changes that are happening? Because like, you know, Luke, you built a company more or less pre-AI and now you're working with a lot post-AI. Quinn, you've, you know, you're kind of navigating it real time. Yeah. So what do you think are the biggest changes?

Quinn Litherland [00:05:31]:
Luke, do you want to maybe take first stab at that of like pre-AI era and how that shifted?

Luke Sophinos [00:05:35]:
Yeah, I mean, for sure. So pre-AI, I think most founders are doing an incredible, actually disservice here. We're taking old org charts that made sense in the SaaS era where you got a product manager, you have a team of engineers, and the product manager's job is to talk to the customer, you know, go tell the engineers what to build. And it's just a natural game of telephone where you, you know, a lot gets lost. The Ramp founder was on recently talking about the, Bevel Toaster. Do you guys see this? And I love it.

Nic Poulos [00:06:03]:
What was it?

Luke Sophinos [00:06:04]:
The Bevel Toaster. You're like, Luke, where are you going with this?

Quinn Litherland [00:06:06]:
Bevel Toaster.

Nic Poulos [00:06:07]:
I like it.

Luke Sophinos [00:06:08]:
It's like the most pristine toaster. It's $500 or something absurd. The founder's talking about how if he did everything that the customer asked him to do, the toaster would have 1,000 buttons on it, right? Like a little crispy, extra crispy, black, dark brown, whatever. And so he made one button outside of the dial turn that's just a little more, right? So he encapsulated all of that into one button. And so I think a lot of vertical software companies in the AI era, the ones built before, are thinking, I just need to add AI, and their interfaces are becoming 1,000 buttons on a screen, right?

Quinn Litherland [00:06:40]:
Yeah.

Luke Sophinos [00:06:41]:
And so like, I'm working with one company right now. They have the domain expert that's actually vibe coding the UI layer, right? And getting exactly what it needs to be and sitting with the customer and literally vibe coding real time on what it should look like. And then they're handing that off to engineers to make it scalable. That's just one example of how I'm seeing people do this, I think. a very different way that will, you know, it'll have serious org chart implications. But Quinn, love to hear what you're doing.

Quinn Litherland [00:07:03]:
Yeah, I think it comes down to like, what are you actually solving when you're a vertical AI company? Like for us, we are building labor. Our workflows and our agents are employees to these businesses. And it's really hard to be a remote employee who has no idea about a company, is not onboarded very well, and then expected to like run the operations. Like, of course, that just like won't work. I think we see this a lot in our space and in other vertical spaces that like I spend a lot of time in. You have these teams who are like super, super smart builders, and maybe they even have like a good growth motion, etc. Maybe they have a couple good distribution channels, but from like a pure product perspective, they like really struggle. And then they'll like layer in this forward-deployed motion, which is great because yes, you're starting to spend more time like manually working with your customer, but if you're not like on-site— like, like we're on-site all the time.

Quinn Litherland [00:07:48]:
We were just in Ohio this week working with like a $250 million home remodeling business. It's like if you're not really like becoming an employee of your customers and then building these workflows around like their very clear operations, you're always gonna be surface level and then you don't really have the moat. You're not embedded deeply enough where you're able to learn from their data, from their workflows. And it gets so embedded, like for us, it's, we get so embedded so quickly because we go so deep on like the first day that a customer goes live that it becomes like really hard to like rip us out because we are like running your business. And so, yeah, I think zooming out, I think your forward deployed motion is really important. I think it's also important of like, where does that sit in your org? Like who runs that? Is it under product? Is it under engineering? Like who's managing that workflow? And it's like, if it's under engineering, is your engineering leader product-centric enough to like learn from your team who is in the field, like giving you insights of like, hey, this is what our customers actually want. And so something that we've been spending a lot of time on, our opinion is that right now it should live within product just because you're getting so much like real-time feedback from the field every single day. And then I think a whole other question is like, how technical does this forward deployed or like AI deployment strategy role become over the next few years? Like our team's gonna be building a bunch of tools internally, like that's what we're doing.

Quinn Litherland [00:09:01]:
But is there gonna be over the next 12 months a bunch of new startups that are building software for this forward deployed motion that like makes their lives easier? And so maybe we can eventually just have like relatively non-technical individuals who are like now more of like a CSM account manager that are then in that role. And so it's something we're thinking through a lot right now. And I'd say I spend so much time talking to incredible founders who've raised so much money and they're just like, yeah, we just have a massive team of 4 deployed engineers. And they're like, that's something we just, we're basically just a services firm right now until we're able to find something that's more repeatable and that we can then scale. And so like for us, like that scares me a lot. And so we spend a lot of time internally of like perfecting this FDE motion. embedding ourselves so deeply within these companies, but then building like repeatable workflows for like every month my FDEs need to be able to take on more and more to prove that we're able to like get this level of scale because yeah, I don't wanna just be continuously hiring massive teams of FDEs.

Luke Sophinos [00:09:55]:
Yeah.

Quinn Litherland [00:09:55]:
And then we can get into this too, but with FDEs you have a huge expansion opportunity and like that's a big thing that we spend a lot of time digging into is yeah, how can we expand these accounts to go from $70K today to $1 million tomorrow? But yeah, I would say the FDE motion is like so critical right now. you're building vertical AI.

Nic Poulos [00:10:10]:
So one kind of question I have around for-deployed is that, I mean, obviously this, this whole terminology started around for-deployed engineers, which makes sense with implementation and makes even more sense because companies are moving so fast. They're often, you know, like they have design partnership, they want engineers in there to like figure out what to, what to build and just build it on site. Right. But a lot of the for-deployed roles that we're seeing across our portfolio are not just engineers. Right. They're handling like, implementation, as you said, they're like, they're product thinkers, they're de facto their customer success, right? In a lot of cases they're just straight up ops, like navigating the hierarchy. So like, is it really still just 4 deployed engineers and like who are you actually putting butts in seats with customers?

Quinn Litherland [00:10:55]:
I mean, it really depends on your product and your ACV and the vertical that you're in. And do you have a massive like expansion motion? Like right now, like we are, like I'm spending time with my FTEs this week training them on like how to manage upsell conversations with their accounts. And so it really just comes down to like, yeah, what type of product are you building and do you have a massive upsell motion? Then yes, absolutely. You need somebody who is a little bit outside of just like a pure engineer. And I think like the term's also changing. We're seeing more and more, for more and more teams use terms like AI deployment strategist. And so there's this like consultancy aspect to these roles where I think a lot of companies, like the actual buyers of vertical software today, are almost like expecting it. They're like, I don't want to be your guinea pig and I don't want to have to go through the pain of getting your automation to a point where it is actually working for me.

Quinn Litherland [00:11:46]:
So how are you going to help that? Okay, well, if you're going to provide me with this person who's going to spend time with me day to day perfecting your product, well, like, who are they? I want to meet them. And so it's like, it's like fundamentally changing a lot of even like the sales process and we're starting to see more and more operators Like ask for that. It's like, who am I gonna be working with day to day? Because I'm gonna want to be changing and making improvements to these workflows that I'm launching. So yeah, zooming out, I would say it really comes down to the space that you're in, the product that you're selling. For us specifically, yeah, our FDEs are in part engineers, but again, we've built a lot of tools around them. And a lot of the new FDEs that we have coming in over the next couple of months is like new employees. starting to see this trend of, yeah, they're becoming less and less technical. They more need to be really, really smart product thinkers, be really, really amazing talking hand in hand with a customer because again, like they're gonna be embedded in the trenches.

Quinn Litherland [00:12:39]:
Like one of our incredible FTEs, Paul, he manages a lot of our like upper enterprise roofing platforms. He could leave Revit right now and probably go run a roofing roll-up better than 95% of the folks that I meet that are in private equity right now. Like he just understands the space so, so well. Today, he understands exactly how these businesses operate. He understands what works, what doesn't. Yeah, I think you just have to go so deep to help your customers today.

Nic Poulos [00:13:03]:
What's his background?

Quinn Litherland [00:13:04]:
So he was running a service business before Revvin. He was in Austin. He was running a car detailing business, fully bootstrapped, doing it himself. He was like, got it to, I think they were probably doing like $500K or so a month. He started building tools himself. He was like, okay, don't love the existing systems. I want to start building this myself. Started to really, really love the building piece, less of the day-to-day detailing cars.

Quinn Litherland [00:13:27]:
Kind of got obsessed with that. And so started reaching out to companies like Revvin of just like wanting to talk, shoot the shit and see what he could learn. And so we, we got to know each other and I thought he was super smart. And so we got to just kind of talking on a routine basis and eventually I was like, dude, you should just like come to Revvin. He was thinking about selling the detailing business. And so he eventually did and he exited that and then he came and joined us. Again, this is also like why he's been so spectacular because he understands it. He like speaks the language.

Quinn Litherland [00:13:50]:
He understands what it's like to run a services business in the first place. So he's like deep empathy for these operators. And then for him, it's so cool because he's now able to be this like CEO of, I don't know, he probably manages across all of the accounts that he works on today, like a couple billion dollars of enterprise value in the roofing space. And so he gets to be like working with the C-suites of these businesses, deploying automation into these like critical workflows, driving hundreds of millions of dollars to these companies. And so I think him coming from the space and being able to like embed himself so deeply has been so cool.

Nic Poulos [00:14:21]:
So.

Luke Sophinos [00:14:21]:
It's almost like the profile is like a founder profile.

Quinn Litherland [00:14:24]:
100%.

Luke Sophinos [00:14:25]:
Like you need to be able to do implementation. You need to be able to do cross-sell expansion. You need to know the industry. You need to be social and be able to talk to people and have empathy for what they do. Nick, what are you seeing across your portfolio with this? Because there's, I mean, there's so much noise around forward deployed. I saw a funny, there was a, in one of the recent earnings calls with Palantir, who obviously made this whole model famous. I can't remember if it was the CEO or the CTO, but they were making fun of everybody else trying to do this. And they were just saying, they're all just sales engineers dressed up.

Luke Sophinos [00:14:56]:
Nick, what are you seeing? I'm curious to get your take on it.

Nic Poulos [00:14:59]:
I think it does, to Quinn's point, I think we're seeing something a little bit different based on whether you are going after, you know, multimillion-dollar enterprise contracts to start, or whether you're starting with more traditional kind of what you might have previously thought of as like transactional SaaS ACVs of $50K. And that doesn't mean one can't turn into the other, but I do think think like, you know, the math just works out such that if you're selling into a Fortune 10 company, like you can afford to have 3 people.

Luke Sophinos [00:15:28]:
Probably.

Nic Poulos [00:15:28]:
Probably including the founder who are like, you know, 1 or 2 of them are there on site and the CEO is there like every other week just holding their hand because especially at the early stages where, you know, we're partnering with founders from inception, like half of it is you're figuring out what you should be building. I mean, it's like you're learning as much from them as they are from you. And so that's part of the benefit is just this is somewhat driving. It's like historically you used to say, okay, I'm going to build a SaaS product. I got to know what to build and I got to take that risk to spend money to build it. And then my reward is that like if I do, I get product market fit, I get revenue, and it's hard to repeat that. Now it's kind of like, well, I know generally where I'm going in terms of what I want to build, but Like let's just get in there first. And you know, maybe you have, Quinn, I mean I met you early on, like you have the vision, but the details, you know, are being figured out along the way.

Nic Poulos [00:16:24]:
So I guess what I would say is founder-led sales is more important than ever. In a lot of ways the founders are, and they're not just selling, right? They're also like getting more deeply involved in product. I'm seeing engineering, like it's as important as ever, honestly. It's like a lot of people talked about, oh, teams can do more with less, and that's true.

Quinn Litherland [00:16:42]:
Yeah.

Nic Poulos [00:16:43]:
but they're also scaling faster. And you gotta get people who are able to understand like what architecture we should be building for years, not just the next 6 months. I mean, that's, so that's been a big, a big thing in the portfolio is like really finding great founding engineering talent and finding folks who are great fits because it's not, it's not just like simple anymore. You know, you gotta wear all these hats. And I wanted to show you guys, something I'd come across. There's this report. So there's this report, I think it's like an HBS and Penn or something, and they did this whole breakdown on like AI-native companies versus ones that weren't and kind of what the team looks like. And, you know, there were a couple of like a couple of learnings.

Nic Poulos [00:17:27]:
I mean, one was that, you know, about, I think they were on average AI-native companies were like 25% smaller or something. But I thought one of the most interesting was looking at the number of hierarchy layers. And what they found was that AI-native companies were much, much flatter. In fact, you can see here in this histogram, right? Like most of the AI-native companies, over a third of them literally were completely flat. And it just, it rang a bell when you guys were talking about the, you know, kind of the element earlier around just the forward-deployed person being like a founder. I think in a lot of ways that's true.

Luke Sophinos [00:18:04]:
There's almost 2 traps in this too, that at least I'm, that I feel like are through lines to this conversation. The first trap is what Gwynn talked about, which is, hey, how do you make sure you don't just turn into a services, you know, factory, right? And that's a real trap. And I think a lot of people are just avoiding it as long as possible. And it's like they're, you know, they're just getting funded. They're basically leveraging VC money to run a services playbook and with the hopes that eventually they can automate those internal roles that are people, right?

Nic Poulos [00:18:32]:
Yep.

Luke Sophinos [00:18:33]:
The second trap though, is almost more interesting to me. It's like, how do you ensure that you don't get to a situation where everybody is, is quote unquote forward deployed and like everybody, you know, and it's across sales and it's across the CEO and it's a little bit of the first bucket, but it's almost just like an excessive amount of time and chickens running around with their heads cut off. Like, Quinn, what are you seeing on the ground? Like, how do we, how are you thinking about both those and ensuring that you don't fall into either of those camps?

Quinn Litherland [00:18:59]:
Yeah. It's a really good call out because it is 100% an excuse not to build great product or repeatable systems. That's the hard truth of it. It's like, it's a necessary evil in a lot of the, in a lot of ways, just as like products get good enough to actually be fulfilling the promise that they've made to customers. And so it makes sense that teams like us are doing it. But if you're not thinking about, okay, what does this look like 2 years from now? How are we building internal software for our 4 deployments? It's just an excuse to, yeah, lean heavily into the services model. And I think a lot of teams are actually gonna be kind of screwed, honestly, because again, I think this is like a wider dynamic in the market right now. Like no one's coming to save you.

Quinn Litherland [00:19:37]:
Like the venture market's so weird. It's such a weird time. I think teams need to be a lot more intentional in terms of like where they're spending their cash and how they're actually building like repeatable workflows and repeatable product versus having this grand vision, but then having like insane costs around it. around the human beings that they're sending on site to go and like actually just like do the work that they're promising the product should be able to do. And so—

Luke Sophinos [00:19:58]:
Can you give us an example of when, like, of a specific workflow in HVAC where, you know, you started with this like forward-deployed heavy services piece and, and over time you've gotten it to a repeatable workflow that AI can handle, hopefully all of, or at least most of?

Quinn Litherland [00:20:13]:
Yeah, well, really it comes down to onboarding and setup and Implementation and then maintenance and then expansion. So for us, like, let's say we're, we're talking to Nick's Home Services. You guys do plumbing, electrical, and HVAC. You are $50 million. You're probably on, at that point, you're 100% gonna be on ServiceTitan. Okay, great. Well, you're probably gonna buy from us our after-hour call answering system, but really your, your inbound speed to lead over SMS and voice. Okay, great.

Quinn Litherland [00:20:39]:
Well, again, you go back a year ago, we were coming on site and setting all that up. Like from scratch ourselves. Today we've built out this full agent ecosystem with templates and workflows specific to, hey, you're a $50 million HVAC business. Here are the semantics and nuances you're gonna run into. We like 99% of the time, we already know like what your qualification process is gonna look like, how you want us to handle job type matching and integrating directly into your system of record. And so like all of that has now become like very much repeatable. Again, there's still a human being helping during the onboarding process and making sure that everything is getting spun up properly. But now we've really been able to automate that.

Quinn Litherland [00:21:14]:
And so, okay, that's awesome. So for us, it's like we can take a customer live so, so fast and launch these automated employees that are just absolutely crushing it for our customers. I mean, like every day we take a customer live and they're like, you guys are now the number one performing call center rep in our, in our company. This is insane. Like, like, okay, where can we go from here? And so I think this is where folks get into trouble. So you have this one workflow that's working really well. Great. Congrats.

Quinn Litherland [00:21:40]:
Well, your customers are gonna want more from you. Like they're gonna want you to start cannibalizing more of their workflows if you're already doing a great job on one or two of them. And so for us, then it's this like really tough question of, okay, like what do we wanna commit to? Do we wanna expand this account? Do we wanna launch this new workflow? But again, it's, we might not know that workflow very well. There might be new systems we have to touch. There might be additional data sources we have to tap into. The process itself might be actually like quite technically complex and we have to spend some time iterating on actually figuring that out. And so for us, this is again going back to this, like when you're an FDE, you are the CEO of your book of business that you're managing. And there's this like constant balance between here are the workflows that are repeatable, here are the ones that aren't that we're scoping.

Quinn Litherland [00:22:20]:
And this is also why I think the forward deployed motion sitting under or like tangential to product is really important because if you're in a really good vertical, where there's a ton of expansionary opportunity like ours, where again, like, we believe in the very near future you're gonna have these almost like headless companies where you're gonna have the C-suite and a system of record and then your actual like sales staff and technical staff, but the entire operating unit is gonna be a bunch of agents. So you might just still gonna have your CMO, your CEO, your COO, and your CFO, but those individuals are gonna be like hyperpowered by automation that's handling all the internal minutia day to day. And so long story short, I think for us, we've been able to really do a great job of systematically building these really templatized workflows based off just going so deep into these businesses. So we can go and say, hey, you're a roofing platform. Awesome. You're this size. Okay, great. This is what you need.

Quinn Litherland [00:23:13]:
This is what you're looking for. And again, there might be some back and forth as we customize the workflows or agents for them. That's what the FDEs are But we've just hyperfixated on how do we templatize this? How do we make this scalable? And the part that I don't have a perfect answer to yet is just as you expand, how do you make sure that you don't lose trust by overpromising, overcommitting, just being there and saying, yeah, we can build that, we can do that, we can handle that workflow as we just cannibalize the full end-to-end customer experience, right? As we start going more into back office workflows as well, which is super exciting and customers are desperate for it. It's just this balance of, okay, yeah, from a product and roadmap perspective, are we ready for that or not?

Nic Poulos [00:23:48]:
I mean, I'm sure you guys have seen that, you know, OpenAI and Anthropic have now launched and spun out these implementation companies, uh, DeployCo at OpenAI and Ode at Anthropic. And, uh, I think a lot of people have looked at that and said, oh, look, like services, like pure services is going to be the business. And like truthfully, those and others may be very successful in kind of the near term. But I think what a lot of times people forget about those is like the incentive there is to drive more usage of model labs, right? And so if they go in and they're paid $10 million to build something and leave, like that's still a success for them. For most startups, that's not a success, right? Like that's just a validation that your additional margin above the AI infrastructure was not like, was ephemeral. And they can't do it again. Yeah, yeah, exactly. Like, so if you want to be like if you're not doing what Quinn just described, you are basically an implementation company on behalf of one of the model labs or OpenWeight models.

Quinn Litherland [00:24:46]:
But I think that's also like why they're doing— like a big part of why they're doing this is also like protect themselves because they're looking at each other going, okay, 100%, we want to own this vertical layer. And we want to make sure that every company on earth is using our models versus theirs. And so yes, it's great and we're gonna provide incentives and we're gonna invest in companies. We're gonna make sure folks are using our, our, um, our LLMs. But if the other guy's doing the same thing, it's like, okay, then we need to do more. We need to do more. We need to do more. And it's like, my hot take on this is like, I think you're gonna see a huge acquisition of OpenAI buying Sierra.

Quinn Litherland [00:25:19]:
So like Brett Taylor, who like, I think he still sits on the board of OpenAI at Sierra, and they're an awesome company. Like we respect them a ton. I think that's gonna be like a huge acquisition that's gonna happen over the I don't know, maybe in the next year, year and a half, as these labs just continue to battle each other on that like application layer. And so yeah, it's gonna be interesting of like how aggressive the labs will get on acquiring the application layer companies and then what that like balancing effect will look like as larger incumbents in vertical layers. Are they then gonna go on their own massive buying acquisition sprint as well? Because they're like, okay, well I don't want want a large lab coming in and buying up all the application layer companies in my space because then they're gonna come into my space and start saturating that more and more and potentially come after me as like the POS or the ERP or the CRM or FSM. I think we're gonna see a very, very, very interesting acquisition market over the next 12 to 18 months as the like incumbent FSMs and CRMs and these large labs are like trying to figure out What do we do with the application layer and how do we make sure that we are protected?

Nic Poulos [00:26:24]:
Dude, Quinn, I like, I completely agree with you. I personally, I probably see it as more of like a 5-year trend. I mean, not to say I don't think it could start immediately, but, you know, think about how many public software companies there are that frankly have no hope at building an AI strategy themselves.

Luke Sophinos [00:26:41]:
Because they're cheap as hell.

Nic Poulos [00:26:42]:
Now's the time to do it. I'm shocked that more hasn't happened. Like, It's crazy to me that like, you know, CCC was one of the first with Evolution and, you know, who we had on the pod. Like, I feel like we're going to just start seeing a drumbeat of these, like, you know, and it may, it may be like 500, 800 today, but like you said, Quinn, like it's going to get competitive, especially if you're like—

Luke Sophinos [00:27:02]:
More and more like we saw Procore bought, who was it? The agent company in construction.

Quinn Litherland [00:27:08]:
Yeah, we've seen a few, but that's a great example.

Luke Sophinos [00:27:10]:
We're going to see way more. You're right.

Quinn Litherland [00:27:12]:
I think what everyone's gonna realize, and this is also like relevant to the question around like all these underlying companies like building versus buying and everyone like so excited about building their own tooling, their own software today. It's like at the end of the day, and I talk to my team about this all the time because like it's hard. Like what we do is really hard. Like every single day we are trying to like deploy this brand new technology into old, outdated, antiquated businesses that have their systems that they've been on for the last 20 years and their internal workflows that haven't changed. And they have individuals in their call center who are fantastic human beings that have been doing the same thing for 30 years plus. Like, it's hard to change that.

Nic Poulos [00:27:49]:
Yeah.

Quinn Litherland [00:27:49]:
And I think right now everyone, everyone is, again, this is like my hot take that everyone has the blinders on of like, oh, this is so easy. It's so easy just to build anything. It's like, yes, but that's why we're in this like slop era right now. And so I think another take that I have is Folks are gonna start realizing how hard it is to do the things that a lot of vertical AI companies are doing. And it's not just product, like it's also relationship based and it's also like buy-in based. And how do you convince a company who's been doing the exact same thing for 30 years to completely destroy and blow up that process and also pay hundreds of thousands of dollars for it and then keep them happy? Like that's hard. And so I, I think a lot of the like CRMs and FSMs in the, in the space, in our space and other spaces as well. 'Cause again, everyone's trying to now become an AI company.

Quinn Litherland [00:28:37]:
And so yeah, I think everyone's gonna realize just how hard it is to do this from a relationship, from a workflow and process perspective, and then just from a pure product and AI perspective. And that's gonna be like another big catalyst for the M&A market. So yeah, I think the, yeah, I have a bunch of takes on this, but yeah, I think the M&A market's gonna get insanely frothy over the next 12 to 18 months.

Nic Poulos [00:28:54]:
We, we would all love to see it. Okay, so Luke, I want to get to your piece, but maybe just this kind of to put a pin in this one thing we've been dancing around. So I'll put this question to both of you guys. Like, where do you think this all shakes out in terms of best practices on for deployed slash implementation? And let's just take the example of like a $100K ACV product to make it easy. It doesn't have to be Revvin. What is best practice? Like, you send someone there and you cut it off at 3 months? Or you deploy one per customer indefinitely? Like, what is this right balance between the real spend of putting someone forward deployed and, you know, the learnings you're getting and, and all everything we've been talking about? Like, what's the right steady state approach to this? Like, do you—

Luke Sophinos [00:29:40]:
Such a hard question.

Nic Poulos [00:29:40]:
Cut it off? I know it's, it's like, I don't even know if there's an answer, but I mean, what are the contours of it?

Quinn Litherland [00:29:46]:
Luke, you wanna go ahead?

Luke Sophinos [00:29:47]:
I'll throw something out there. I mean, I think assuming it's $100K, I think I think Quinn, the profile of the individual at Revvin that he talked about is, is if I'm sitting in his seat is probably what I'd try to replicate. It's like, it's like, let me go out and literally instead of hiring a PM and an engineer and a CSM and, and, and doing the, you know, the 7 heads kind of model, right?

Quinn Litherland [00:30:08]:
Yeah.

Luke Sophinos [00:30:08]:
The pod model as we all did in the software, the SaaS days. It's almost like you gotta like pay up for an incredible kind of ex-founder, somebody that just has the broad skillset across the industry, across AI, can talk to the customer, right? And they, and they can ideally work with an engineer behind them that can, that can build the scalable architecture backend. Like that's where I think AI gets really hard. And I would try to replicate that and I would, I would, I'd figure out, okay, this person is a, is a unicorn. I'm gonna pay 'em $250,000 to $300,000 a year, um, and give 'em some commission additionally. Like they're gonna be crazy high paid, but it's gonna, Enable me to have 1 person instead of 6. And, and then I'm just gonna see how many, and I think Quinn said this, I'm gonna see how many they can support and then I'm gonna try to replicate that. Like that's, that's—

Quinn Litherland [00:30:54]:
Yeah.

Luke Sophinos [00:30:54]:
You know, and when I say support, it's like implementation, getting, you know, getting it to templatizing so we can make it scalable, expanding the accounts, right? Like, you know, if we're providing 10x the value, like let's make sure our pricing, you know, aligns accordingly with that, which is a problem for everybody right now. mentioned it. So I think that's like my at least day one starting point and then I'm gonna iterate after.

Quinn Litherland [00:31:17]:
Yeah, I agree with all that. Like for us internally, our mantra is how do we deploy? How do we maintain? How do we expand? And how do we do that in a sustainable way? Like those are the 3 pillars that we care most about. How do we get in and go live as quickly as possible with the highest quality outcomes that we can possibly drive? How do we then maintain that? Because you see this a ton. where a team will go in, just knock, like knock the socks off from a sales perspective. Founder will come in, razzle dazzle. Okay, amazing. You got the contract. Maybe it's $100K, maybe it's $250K, maybe it's a million bucks, maybe it's $10 million.

Quinn Litherland [00:31:48]:
Okay, well now we're gonna go live. Okay, great. But at one point, like Nick, to, to your question of like, do you disappear at, at month 3? Like that's where things get really scary. And so like, I'm really interested to see the renewal period and I'm very interested to see for a lot of these newer vertical SaaS companies, what their renewals are actually like and what percentage of customers actually renew. For us, like, it's extremely high because we're so fundamentally focused and obsessed with that maintenance and expansion. Because if a customer's buying more from you, they are most likely happy and you are most likely— you have successfully embedded deep enough where they're going, okay, you crush these 3 workflows, please can you go and do these 6 others? And so you have to take them live, you have to maintain, and then you have to expand. And then, yeah, the hardest part is doing that in a repeatable way. And this is where playbooks come in.

Quinn Litherland [00:32:34]:
This is where hiring comes in and finding the right people. There's a lot of ambiguity. And so, yeah, I think the, for us, the biggest struggle has been hiring of just like hiring the right people. 'Cause we'll bring in folks and they are smart, they have good experience, but they just like fall apart with the level of like intensity that goes into managing these accounts on a repeatable basis.

Luke Sophinos [00:32:53]:
I don't think that person though, Quinn, can go away. Like, I don't think that— that's where I'd push back is like, I don't think they ever go away. Just like a CSM never goes away.

Quinn Litherland [00:33:02]:
I agree. I agree. And this is where a comment that you made, which was so smart, and I 100% agree with you, and we are now like rethinking this model. I think Decagon does a great example of this. The incentive structure of your FDE team. How do you make sure that your FDEs every single day, they're walking into the office and going, okay, I can make a million dollars this year if I renew, if every single one of my customers renew and I get a small portion of that renewal. And if I expand my accounts, like if, if I'm Paul who's managing a $500 million business, it's okay, how do I get that account from $100K to $250K to $1 million to $10 million over the next 2 or 3 years? Because the incentive piece is so important.

Nic Poulos [00:33:40]:
Especially because in the long run, that team is also absolutely critical to product, right? And, you know, so if I had to agree with what you guys said, if maybe if I had to sum it, sum up how I'm thinking about it, it's like your CS effort is now structurally 50% more expensive. But I think in this market, if you're tackling the right problems, your ACV opportunity is at least double, if not more than that. And that's a worthwhile trade.

Quinn Litherland [00:34:06]:
Yes. It's like CS is no longer this just like massive cost center. Like I think if you can embed really well into this FDE motion. Like your FDEs like have a, like could have a, some form of like sales commission. And so I think there's just this like really interesting—

Luke Sophinos [00:34:22]:
Question.

Nic Poulos [00:34:23]:
Yeah.

Quinn Litherland [00:34:23]:
Yeah. Embedding happening within this FDE motion. And, and Nick, to your earlier comment of the graph you showed me of like having this flat ecosystem, I think that's also so important. Again, you have to, you have to find, find the right line where you don't have everyone's an FDE and we're not we're never fixing this and it's just running around with their heads cut off, which is super scary. But, again, being super, super tight with the team, you have a very, like, concentric atomic unit that's constantly talking. We're like, I want my FTEs to be able to, like, turn around and talk to product and be like, hey, I've seen this 5 times today. We have to find a solution for this thing. Like, I think that it actually, the FTE motion, and if we want to thank Alex Karp or whoever for it, but, like, I actually think it's amazing because it's gonna drive and incredible product.

Quinn Litherland [00:35:03]:
Like it will if handled well. I think we're gonna see like this like golden age of vertical AI and vertical software en masse over the next, over the next couple of years because we're like forcing ourselves to like actually understand these businesses. Like we're like in like middle of nowhere US and Canada every single week understanding these operators in a fundamentally different way than like I probably would've thought about it 2 or 3 years ago. And so I think we're actually gonna Like it's gonna drive much better product, much stickier product. And I think for investors like the two of you, I think that's great. And I think there's gonna be a ton of value accrued because of that if handled the right way. So, if you do it wrong, you're screwed.

Luke Sophinos [00:35:41]:
Nick, I wanna ask you a question because I think like this is one thing I'm struggling with is I think we are at least somewhat aligned on the bigger ACV tickets and what you can do. Albeit the one thing I didn't mention is if that, if you screw up that hire, It's like incredibly painful and incredibly expensive, more so than we've ever seen in software. So you have to like get the hire right. How do you do this in, you know, I have a business I'm working with right now, you know, thousands of customers, average ACV is $5K. Like, what do we do? Like, I, like, that's something I'm banging my head against the wall. And I'm curious, Nick, if you have Portcos you're seeing that are doing this, or like, you know, Quinn, you have friends or smaller customers, like, what does this model look like in that world? It's so hard. It's so much harder.

Nic Poulos [00:36:20]:
And these, I assume, are like hyper SMBs or—

Luke Sophinos [00:36:25]:
This example is retail storefront, but let's just say it's like, we can just go under sub-$20K bucket.

Nic Poulos [00:36:31]:
Yep.

Luke Sophinos [00:36:32]:
What do you do there?

Nic Poulos [00:36:33]:
Yeah, I mean, I think if a market is structurally margin-constrained such that they are just cheap across the board, that can be challenging. But I think what we're— here's one interesting thing we're seeing in our portfolio, and Gwynne, I bet you, you're probably seeing this too, like the willingness to pay for handling a workflow soup to nuts versus handling 90% of it, but it requires you to log into something, is incredible, right? It's like literally in, in some of these examples, it's the difference between like, I'll pay $10,000 to $20,000 maybe a year to like, I'll pay $100,000 easily. In a lot of cases, they're already paying consultants, you know, or advisors to do that, or fractionals to do this for them at those rates. And so for them, it's just like, it's— and it's not even It doesn't even have to be like a labor replacement thing. It's just being able to offload an entire process has a huge premium to it. So I feel like that's maybe one angle is like, okay, what are you actually doing? Take a step back and think like, what else is the org doing related to this to take it from 0 to 100? And can we do those things? And maybe they start out as services, but over time you can automate them.

Luke Sophinos [00:37:41]:
If the answer, let's say the answer isn't growing the ACV though, like obviously I think that's naturally going to happen, but there's going to be, and then Quinn, jump in here.

Nic Poulos [00:37:48]:
Sorry.

Luke Sophinos [00:37:48]:
Like I'm thinking like Slice is a good example, right? Like pizza shops. Can a pizza shop customer pay a vertical AI company $100,000 a year? You know, they're, most of those guys are doing half a million in revenue. Like it's going to be very difficult even if you do everything for them and you do it well.

Nic Poulos [00:38:03]:
Yeah, no, that's fair. I mean, but, but, you know, Alear did go from I mean, I'm going to paraphrase, like 5 to 30, right? I mean, he did, he did 6 exits and I think a lot of people would have said that would have been impossible. So yeah, like there's structural constraint based on like the average top line and average margin.

Luke Sophinos [00:38:22]:
Like, but what do you do with FTE today to at least grow the contract?

Nic Poulos [00:38:26]:
Oh, I see what you mean.

Quinn Litherland [00:38:27]:
I guess, Luke, real quick, one question I have is for this company, like what is the product? Like, is it a, like, is it an agentic platform? Like, what are they doing?

Luke Sophinos [00:38:34]:
Yeah, it's, it's your classic like ERP kind of end-to-end business management software for their space.

Quinn Litherland [00:38:39]:
Got it.

Nic Poulos [00:38:40]:
Yeah.

Quinn Litherland [00:38:40]:
I think right now what we see across the board is everyone, like the buyer today is directly aligned with outcomes. And so I think when I see and I talk to teams who are like, oh, our ACV is like $5K, like what do we do? How do we manage this? Like, do we need FTEs or not? I think my first question always just like, why is it so low? And is it because these businesses are just like super small? Like, okay, but like what else could you provide to increase their outcomes. And I think like even using the pizza shop example of like, okay, if a pizza shop is doing $500K, could you get them to a point of spending $100,000 a year? Like probably not on day one, but if your platform is like directly attributing to net new revenue, like for us, then maybe, maybe. Like for us, like we come in and like in the first month we might drive. This is what's so cool about at least what we do. And I'm not trying to make it all about Revint, but I'm gonna probably do that for the next 2 minutes. For us, especially because of the ticket size of our customers is so high, So we're like a roofing business who every new job is $50,000. Us coming in and on day 1 helping them close 5 new customers that they otherwise wouldn't have been able to manage or convert, or they would have fallen through the stack or fallen through their funnel, or they didn't have enough resources to go do an outbound marketing campaign, or estimates would have just fallen through because they didn't have enough inside sales to follow up.

Quinn Litherland [00:39:49]:
It's like, okay, well yeah, now you just helped us convert way more than we're paying you, and we now look into the We have 11 months left. This is awesome. Like, yeah, we're willing to pay for this. And so I think when I talk to teams that have low ACVs, it's like, what are the outcomes you can hit yourself and like align yourself with that increases free cash flow into these businesses? And then you can start charging more. But Lucio, you're saying of like, it's not around ACV expansion, then I think it gets really hard. And I think then it's a product question of like, why does this team have a product that needs FDEs to go and embed it into these companies at such a low ACV. It's like, it's almost like if they're not willing to pay that much, then you need to, as a product builder, get your product to a place where like you don't need to have FDEs. And I think that comes down to like alignment with your actual buyer and like the quality of the product.

Nic Poulos [00:40:35]:
I would also add, like, I think a lot of the times that can be a reflection of the fact that the business owner doesn't fundamentally believe that like the, the Neo ERP is going to move the needle that much on his or her business. But an ERP, like, it's an expression of the entire business. And so what I'm kind of seeing in our portfolio is really where the, like, low-hanging fruit exists in that business is kind of all the behavioral inefficiency that is built up in this business and how they're running. And that's hard to change day one. But like, we have a business, for example, that, you know, Their vision is to be completely headless and handle, you know, what in this case it is kind of a revenue-oriented process, but to handle it soup to nuts. And they feel like today we could do that. And in every single customer, we would be better than their current process. But they don't believe that because they've been doing it this way forever.

Nic Poulos [00:41:33]:
So the path they've been taking is we are using our product, which today is not headless, like there is a UI because that's what they're used to, but it is behaviorally nudging them to do that. So for example, they're not okay just saying, I'm gonna let some AI that I've never heard of take over customer communication. What they will do is say, hey, when you wake up every morning, every single response is pre-populated for you and you can just go through and click 'em. And the idea is that like eventually you're just waking up and clicking yes on every single thing. You build trust. and you can take it off their hands. And then that allows you to like actually make the business better. So long-winded, but like tying into Luke, your headless piece.

Quinn Litherland [00:42:13]:
And it's also where like the outcomes, like again, even right there, it's like you're paying more for outcomes. I think we're like, if you're like an out-of-the-box ERP, I think the biggest question is like, okay, how do you, like, I think we were past the point where you can, I think it's tough for teams if you're expecting just to be like a very static product. and not be involved in the actual automation of workflows. And so like, Luke, if I'm like talking to your team, and again, I don't know this company at all or like exactly the semantics of the situation, but like my first question would be like, how can you go one step above and actually own the action layer? And I think the action layer right now is like where the vast majority of spend is. And so I think for any team, it's what is the action layer in our industry? How can we build workflows that actually perform an outcome Closing an estimate, closing an invoice, sending an email, drafting an email, reaching out to customers, rescheduling, canceling appointments. Like there's just so much on the action layer, and I think that's where the most amount of spend is. And I think for teams that aren't aren't leaning into that, it's gonna be really hard because your competitor is, and then they own the workflow. And like my take is, if you own the workflow, like you're winning.

Quinn Litherland [00:43:15]:
If you own the workflow, that's the stickiest part because that's like the lifeblood of the business. Like it matters a little less in terms. of like where that data might be going and being stored. So owning the workflow in my eyes is like the stickiest part today. But I don't know, Luke, I don't know if this is— if you agree with this or not.

Luke Sophinos [00:43:28]:
No, I do. I think, you know, what, what this particular company had done is they basically came in with like the lowest cost solution, and then the market of other software ERPs kind of followed them. And so everybody's paying like hundreds of dollars, a few hundred bucks a month for the solution, but everybody's monetizing really heavily on payments flow, on like ancillary actions that are happening. And that's where their scale is basically rapidly rising. And so it's probably, it was probably convoluted for me to say $5K ACVs because that's accurate in just the software representation. But the real way to think about it, and you guys helped me get clarity on thought on this, so I appreciate it, is you need to, I need to wrap in the payments revenue and the ancillary revenue, even though it's not quote unquote SaaS-based business, to look at how I can actually streamline FTEs to get, even if it's not software revenue, to go get more transactional revenue out of those, the end customers when an action actually happens. Right. So super helpful.

Luke Sophinos [00:44:25]:
Nick, I want to, and Quinn, I want to dive into this headless thing because I think that's a good segue.

Nic Poulos [00:44:29]:
Yeah.

Luke Sophinos [00:44:29]:
I think like 99% of vertical software companies are trying to be the UI layer. We're going to have a research report come out and we asked, we had like, I don't know, close to 150 vertical software companies respond to it. And basically like 90% of them are trying to be the UI layer or remain the UI layer. I think field services is like an epic example of seeing this play out in real time because you have vicious competition to be the UI layer from ServiceTitan, from Housecall Pro, from, you know, I think Salesforce has like a field services—

Quinn Litherland [00:45:01]:
Yeah, they have their own FSM product now.

Luke Sophinos [00:45:03]:
Yeah. So it's, that's like a very tough to attack that. And I, but I still think most companies that serve that end market are attacking it like that. I think the beauty of what you're doing is you're necessarily not. So, so I guess first to you, Quinn, I'd love to hear like your methodology, your thinking around owning the UI layer and when it makes sense and when it doesn't. And then Nick, I'd love to kind of get your view as well on what you're seeing working and what's not and why everybody in vertical software is still trying to be the UI layer.

Quinn Litherland [00:45:28]:
Yeah. My take on this is I care a lot less around the UI layer. Like at the end of the day, we look at it as you have this, and I know I've mentioned You have, you have the CRM layer and the action layer. And for the last 20 years in vertical SaaS, or at least specifically in home services, that action layer was humans, right? You have human beings interacting with a system of record and then performing some other task. And then either some form of automation would pump data back into the system of record, or they would have to go and copy and paste it themselves. Now in this like agentic-first ecosystem, you have the system of action that is being run by the agent. Run by humans, and that's really cool. And it's really cool for a couple reasons because yeah, from a UI perspective, it's like okay, yeah, of course.

Quinn Litherland [00:46:07]:
Like I want to be able to like, and from a compliance perspective, I want to be able to like see the transcripts of the conversations, or I want to like be able to go back and see some interesting insights that the agent pulled from a conversation. And of course, I want to be able to see from an analytics and performance perspective how are my employees, regardless if they're human or or agents, and When I say agents, AI agents, how are they performing? And so of course, like there's still gonna be some level of, of a UI, especially on analytics. But at the end of the day, like the product itself, like our product, like the Revvin product, if you were to ask me like, what's the most important, like what is like the core, like atomic unit of the Revvin product that we offer? It's like, it's not a UI at all. It's our agents. Like people pay us hundreds of thousands of dollars a year for our agents because we have the best agents outta the box. We've built a ton of workflows so those agents are learning directly from conversations, are constantly improving, and we embed so deeply into the existing stack and existing workflows of our customers. And so at the end of the day, it's like the most important thing is not our platform. Of course, I can demo you guys our product and it's awesome and we've like the cleanest UI out there.

Quinn Litherland [00:47:11]:
And so again, I think we've done both really, really well and we have all the fundamentals of your agent builder and your testing suite and your eval suite. and your analytics and your conversation view for a live rep to then step in and, and join that conversation or live handoffs if needed and AI summaries and all that fun stuff. But at the end of the day, like I am, am like pretty, pretty certain that in the next few years the Revvin product will just, just, it'll just be operating. Like we will have like a very, very, very thin UI layer and the product itself will just be this agentic system that is powering your business. And I think you might be able to like talk to it. Like, like I'm, as an operator, I might wake up in the morning and be like, okay, Revvin, like let's plan our day. Like what's going on? What, what, what, like what are we fixing today? What customers are mad? Who do I need to call? And it's almost this like partner in crime for you as an operator. But I think we're gonna like fundamentally shift away from this like, oh, let me like sign into my dashboard and like, what do I have to do today? I think like products, especially like the best vertical SaaS products, vertical AI, products will become more and more just so action-oriented where they just run your business.

Quinn Litherland [00:48:15]:
And that's like, that's what we're building. We're building a product that's gonna run every single home service business, home service business in North America to start, eventually the world. And so yeah, my, my take is like UI is not a waste of time, but not the end. It's not the endgame. The only nuance, and then I'll, I'll be quiet after this. The only nuance, I think UI is an important short-term necessity to help train your agents with human-in-the-loop learning. And so for us, like a ton of what we do is like we've built all these internal workflows within Revvin where we're pulling in live reps to tell us, hey, is this a good conversation or a bad conversation? What would you have done in this situation? Hey, like we saw, we had this really interesting conversation where like we weren't 100% sure what to do. Like what would you have done here? And like we want to get those insights from our customers as quickly as possible.

Quinn Litherland [00:49:02]:
To train our agentic system. And so that's like the one thing where like a UI is important in the short term, just like pull all of that business context into our platform and into our agents. But once we're at a certain point where like we don't need that as much as we do today, then yeah, I don't, I think the UI will start to be less and less prioritized and we'll actually start decreasing the circumference of our, or the surface area of our UI. Because again, it's just something you have to maintain. And this is like the hard part for a lot of CRMs, FSMs today is like they're trying to be AI first, but they have this like, they have this huge behemoth of a platform that they're just trying to maintain every single day. That's like, that's hard and it's super expensive. And that's why I think you have folks that are kind of, kind of caught in the bear trap a little bit of like, we have to be AI first, we're a public company, but we have this like huge, we're like tied to this massive ball and chain that we're dragging along anytime we try and make any type of update. So I don't know, curious to hear your guys' thoughts, but yeah, that's our take.

Nic Poulos [00:49:57]:
I would say that if your defensibility as a product is UI, you have a problem, right? UI is fungible, it's cheap. There's no reason today why if you have an AI-native platform, every customer shouldn't theoretically be able to have their own custom UI that they can tweak at any time they want. You may proactively choose not to do that for other reasons, but you know, UI is no longer defensible, right? I think there's also— we're also seeing changes in UI because, you know, in this first wave of like kind of repricing software, if you will, a lot of what a lot of folks have, at least in public market equities, have put a premium on is like scalability, consumption-based pricing. Are you usable by other agents? Like, you know, say what you will about RingCentral's product, but like people are thinking, oh, agents will use it, therefore it's great. And that's, you know, or Twilio, right? And those are headless products. So I think that's why people have— why things have changed and people have maybe pushed away from them. And I think, look, that's great if you can provide all the value in the world. No one wants to go into an ERP and click checkboxes all day.

Nic Poulos [00:51:06]:
But I also do personally, I think that humans are very visual creatures. Like we evolved that way. A picture is worth a thousand words. And I'm sure you guys are experiencing this somewhat. Like, I'm incredibly reliant on like my agents that I built, but sometimes I'm like, oh man, like just flipping between 10 different agents in a terminal all day and using that as my only interface to do work is not ideal either.

Quinn Litherland [00:51:30]:
Yeah.

Nic Poulos [00:51:30]:
So UI is not defensible, but I do think that it's maybe will have a place in making work easier based on the context. And maximizing your exposure to the customer.

Luke Sophinos [00:51:42]:
Well, this is what's fun about being in vertical software too, is like, we're going to let that play out in the consumer market, right? And then we'll figure out, we'll figure out what's best and take from it because that's, that's what all those guys are chasing over there. You know, you had Instinct launch where it's like the iMessage-based agent, right? And so those, the consumer companies, and God bless them, I don't know how they do it. I couldn't sleep at night with the trends and the ups and downs of those businesses, but that's where a lot of that UI experimentation I think is going to happen and we can kind of borrow what works.

Nic Poulos [00:52:11]:
Why is AI UI still so bad? Like, I don't even know if I have a good answer for this because there's plenty of data out there.

Luke Sophinos [00:52:16]:
Paralyzes older users too because they just see the blank thing and they don't know, you know.

Nic Poulos [00:52:21]:
But I mean, I'm even talking about like design. Like, have you guys like tried to, I mean, create a deck? Like even with the best models, like it's, it's kind of dogshit, right? I mean, have you seen it?

Luke Sophinos [00:52:31]:
My deck, deck gen is solid. I used, uh, GenSpark and the PowerPoint output is incredible. It was the only one that I tried. I tried all of 'em. That was the only one with a credible, like, PowerPoint output.

Quinn Litherland [00:52:42]:
It is funny how it has like, like most, most AI-generated decks have that, like, that one specific look. Like you can tell immediately that it's AI-generated. And I think this is such a side topic, but I think there's such an immediate decrease in trust of whatever that piece of content is the second that you see it. You can just notice it immediately, whether it's the font or the spacing, the colors or the, or the text font or the text that's actually being used. And I think folks just like lose trust almost instantaneously when they see that. And I'm sure that'll change. And I'm sure also quality will improve over the next couple of months. Oh, I was gonna go back to this like headless, this headless comment real quick.

Quinn Litherland [00:53:18]:
The last thing I was gonna say is, and this like pairs back to my earlier comment of this like renaissance of especially home services, but more broadly vertically industries, I think that running these businesses is gonna get really, really fun because I think the tools are gonna be much more experience-based. And for an operator today, they have their CRM and FSM and a bunch of different point solutions. Some of them are pre-AI, some of them are post-AI. They have a bunch of humans, they have their marketing agency, they have their like ad agency. It's just like, it's such a mess. It's so hard. And I think we're going to get to a place very soon, whether it's Revvin that eventually becomes that, or there's this like other sector that kind of opens up of, yeah, this like experience, this like experience to run your business of like this, this partner in crime of like, I think operators are now going to be able to have everything tied in one place and they're going to be able to like have this interaction with an agent that knows their business just as well. well, if not better than they do.

Quinn Litherland [00:54:15]:
It's embedded into— now that more and more that I say this, this actually will, will be Revvin. Um, it's so embedded into all of your workflows. It just like understands everything that's going on and it's your partner in crime and you're able to go like, hey, like we need to hire more techs today. Um, we're going into busy season. Like let's go and do X, Y, and Z thing. And it goes and actions that and then it comes back and talks to you. And so I think, Nick, to your point, like yes, maybe it won't be the same like beautiful UI of the past, but again, I would push back of like, when have we ever had beautiful UI in vertical software. I don't think— I don't know many tools that have actually provided us with that.

Quinn Litherland [00:54:45]:
And so I think the inverse is actually gonna be like really, really, really cool experiences for operators where like if I'm running a $15 million HVAC business, I have this like kick-ass way to manage my company and it's fully autonomous. It's deeply embedded into every aspect of my business and I'm able to interact with it probably just like through my phone over SMS, email, and voice. And it's just like so embedded my partner in crime. And I think that's gonna be so cool for operators because they're just gonna be able to be so much more streamlined. Nothing's gonna fall through the cracks. Again, I think we're entering like the coolest decade for vertical software. And I think operators who have like been so historically forgotten are gonna start having some of like the coolest, most badass ways to grow their business. And you're gonna start seeing a $500 million roofing company run by 5 people and a bunch of Yeah, I think, I think it's, it's, it's such a, it's gonna be such a crazy time, especially in home services.

Quinn Litherland [00:55:38]:
But pause there.

Nic Poulos [00:55:39]:
Totally agree with that, man. I mean, if, uh, and if that's the case and they're like paying 2, 3, 4x ACV, like the aggregate opportunity for, for vertical software, vertical AI is so much larger than people are giving it credit for, which I know it's probably not controversial amongst us 3, but, uh, it's, it's exciting.

Luke Sophinos [00:55:59]:
So Quinn, one thing I was thinking about, you know, in your kind of view of the future where, which I agree with, by the way, but I'm just curious to get your steelman of it, which is you have an owner, he has kind of one agentic interface. He talks to it, that thing goes and executes across whether it's your app doing it or third-party apps, but the agents are basically going in and executing across those surface areas. What happens with the system of record fighting back? Like we saw Podium, right?

Quinn Litherland [00:56:23]:
Get shut off.

Nic Poulos [00:56:24]:
Yeah.

Luke Sophinos [00:56:24]:
That's the one, that's the one thing that I think can happen is even if you get there, at what point do those guys, you You know, say, hey, we're gonna come out with a competing solution and shut off access.

Nic Poulos [00:56:33]:
What's the steel man on it?

Quinn Litherland [00:56:35]:
Yeah. So, I think every— like, again, the amount of text messages I got about the Podium Service Titan thing over the last week, it was nuts. My phone just like blew up. Everyone's just like freaking out about it.

Luke Sophinos [00:56:45]:
Don't send those annoying text messages.

Quinn Litherland [00:56:47]:
Just saying. We're thinking about it.

Luke Sophinos [00:56:48]:
No, it was—

Quinn Litherland [00:56:50]:
to my investors listening, that's not what I was talking about. You can text me whatever you want. This was like everyone in the space. just asking my take on this. Again, everyone has to remember that Podium has been building a competitive field service management product for the last 18 months, and they didn't want to give up a percentage of their revenue to be a part of the marketplace. It's like, it's just at the end of the day, like Podium is becoming a direct competitor to ServiceTitan and going after the same customers. And so of course they're like, yeah, we don't want you in our marketplace. And if you're not gonna be comfortable with our terms of our marketplace, then like, yeah, we're gonna, gonna like break, we're gonna end this relationship.

Quinn Litherland [00:57:23]:
And so my, my perspective is, again, all, and this is like our take at Revvin, like all we care about right now is this action layer because the action layer to Nick's earlier point is so flipping huge because we're not only augmenting labor, but we're increasing cash flow into these businesses. We are helping them grow. And the more money we're driving for these businesses, the more they grow, the more the space grows. This is already a $657 billion market. soon to be a trillion-dollar market. So the more revenue coming into these businesses means that they can invest deeper into tools that are running their businesses like Revint. And so for me, like the biggest opportunity is on the system of action, which I don't even know how large that— like people ask me this all the time, like how big is this space? It's like, I don't know. Like I honestly don't know because it's growing so quickly.

Quinn Litherland [00:58:06]:
There's so like hundreds of billions of dollars is being spent on labor today that we're going after. But as we help our customers grow and like A lot of our customers are having like the best year ever because we've been crushing it so hard for them in terms of driving new revenue, helping them close opportunities that they would've otherwise lost. It's like, yeah, we don't know how like big this action layer could actually get. And then in terms of like the system of record layer, I mean, we just wanna be good partners and we just wanna make sure that we're like continuously supporting those ecosystems, piping data back into them. Like there's a lot of value there. And of course, like there will be certain workflows that like we might butt heads on, That's expected. But I think if anyone, including us, turns around and is like, hey, we are now a field service management tool, which like, I don't want it to go and do. I don't want to go and manage all that UI.

Quinn Litherland [00:58:48]:
Like, I just have no interest to do that. As long as you don't go and like, not even poke the bear, like try and stab the bear, like you're probably going to be fine.

Nic Poulos [00:58:56]:
I get it.

Luke Sophinos [00:58:56]:
I think it makes sense.

Nic Poulos [00:58:58]:
Last question. All right, Quinn, you're building an AI-native company and you can have 3 hires total. What are those roles?

Quinn Litherland [00:59:07]:
Oh man, 3 hires. Sales, FTE engineering. Again, that, that at high level is not, no, no hot takes there, but I'll go a layer deeper of it comes down to, can you have the best seller possible who understands the semantics of the industry you're, you're, you're building in? And again, for most vertical spaces, that means they know every single conference they go to. They know every single think group. They know every single Facebook and Reddit thread to be a part of. They know all the podcasts that you need to go and sponsor. They know all the kind of like paid influencers in your space that everyone is talking to and listens to. It's like somebody who so deeply understands the nuances of your industry that is able to like on day one, just like build trust, unlock all that distribution, and then is also able to go and like support from a partnerships perspective on building distribution channels.

Quinn Litherland [00:59:54]:
So it's What are the systems that you need to go and integrate with? What are the other tools that your customers are buying that you wanna go partner with? And you're just constantly sending each other customers. So again, that like full service, it was like that very, very deeply embedded go-to-market expert who most likely comes from the industry. I think they can do so much damage. I think teams can, with the right hire, can go like 1 to 10 really, really quickly with the right person building the right distribution channels and who already has like a massive Rolodex of the space. So that's one. 2 is from that FTE perspective or AI deployment strategist, whatever you wanna call them.

Nic Poulos [01:00:27]:
Yeah.

Quinn Litherland [01:00:27]:
Somebody who understands your product, understands your vertical, and is able to go on site, build trust with your customers, and just deploy really, really good agents that you can then maintain and then expand. And I think there is both like an art and science to it, especially on the relationship side. And so somebody who is like Paul, Who is so incredible at their job and so deeply understands and has so much empathy and trust and love for the space. Like, that's just so important. Like, you mess that up, you are in a really, really tough spot. And then an engineering leader. Like, I don't think— I know everyone's always talking about this is the end of engineering, etc. Like, I fundamentally disagree with that.

Quinn Litherland [01:01:05]:
I think there is such an art to it and you need somebody who has good taste and can scale systems and can do that in a way that is aligned with this like really complex and convoluted world that we live in where things are changing so quickly and is able to just like put the blinders on and just feel like none of this BS, like this is what we're doing. This is how we're gonna scale over the next 10 years, which is a lot harder to do than I think a lot of people think. And so, yeah, I think that engineering leader who definitely doesn't have to come from the space at all, I think it more comes from, can they, have they had experience scaling similar products in past? Do they understand like the nooks and crannies that you're gonna fall into? And can they hire exceptional other engineering talent? And especially right now in this hiring market where it's just, it's so crazy, especially if you're in a hub like New York or San Francisco. Yeah, I would say those are the 3 that I care most about. And if anyone was starting a company, like those are the 3 that I would heavily lean into. And I think if you get any of them wrong, like it's not the end of the world, but it's definitely gonna be a harder journey if you don't have them.

Nic Poulos [01:02:02]:
Love it, man. That's, I think a perfect note to wrap on, but dude, great catching up. I think we covered a lot today on a Sunday here. So thanks for joining us, man.

Quinn Litherland [01:02:12]:
Yeah, of course. Thanks for having me, guys.

Luke Sophinos [01:02:13]:
That was fun.

Nic Poulos [01:02:14]:
Of course.