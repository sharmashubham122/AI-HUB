import os

categories = {
    "cat-text": {
        "title": "✍️ Text & Writing",
        "subtitle": "AI-powered writing assistants, editors, and content generators",
        "tools": [
            ("✍️","AI Writer Pro","Free","Generate high-quality blog posts, articles, and social media content with a single click.","https://ADD-LINK-HERE"),
            ("📝","Jasper AI","Paid","Advanced AI copywriting tool for marketers and content creators.","https://ADD-LINK-HERE"),
            ("📖","Writesonic","Freemium","Create SEO-optimized articles, product descriptions, and ad copy effortlessly.","https://ADD-LINK-HERE"),
            ("🖊️","Copy.ai","Freemium","AI-powered copy generator for emails, landing pages, and marketing materials.","https://ADD-LINK-HERE"),
            ("📄","Grammarly","Freemium","AI grammar checker and writing assistant trusted by millions.","https://ADD-LINK-HERE"),
            ("🔤","QuillBot","Freemium","Smart paraphrasing and summarization tool for better writing.","https://ADD-LINK-HERE"),
            ("📜","Hemingway Editor","Free","Highlights complex sentences and readability issues in your writing.","https://ADD-LINK-HERE"),
            ("✒️","Rytr","Freemium","AI writing assistant that helps you create content in 30+ languages.","https://ADD-LINK-HERE"),
            ("💡","Wordtune","Freemium","Rewrite and rephrase sentences to sound more professional and clear.","https://ADD-LINK-HERE"),
            ("🗒️","Notion AI","Paid","AI assistant built inside Notion for summarizing, editing, and drafting.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-image": {
        "title": "🎨 Image Generation",
        "subtitle": "Create stunning visuals, illustrations, and photos using AI",
        "tools": [
            ("🎨","Midjourney","Paid","Industry-leading AI art generator producing breathtaking, painterly images.","https://ADD-LINK-HERE"),
            ("🖼️","DALL·E 3","Freemium","OpenAI's image generator creating detailed visuals from text descriptions.","https://ADD-LINK-HERE"),
            ("🌟","Stable Diffusion","Free","Open-source AI image generator you can run locally or in the cloud.","https://ADD-LINK-HERE"),
            ("🖌️","Adobe Firefly","Freemium","Adobe's creative AI for generating images, effects, and text styles.","https://ADD-LINK-HERE"),
            ("✨","Canva AI","Freemium","AI-powered design tool with magic image generation and editing.","https://ADD-LINK-HERE"),
            ("🎭","Leonardo AI","Freemium","Create game assets, concept art, and illustrations at scale.","https://ADD-LINK-HERE"),
            ("🌈","Ideogram","Freemium","AI image generator with excellent text rendering capabilities.","https://ADD-LINK-HERE"),
            ("🖍️","Playground AI","Freemium","User-friendly AI art platform with multiple model support.","https://ADD-LINK-HERE"),
            ("📸","Photoroom","Freemium","Remove backgrounds and create product photos using AI automatically.","https://ADD-LINK-HERE"),
            ("🔮","NightCafe","Freemium","Community-focused AI art generator with daily free credits.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-video": {
        "title": "🎬 Video Creation",
        "subtitle": "Generate, edit, and enhance videos using the power of AI",
        "tools": [
            ("🎬","Sora","Paid","OpenAI's revolutionary text-to-video model creating cinematic clips.","https://ADD-LINK-HERE"),
            ("🎥","Runway ML","Freemium","Professional AI video editor with generative video and inpainting.","https://ADD-LINK-HERE"),
            ("🎞️","Pika Labs","Freemium","Generate short creative videos from text or images in seconds.","https://ADD-LINK-HERE"),
            ("📹","HeyGen","Freemium","Create AI avatar videos with realistic lip-sync and voices.","https://ADD-LINK-HERE"),
            ("🎦","Synthesia","Paid","Create professional training and explainer videos with AI avatars.","https://ADD-LINK-HERE"),
            ("🎙️","Descript","Freemium","Edit video by editing text — remove filler words with one click.","https://ADD-LINK-HERE"),
            ("🎭","Kling AI","Freemium","High-quality AI video generation with motion physics.","https://ADD-LINK-HERE"),
            ("📽️","Invideo AI","Freemium","Turn scripts into fully produced videos with stock footage and voiceover.","https://ADD-LINK-HERE"),
            ("🎪","Luma AI","Freemium","Create 3D content and AI-generated videos from real-world captures.","https://ADD-LINK-HERE"),
            ("🎯","Pictory AI","Paid","Transform long-form content into short shareable video clips.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-audio": {
        "title": "🎵 Audio & Music",
        "subtitle": "AI tools for music generation, voice cloning, and audio editing",
        "tools": [
            ("🎵","Suno AI","Freemium","Generate complete songs with vocals and instruments from a text prompt.","https://ADD-LINK-HERE"),
            ("🎶","Udio","Freemium","Create high-fidelity music tracks across any genre using AI.","https://ADD-LINK-HERE"),
            ("🎤","ElevenLabs","Freemium","Ultra-realistic AI voice generation and voice cloning platform.","https://ADD-LINK-HERE"),
            ("🔊","Murf AI","Freemium","Studio-quality AI voiceovers for videos, podcasts, and presentations.","https://ADD-LINK-HERE"),
            ("🎸","Soundraw","Paid","Generate royalty-free AI music for your videos and content.","https://ADD-LINK-HERE"),
            ("🎹","AIVA","Freemium","Compose emotional soundtracks and background music with AI.","https://ADD-LINK-HERE"),
            ("🎺","Boomy","Freemium","Create original songs in seconds and release them on streaming platforms.","https://ADD-LINK-HERE"),
            ("🎼","Loudly","Freemium","AI music platform for creators with 170,000+ AI-generated stems.","https://ADD-LINK-HERE"),
            ("🔉","Adobe Podcast","Freemium","Enhance and clean up audio recordings with AI in one click.","https://ADD-LINK-HERE"),
            ("🎙️","Whisper","Free","OpenAI's open-source speech-to-text model with high accuracy.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-code": {
        "title": "💻 Coding & Dev",
        "subtitle": "AI-powered coding assistants, debuggers, and developer tools",
        "tools": [
            ("💻","GitHub Copilot","Paid","AI pair programmer that auto-completes code in any language inside your IDE.","https://ADD-LINK-HERE"),
            ("🤖","Cursor","Freemium","AI-first code editor with chat, edit, and generation built in.","https://ADD-LINK-HERE"),
            ("⚡","Claude Code","Paid","Agentic coding tool by Anthropic for complex coding tasks in the terminal.","https://ADD-LINK-HERE"),
            ("🔧","Tabnine","Freemium","AI code completion that learns your codebase and style.","https://ADD-LINK-HERE"),
            ("🛠️","Codeium","Free","Free AI code autocomplete and chat supporting 70+ languages.","https://ADD-LINK-HERE"),
            ("🚀","Replit AI","Freemium","Build and deploy apps in the browser with AI-assisted coding.","https://ADD-LINK-HERE"),
            ("🐛","Devin","Paid","The world's first fully autonomous AI software engineer.","https://ADD-LINK-HERE"),
            ("📦","v0 by Vercel","Freemium","Generate React UI components from text descriptions instantly.","https://ADD-LINK-HERE"),
            ("🔍","Sourcegraph Cody","Freemium","AI coding assistant with deep codebase context and search.","https://ADD-LINK-HERE"),
            ("🌐","bolt.new","Freemium","Build and deploy full-stack web apps from a single prompt.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-chat": {
        "title": "💬 Chatbots & LLMs",
        "subtitle": "Conversational AI models and large language models",
        "tools": [
            ("💬","ChatGPT","Freemium","OpenAI's flagship conversational AI used by 100M+ people worldwide.","https://ADD-LINK-HERE"),
            ("🤖","Claude","Freemium","Anthropic's helpful, harmless, and honest AI assistant.","https://ADD-LINK-HERE"),
            ("🔷","Gemini","Freemium","Google's multimodal AI model for text, images, and reasoning.","https://ADD-LINK-HERE"),
            ("🦙","Meta Llama","Free","Meta's open-source LLM available for research and commercial use.","https://ADD-LINK-HERE"),
            ("🌙","Mistral AI","Freemium","High-performance open-weight language models from Europe.","https://ADD-LINK-HERE"),
            ("🔎","Perplexity AI","Freemium","AI-powered search engine that gives cited, real-time answers.","https://ADD-LINK-HERE"),
            ("💡","You.com","Freemium","AI search assistant combining web results with AI generation.","https://ADD-LINK-HERE"),
            ("🐬","Dolphin","Free","Uncensored open-source conversational AI model by Eric Hartford.","https://ADD-LINK-HERE"),
            ("🌊","Cohere","Freemium","Enterprise-grade LLM API for building custom AI applications.","https://ADD-LINK-HERE"),
            ("⚗️","Grok","Freemium","xAI's witty, real-time AI assistant with web access and humor.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-research": {
        "title": "🔬 Research & Data",
        "subtitle": "AI tools for data analysis, research, and knowledge discovery",
        "tools": [
            ("🔬","Elicit","Freemium","AI research assistant that finds and summarizes academic papers.","https://ADD-LINK-HERE"),
            ("📊","Julius AI","Freemium","Chat with your data — upload CSV/Excel and get instant insights.","https://ADD-LINK-HERE"),
            ("🗺️","Consensus","Freemium","AI-powered scientific search engine with evidence-backed answers.","https://ADD-LINK-HERE"),
            ("📚","Semantic Scholar","Free","AI-powered academic search engine for scientific literature.","https://ADD-LINK-HERE"),
            ("🧪","Research Rabbit","Free","Discover related papers and visualize research networks.","https://ADD-LINK-HERE"),
            ("📈","Tableau AI","Paid","Augmented analytics and AI-driven data visualization in Tableau.","https://ADD-LINK-HERE"),
            ("🤔","Wolfram Alpha","Freemium","Computational intelligence engine for math, science, and data.","https://ADD-LINK-HERE"),
            ("🧬","AlphaFold","Free","DeepMind's AI predicting protein structures with atomic accuracy.","https://ADD-LINK-HERE"),
            ("📰","Scite AI","Paid","Smart citations that show how papers have been cited in context.","https://ADD-LINK-HERE"),
            ("🔭","Iris AI","Freemium","AI workspace for finding, reading, and organizing research papers.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-design": {
        "title": "🖌️ Design & UI",
        "subtitle": "AI-powered tools for UI/UX design, prototyping, and visual creation",
        "tools": [
            ("🖌️","Figma AI","Freemium","AI features inside Figma for generating UI, layers, and auto-layouts.","https://ADD-LINK-HERE"),
            ("🎨","Uizard","Freemium","Transform sketches and wireframes into polished app mockups with AI.","https://ADD-LINK-HERE"),
            ("✏️","Galileo AI","Paid","Generate high-fidelity UI designs from text descriptions instantly.","https://ADD-LINK-HERE"),
            ("🌟","Framer AI","Freemium","AI website builder that generates full pages from a text prompt.","https://ADD-LINK-HERE"),
            ("🎭","Looka","Paid","AI logo maker and brand identity generator for businesses.","https://ADD-LINK-HERE"),
            ("🖼️","Khroma","Free","AI color tool that learns your palette preferences and suggests combos.","https://ADD-LINK-HERE"),
            ("📐","Visily","Freemium","AI-powered UI design tool for non-designers and developers.","https://ADD-LINK-HERE"),
            ("🎪","Picsart AI","Freemium","AI editing tools for photos, graphics, and social media content.","https://ADD-LINK-HERE"),
            ("🎡","Zyng AI","Freemium","Generate product photography backgrounds and mockups with AI.","https://ADD-LINK-HERE"),
            ("✨","Relume","Freemium","AI website design system generating sitemaps and wireframes.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-business": {
        "title": "📊 Business & Marketing",
        "subtitle": "AI tools to grow your business, automate marketing, and boost sales",
        "tools": [
            ("📊","HubSpot AI","Freemium","AI tools inside HubSpot for content, email, and CRM automation.","https://ADD-LINK-HERE"),
            ("📣","AdCreative.ai","Paid","Generate high-converting ad creatives and copy with AI.","https://ADD-LINK-HERE"),
            ("📧","Instantly AI","Paid","AI-powered cold email outreach platform for lead generation.","https://ADD-LINK-HERE"),
            ("🔑","Surfer SEO","Paid","AI content editor that helps you rank higher on Google.","https://ADD-LINK-HERE"),
            ("💼","Tome","Freemium","AI-powered storytelling and presentation tool for business pitches.","https://ADD-LINK-HERE"),
            ("📱","Buffer AI","Freemium","AI social media manager that schedules and creates content.","https://ADD-LINK-HERE"),
            ("🤝","Gong","Paid","AI revenue intelligence platform analyzing sales calls and deals.","https://ADD-LINK-HERE"),
            ("🏪","Shopify Magic","Freemium","AI features for Shopify merchants — product descriptions, campaigns.","https://ADD-LINK-HERE"),
            ("📉","Domo AI","Paid","AI-powered business intelligence and data visualization platform.","https://ADD-LINK-HERE"),
            ("💰","Drift AI","Paid","Conversational AI chatbot for B2B sales pipeline acceleration.","https://ADD-LINK-HERE"),
        ]
    },
    "cat-productivity": {
        "title": "⚡ Productivity",
        "subtitle": "Automate workflows, manage tasks, and get more done with AI",
        "tools": [
            ("⚡","Zapier AI","Freemium","Automate workflows between 6,000+ apps with AI-powered Zaps.","https://ADD-LINK-HERE"),
            ("📋","Notion AI","Paid","AI assistant inside Notion for writing, summarizing, and tasking.","https://ADD-LINK-HERE"),
            ("🗂️","Motion","Paid","AI calendar that auto-schedules your tasks and meetings.","https://ADD-LINK-HERE"),
            ("📅","Reclaim AI","Freemium","AI scheduling assistant that protects time for deep work.","https://ADD-LINK-HERE"),
            ("🧠","Mem AI","Paid","AI-powered notes app that organizes your knowledge automatically.","https://ADD-LINK-HERE"),
            ("📝","Otter AI","Freemium","AI meeting transcription and note-taker for Zoom and Google Meet.","https://ADD-LINK-HERE"),
            ("🔄","Make (Integromat)","Freemium","Visual automation platform with AI modules for complex workflows.","https://ADD-LINK-HERE"),
            ("📌","Taskade AI","Freemium","AI productivity suite for project management and team collaboration.","https://ADD-LINK-HERE"),
            ("🗓️","Clara","Paid","AI executive assistant that schedules meetings via natural email.","https://ADD-LINK-HERE"),
            ("🚀","Superhuman AI","Paid","AI email client that helps you reach inbox zero twice as fast.","https://ADD-LINK-HERE"),
        ]
    },
}

TOOL_CARD = '''      <div class="tool-card">
        <div class="tool-img">{emoji}</div>
        <div class="tool-body">
        <div class="tool-name">
            {name}
            <span class="tool-badge">{badge}</span>
        </div>
        <div class="tool-desc">{desc}</div>
        </div>
        <div class="tool-footer">
        <!-- ===== ADD YOUR TOOL LINK BELOW (replace # with the actual URL) ===== -->
        <a class="tool-visit-btn" href="{link}" target="_blank" rel="noopener">Visit Tool →</a>
        <a class="tool-info-btn" href="{link}" target="_blank" rel="noopener">Info</a>
        </div>
        </div>'''

PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title} – AI HUB</title>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<script src="navbar.js"></script>

<div class="page-header">
    <a class="back-btn" href="index.html">← Back to Home</a>
    <div class="page-header-text">
    <h1>{title}</h1>
    <p>{subtitle}</p>
    </div>
</div>

<div class="tools-grid">
{cards}
</div>

<footer>
    <div class="footer-inner">
    <div class="footer-logo">⚡ AI HUB</div>
    <p>Your ultimate AI tools directory. &copy; 2025 AI HUB. All rights reserved.</p>
    </div>
</footer>
</body>
</html>'''

for filename, data in categories.items():
    cards = "\n".join(
        TOOL_CARD.format(emoji=t[0], name=t[1], badge=t[2], desc=t[3], link=t[4])
        for t in data["tools"]
    )
    html = PAGE_TEMPLATE.format(
        title=data["title"],
        subtitle=data["subtitle"],
        cards=cards
    )
    with open(f"/home/claude/aihub/{filename}.html", "w") as f:
        f.write(html)
    print(f"Created {filename}.html")

print("All category pages done!")
