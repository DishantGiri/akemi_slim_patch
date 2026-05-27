import os
import re

SEO_BASE = """
    <meta name="keywords" content="Akemi Slim Patch, weight loss patch, slim patch, wellness patch, weight management support">
    <meta name="author" content="Akemi Slim Patch Official">
    <link rel="icon" type="image/png" href="/favicon.png">
    
    <!-- Open Graph / Social -->
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://www.akemislimpatchofficial.com/images/akemi_slim_patch_box.webp">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:image" content="https://www.akemislimpatchofficial.com/images/akemi_slim_patch_box.webp">
"""

INDEX_SCHEMA = """
    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Product",
          "name": "Akemi Slim Patch",
          "description": "Akemi Slim Patch is a transdermal wellness patch designed to support daily weight management, craving control, and routine consistency.",
          "image": "https://www.akemislimpatchofficial.com/images/akemi_slim_patch_box.webp",
          "sku": "AKEMI-SLIM-001",
          "brand": {
            "@type": "Brand",
            "name": "Akemi"
          },
          "offers": {
            "@type": "Offer",
            "url": "https://www.akemislimpatchofficial.com/#pricing",
            "priceCurrency": "USD",
            "price": "19.99",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          },
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "reviewCount": "842"
          },
          "review": [
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Emily Carter" },
              "datePublished": "2025-10-15",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "I honestly bought the Akemi Slim Patch because I was tired of carrying around bottles of supplements everywhere. I travel a lot for work and wanted something simple. After a few weeks, I noticed I wasn’t constantly snacking late at night anymore. The biggest thing for me wasn’t crazy weight loss - it was finally feeling more in control of my routine again."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Daniel Brooks" },
              "datePublished": "2025-11-02",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "I saw a bunch of reviews on Akemi Slim Patch online and figured I’d give it a shot since I hate swallowing pills. The patch was surprisingly comfortable, and I liked how low-maintenance it felt. My wife actually noticed I’d stopped digging through the kitchen at midnight. Small change, but honestly that’s been huge for me over the last month."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Sophie Lambert" },
              "datePublished": "2026-01-20",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "What convinced me was how easy the Akemi patch sounded compared to all the strict programs I’d tried before. I work long hospital shifts, so convenience matters. I followed the Akemi Slim Patch instructions carefully and wore it daily for several weeks. I felt less bloated and more consistent with my eating habits. It just fit naturally into my life without feeling stressful."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Michael Turner" },
              "datePublished": "2026-02-14",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "I was mostly curious about the Akemi Slim Patch ingredients because a lot of weight products feel overloaded with stimulants. This felt gentler than the energy pills I used years ago. I started using it while walking every morning with my dog, and over time my clothes started fitting better. Nothing dramatic overnight, but steady progress that actually felt realistic."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Olivia Bennett" },
              "datePublished": "2026-03-05",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "I almost didn’t order because I kept comparing the Akemi Slim Patch price with other products online. In the end I went for the bundle deal, mainly because the daily patch format sounded easier for me to stick with. A month later, I’d say the biggest difference is consistency. I’m finally not bouncing between random diets every other week."
            },
            {
              "@type": "Review",
              "author": { "@type": "Person", "name": "Luca Meyer" },
              "datePublished": "2026-04-12",
              "reviewRating": { "@type": "Rating", "ratingValue": "5" },
              "reviewBody": "Most akemi weight loss patch reviews sounded way too exaggerated, so I kept my expectations pretty normal. I used the patches while trying to clean up my eating a bit and get back to cycling again. The funny thing is the patch became a daily reminder to stay disciplined. That mental side of it helped me more than I expected."
            }
          ]
        },
        {
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "What is Akemi Slim Patch?", "acceptedAnswer": { "@type": "Answer", "text": "Akemi Slim Patch is a transdermal wellness patch designed to support daily weight management, craving control, and routine consistency. It is applied to the skin and used as part of a healthy lifestyle." } },
            { "@type": "Question", "name": "How much does Akemi Slim Patch cost?", "acceptedAnswer": { "@type": "Answer", "text": "Akemi Slim Patch price depends on the bundle selected. Larger bundles usually lower the cost per pack and may include stronger discounts than a single-pack order." } },
            { "@type": "Question", "name": "Does Akemi Slim Patch Really Work?", "acceptedAnswer": { "@type": "Answer", "text": "Akemi Slim Patch is designed to support weight-management habits through a wearable patch format focused on convenience, appetite awareness, and routine consistency. Some users prefer patches because they fit more easily into daily life than pills or powders. However, results vary significantly between individuals, and the product should not be viewed as a guaranteed fat-loss solution or replacement for healthy lifestyle habits." } },
            { "@type": "Question", "name": "What are the Akemi Slim Patch ingredients?", "acceptedAnswer": { "@type": "Answer", "text": "Product materials describe Akemi as a transdermal patch with wellness-support positioning. Buyers should check the official label and packaging for the most accurate Akemi Slim Patch ingredients list before use." } },
            { "@type": "Question", "name": "Is Akemi Slim Patch safe?", "acceptedAnswer": { "@type": "Answer", "text": "Akemi Slim Patch is for adults only. Anyone with health conditions, allergies, pregnancy, breastfeeding, or medication use should consult a healthcare provider before using it." } },
            { "@type": "Question", "name": "Where should I place Akemi Slim Patch?", "acceptedAnswer": { "@type": "Answer", "text": "Apply Akemi Slim Patch to clean, dry skin as directed on the product instructions. Avoid irritated skin, cuts, lotion-heavy areas, or places where clothing may rub too much." } },
            { "@type": "Question", "name": "Are there Akemi Slim Patch before and after results?", "acceptedAnswer": { "@type": "Answer", "text": "Some users may share slim patch before and after experiences, but results vary. Photos and testimonials should be viewed as individual experiences, not guaranteed outcomes." } },
            { "@type": "Question", "name": "Do Weight Loss Patches Actually Work?", "acceptedAnswer": { "@type": "Answer", "text": "Weight loss patches are designed to support wellness routines through a wearable transdermal format, but scientific evidence for slimming patches as a category remains limited. Some users prefer patches because they are easy to use and may help support routine consistency, appetite awareness, or healthier habits. However, no patch should be viewed as a guaranteed fat-loss solution or replacement for balanced nutrition, movement, and healthy lifestyle choices." } },
            { "@type": "Question", "name": "Is Akemi Slim Patch Legit?", "acceptedAnswer": { "@type": "Answer", "text": "Akemi Slim Patch is marketed as a wellness-support product designed to help users maintain a simpler daily weight-management routine. Buyers should use realistic expectations, review the ingredient label carefully, and purchase only from the official source to avoid misleading third-party sellers or counterfeit listings." } },
            { "@type": "Question", "name": "How Does a Slim Patch Work?", "acceptedAnswer": { "@type": "Answer", "text": "Slim patches are designed to be applied directly to the skin using a transdermal-style format. The idea behind these patches is gradual ingredient delivery while supporting routine consistency, appetite awareness, or wellness habits. However, results vary significantly between individuals, and healthy lifestyle habits still play the biggest role in long-term weight management." } },
            { "@type": "Question", "name": "Are Slim Patches Effective?", "acceptedAnswer": { "@type": "Answer", "text": "Some users find slim patches easier to stay consistent with compared to pills or powders because they are simple and wearable. However, effectiveness varies depending on lifestyle habits, nutrition, activity level, sleep, and overall consistency. Slim patches should be viewed as supportive wellness tools rather than guaranteed weight-loss treatments." } },
            { "@type": "Question", "name": "What Are the Side Effects of Slim Patches?", "acceptedAnswer": { "@type": "Answer", "text": "Some users may experience mild skin irritation, redness, itching, or adhesive sensitivity when using slimming patches. Reactions vary depending on skin type and product ingredients. Users should avoid applying patches to broken or irritated skin and should discontinue use if discomfort continues. Anyone with medical conditions or medication use should consult a healthcare professional before use." } },
            { "@type": "Question", "name": "Where Can I Buy Akemi Slim Patch?", "acceptedAnswer": { "@type": "Answer", "text": "Akemi Slim Patch should be purchased through the official order source or authorized checkout page to help ensure product authenticity, customer support access, secure payment processing, and eligibility for the money-back guarantee." } },
            { "@type": "Question", "name": "Where Can I Buy Slim Patches in Canada?", "acceptedAnswer": { "@type": "Answer", "text": "Availability for slim patches in Canada depends on the seller and shipping policies. Buyers should review the official checkout page to confirm Canadian shipping availability, delivery timelines, customer support access, and refund eligibility before ordering." } }
          ]
        }
      ]
    }
    </script>
"""

OTHER_SCHEMA = """
    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "{title}",
      "url": "{url}"
    }}
    </script>
"""

def update_html_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"\s*>', content)
    
    title = title_match.group(1) if title_match else "Akemi Slim Patch"
    desc = desc_match.group(1) if desc_match else "Akemi Slim Patch is a transdermal wellness patch designed to support daily weight management."
    
    page_name = "" if filename == "index.html" else filename
    url = f"https://www.akemislimpatchofficial.com/{page_name}"
    
    seo_injection = f"""
    <link rel="canonical" href="{url}">
    {SEO_BASE}
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="twitter:url" content="{url}">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{desc}">
"""

    if filename == "index.html":
        seo_injection += INDEX_SCHEMA
    else:
        seo_injection += OTHER_SCHEMA.format(title=title, url=url)

    content = content.replace('{seo_injection}', seo_injection)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for file in os.listdir('.'):
    if file.endswith('.html'):
        update_html_file(file)
