export default {
  hello: "Hello",
  login: "Login",
  logout: "Logout",
  register: "Register",
  confirmLogout: "Are you sure you want to logout?",

  Login: {
    welcome: "Welcome",
    subtitle: "Login to experience our services",
    emailLabel: "Email",
    emailPlaceholder: "Enter email",
    passwordLabel: "Password",
    passwordPlaceholder: "Enter password",
    forgotPassword: "Forgot password?",
    loginButton: "Login",
    orContinueWith: "Or continue with",
    noAccount: "Don't have an account?",
    registerLink: "Sign up now",
    adminLoginLink: "Login with admin account",
    validation: {
      emailRequired: "Please enter email",
      emailInvalid: "Invalid email",
      passwordRequired: "Please enter password",
      passwordMinLength: "Password must be at least 6 characters",
    },
    messages: {
      success: "Login successful!",
      googleSuccess: "Google login successful!",
      facebookSuccess: "Facebook login successful!",
      oauthSuccess: "{provider} login successful!",
      error: "An error occurred during login",
      invalidCredentials: "Invalid email or password!",
    }
  },

  Register: {
    title: "Sign Up",
    subtitle: "Create a new account to get started",
    fullNameLabel: "Full Name",
    fullNamePlaceholder: "Enter full name",
    emailLabel: "Email",
    emailPlaceholder: "Enter email",
    passwordLabel: "Password",
    passwordPlaceholder: "Enter password",
    phoneLabel: "Phone Number",
    phonePlaceholder: "Enter phone number (e.g., 0912345678)",
    registerButton: "Sign Up",
    hasAccount: "Already have an account?",
    loginLink: "Login now",
    validation: {
      fullNameRequired: "Please enter full name",
      fullNameMin: "Full name must be at least 2 characters",
      fullNameMax: "Full name cannot exceed 64 characters",
      emailRequired: "Please enter email",
      emailInvalid: "Invalid email",
      emailMin: "Email must be between 6 and 64 characters",
      emailMax: "Email must be between 6 and 64 characters",
      passwordRequired: "Please enter password",
      passwordMin: "Password must be at least 6 characters",
      passwordMax: "Password cannot exceed 64 characters",
      phoneRequired: "Please enter phone number",
      phoneInvalid: "Invalid phone number (e.g., 0912345678 or +84912345678)",
    },
    messages: {
      success: "Verification code has been sent to your email!",
      error: "Registration failed!",
    }
  },

  AdminLogin: {
    title: "Admin Portal",
    subtitle: "Shoez Management System",
    emailLabel: "Email or Username",
    emailPlaceholder: "admin@shoez.com",
    passwordLabel: "Password",
    loginButton: "Login",
    processing: "Processing...",
    or: "or",
    customerLoginLink: "Login with customer account",
    securityNotice: "This is the system administration area. Only for authorized managers. All actions are recorded.",
    copyright: "© 2025 Shoez Shop. All rights reserved.",
    messages: {
      fillAllFields: "Please fill in all required fields",
      noPermission: "You do not have permission to access the administration area",
      success: "Login successful! Redirecting...",
      invalidCredentials: "Invalid email or password",
    }
  },

  Navigation: {
    home: "Home",
    products: "Products",
    about: "About",
    news: "News",
    contact: "Contact",
  },
  HEROSECTION: {
    badge: "UP TO 50% OFF",
    title1: "SHOEZ",
    title2: "SHOP",
    subtitle: "PREMIUM AUTHENTIC SNEAKERS",
    ctaExplore: "EXPLORE NOW",
    ctaViewProducts: "VIEW PRODUCTS →",
    statsProducts: "PRODUCTS",
    statsCustomers: "CUSTOMERS",
    statsSatisfaction: "SATISFACTION",
    bgAlt: "Premium sneakers background",
  },

  Home: {
    FeaturedProducts: {
      title: "Featured Products",
      subtitle: "Most loved sneakers",
      loading: "Loading products...",
      error: "Error loading products:",
      retry: "Retry",
      menShoes: "Men's Shoes",
      womenShoes: "Women's Shoes",
      sale: "🔥 Sale",
      topRated: "⭐ Top Rated",
      viewAll: "View All",
      empty: "No products to display.",
      errorLoad: "Error loading product data",
    },
    BrandSection: {
      title: "Brands",
      empty: "No brands available",
      officialPartner: "Official Partner",
      authentic: "100% Authentic",
      globalWarranty: "Global Warranty",
    },
    NewsSection: {
      title: "SHOEZ.VN NEWS",
      hashtag: "#BLOG",
      brandName: "Myshoes.vn",
      articles: {
        "1": {
          title: 'WHICH RUNNING SHOES ARE THE "CROWN" OF RUNNERS IN 2025?',
          excerpt: 'Introduction: The Pinnacle of Running Shoe Technology 2025…',
        },
        "2": {
          title: 'Don\'t Ask Why I Only Wear Authentic Shoes – The Answer Lies in the Feeling When Putting Them On',
          excerpt: 'I used to be a "sale hunter" for fake shoes…',
        },
        "3": {
          title: '5 Comfortable and Convenient Sneaker Recommendations for Late 2025',
          excerpt: 'End of year is always the ideal time to shop…',
        },
        "4": {
          title: 'Cold Wind is Coming, Do You Have Warm Shoes Yet?',
          excerpt: 'Introduction When the first cold winds of the season begin to creep in…',
        },
        "5": {
          title: 'Top Sneaker Models Worth Buying for Fall 2025',
          excerpt: 'Latest collection with many colors and comfortable technology…',
        },
        "6": {
          title: 'How to Choose Shoe Size Online: Tips from Experts',
          excerpt: 'Guide to accurate measurement, avoid troublesome returns.',
        },
      },
    },
    NewsDetail: {
      back: "Go Back",
      tableOfContents: "Table of Contents",
      relatedImages: "Related Images",
      image: "Image",
      imageIndex: "Image {index}",
      imageForSection: "Image for {section}",
      share: "Share:",
      comments: "Comments",
      enterComment: "Enter your comment...",
      submitComment: "Submit Comment",
      guest: "Guest",
      noComments: "No comments yet.",
      relatedArticles: "Related Articles",
      articleNotFound: "Article does not exist.",
      linkCopied: "Article link copied!",
      author: "Author: Myshoes Team",
      views: "views",
      articleContent: {
        "1": `I. Introduction: The Pinnacle of Running Shoe Technology 2025

2025 marks a major turning point in the running shoe industry. Not just small improvements, we are witnessing a true revolution in technology and materials. Major brands have invested millions of dollars in research and development, bringing products that not only improve performance but also protect runners' health.

The 2025 running shoe market sees fierce competition among giants like {{BRAND_NIKE}}, {{BRAND_ADIDAS}}, {{BRAND_NEW_BALANCE}}, and {{BRAND_ASICS}}. Each brand brings exclusive technologies, from ultra-light cushioning systems to integrated smart sensors. Consumers now seek not just comfortable shoes, but a "powerful assistant" that can accompany them on every journey.

II. Breakthrough New Technologies

{{TECH_CARBON_FIBER_PLATE}} - Carbon plates are no longer exclusive to {{TECH_RACING_SHOES}}: 2025 sees the popularity of carbon plates in {{TECH_TRAINING_SHOES}} as well. This technology increases forward propulsion efficiency by up to 4%, while minimizing muscle injuries.

Foam Revolution - The revolution in cushioning materials: Brands have developed new foam types with superior elasticity. {{BRAND_NIKE}} with {{TECH_ZOOM_X}}, {{BRAND_ADIDAS}} with {{TECH_LIGHTSTRIKE_PRO}}, and {{BRAND_NEW_BALANCE}} with {{TECH_FUELCELL}} all show significant improvements in durability and responsiveness.

Sustainable Materials - Sustainable materials: The greening trend in the sports shoe industry continues to be promoted. Over 50% of running shoes in 2025 use recycled materials, from {{TECH_UPPER}} mesh made from recycled plastic bottles to {{TECH_MIDSOLE}} made from corn and bio-based raw materials.

Smart Integration - Smart sensors: Many premium shoe models now integrate sensors that monitor foot strike, ground contact force, and running form. Data is synchronized with mobile applications, helping runners analyze and improve their technique.

III. Top 5 Most Notable Shoe Models 2025

1. {{BRAND_NIKE}} {{PRODUCT_ALPHAFLY_3}} - "Speed Masterpiece"
   • Improved {{TECH_ZOOM_X}} cushioning with optimal thickness
   • Exclusive wing-shaped carbon plate
   • Weight only 180g for US size 9
   • Suitable for: {{TECH_MARATHON}}, speed training

2. {{BRAND_ADIDAS}} {{PRODUCT_ADIZERO_PRIME_X_2}}
   • Dual {{TECH_LIGHTSTRIKE_PRO}} technology
   • {{TECH_MIDSOLE}} thickness 50mm - technical limit
   • Flexible {{TECH_ENERGY_RODS}} design
   • Suitable for: Experienced runners seeking new sensations

3. {{BRAND_NEW_BALANCE}} {{PRODUCT_FUELCELL_SUPERCOMP_ELITE_V4}}
   • {{TECH_FUELCELL}} foam with new formula
   • Dual energy carbon plate system
   • Ultra-light {{TECH_UPPER}} {{TECH_ENGINEERED_MESH}}
   • Suitable for: Balance between speed and stability

4. {{BRAND_ASICS}} {{PRODUCT_METASPEED_SKY}}
   • Premium {{TECH_FLYTEFOAM_BLAST_TURBO}}
   • {{TECH_GUIDESOLE}} technology reduces energy consumption
   • Design specifically for high-cadence runners
   • Suitable for: Professional racing runners

5. {{BRAND_SAUCONY}} {{PRODUCT_ENDORPHIN_PRO_4}}
   • Ultra-light {{TECH_PWRRUN_HG}} foam cushioning
   • {{TECH_SPEEDROLL}} technology creates propulsion
   • Perfect Formfit {{TECH_UPPER}} fit
   • Suitable for: Diverse from beginner to pro

IV. Shoe Selection Criteria

To choose the "crown" shoe for yourself, runners need to consider factors:

• Running type: {{TECH_ROAD_RUNNING}}, {{TECH_TRAIL_RUNNING}}, or {{TECH_TRACK}}?
• Distance: 5K, 10K, half marathon, or full marathon?
• Running gait: {{TECH_NEUTRAL}}, {{TECH_OVERPRONATION}}, or {{TECH_UNDERPRONATION}}?
• Body weight: Affects cushioning durability
• Budget: From 2-6 million VND depending on segment
• Terrain: Concrete, dirt roads, or complex terrain?

V. Conclusion: Break Through All Limits

2025 is truly a golden time for the Vietnamese running community. With diverse technologies and models, every runner can find the perfect "crown" for their feet. Most importantly, listen to your body and choose shoes not just based on technology, but also on comfort when wearing them.

Remember: The best shoes are not the most expensive, but the most suitable for you. Come to Myshoes.vn, we commit to bringing the best shopping experiences and most professional advice to help you find the perfect companion on every road.`,
        "2": `I. Journey From "Sale Hunter" To Smart Consumer

5 years ago, I was a dedicated "sale hunter". My goal was always to find the cheapest shoes, whether they were authentic or replicas. I was proud of my ability to find shoes that were "99% identical" at just 1/3 or 1/4 of the real price. But then an event completely changed my perspective.

It was on a rainy day, when I was wearing a fake shoe I bought for 400k, the sole suddenly came off causing me to slip and injure my ankle. 2 weeks of immobility and medical costs 10 times the amount I "saved" taught me an expensive lesson.

II. Unmistakable Differences

1. Materials: From the Smallest Details
   • {{TECH_UPPER}}: Authentic shoes use premium {{TECH_ENGINEERED_MESH}}, with carefully calculated stretch and breathability. Fakes usually use regular fabric, prone to tearing and causing heat.
   • Cushioning: Exclusive foam technologies like {{TECH_BOOST}}, {{TECH_ZOOM_X}}, {{TECH_REACT}} are only found in authentic products. Fakes use cheap foam that quickly deflates and lacks elasticity.
   • Adhesive: Authentic shoes use specialized industrial adhesive that withstands high temperature and pull force. Fakes use regular glue that easily peels.

2. Manufacturing Technology
   • Strict {{TECH_QC}} ({{TECH_QUALITY_CONTROL}}) process
   • High-tech machinery from Germany, Japan
   • Experienced engineering team
   • Inspection at every production stage

3. Usage Experience
   • Perfect foot fit
   • Even force distribution
   • Superior durability (average 800-1000km)
   • Authentic 2-year warranty

III. Consequences of Using Fake Shoes

1. Health Risks
   • Knee and ankle injuries
   • Back pain, spinal pain
   • Plantar fasciitis
   • Gait deformity

2. Economic Loss
   • Low lifespan, frequent replacement needed
   • Medical costs when injuries occur
   • No resale value

3. Environmental Issues
   • Use of toxic chemicals
   • Uncontrolled production process
   • Quickly becomes waste

IV. How to Distinguish Authentic from Fake?

1. Check Packaging
   • Sturdy box, sharp printing
   • QR code, serial number
   • Anti-counterfeit labels

2. Observe Details
   • Meticulous, even stitching
   • Clear, non-blurry logo printing
   • Consistent colors, no defects

3. Feel When Using
   • Light and comfortable from first wear
   • No chemical smell
   • Good elasticity

V. Sincere Advice

After 3 years of using only authentic shoes, I realized: "Expensive once but quality forever". Every morning when I put on authentic shoes, I feel trust and peace of mind. No more worries about soles coming off while running, no more fear of unexpected injuries.

Especially with Myshoes.vn's warranty policy, I'm completely confident about quality. The professional consulting team helps me choose the most suitable shoes for my needs and budget.

Invest in your feet - the foundation that supports your entire body. Don't let short-term savings cost you dearly later.`,
        "3": `I. End-of-Year 2025 Sneaker Trends: Convenient & Versatile

Year-end is always a busy time with many events: parties, travel, shopping, and gatherings. A comfortable, flexible sneaker becomes essential for every fashion enthusiast. 2025 sees the rise of "all-in-one" sneakers - can be styled from casual to semi-formal, from office to year-end parties.

According to the latest survey from Myshoes.vn, 85% of customers seeking year-end sneakers prioritize 3 factors: maximum comfort, easy styling, and reasonable prices. Below are the 5 most prominent names that fully meet these criteria.

II. Top 5 Worth-Every-Penny Sneakers

1. {{BRAND_NIKE}} {{PRODUCT_AIR_FORCE_1}} '07 Premium
   • Advantages: Classic design never goes out of style
   • Technology: {{TECH_AIR_SOLE}} unit throughout sole
   • Material: Premium leather, easy to clean
   • Styling: Jeans, joggers, or even suits
   • Price: 2,500,000 VND
   • Rating: 9.5/10 - "Basic but never boring"

2. {{BRAND_ADIDAS}} {{PRODUCT_ULTRABOOST_LIGHT}}
   • Advantages: Most comfortable in segment
   • Technology: New {{TECH_BOOST}} foam 30% lighter
   • Material: {{TECH_PRIMAKNIT}}+ 4-way stretch
   • Styling: Sporty chic, streetwear
   • Price: 4,200,000 VND
   • Rating: 9.8/10 - "Like walking on clouds all day"

3. {{BRAND_NEW_BALANCE}} {{PRODUCT_NB_990V6}}
   • Advantages: Excellent support for feet
   • Technology: {{TECH_FUELCELL}} {{TECH_MIDSOLE}} combined with {{TECH_ENCAP}}
   • Material: Pigskin suede and premium mesh
   • Styling: Smart casual, business casual
   • Price: 5,500,000 VND
   • Rating: 9.2/10 - "Classy and comfortable"

4. {{BRAND_VEJA}} {{PRODUCT_CAMPO_LEATHER}}
   • Advantages: Eco-friendly, minimalist design
   • Technology: {{TECH_L_FOAM}} cushioning from recycled corn
   • Material: Chrome-free leather
   • Styling: Minimalist, sustainable fashion
   • Price: 2,800,000 VND
   • Rating: 8.8/10 - "Responsible style"

5. {{BRAND_CONVERSE}} {{PRODUCT_CHUCK_70}} Vintage Canvas
   • Advantages: Affordable price, diverse colors
   • Technology: Classic rubber sole, durable
   • Material: Premium 12oz canvas
   • Styling: Streetwear, retro style
   • Price: 1,500,000 VND
   • Rating: 9.0/10 - "Ageless icon"

III. Tips for Choosing Sneakers by Need

1. Office Workers
   • Priority: Neutral colors (white, black, beige)
   • Style: Neat, not too sporty
   • Comfort: Top priority

2. Active Youth
   • Priority: Youthful colors, innovative design
   • Features: Light, flexible
   • Budget: Flexible 1-3 million

3. Middle-Aged
   • Priority: Comfortable, good support
   • Design: Simple, easy to style
   • Brand: Reputable, durable

IV. Smart Styling with Sneakers

1. End-of-Year Smart Casual
   • White sneakers + Chinos + Shirt
   • Add blazer for important events
   • Accessories: Low-cut socks, leather watch

2. Energetic Streetwear
   • Colored sneakers + Joggers + Hoodie
   • Layer with denim or bomber jacket
   • Accessories: Bucket hat, backpack

3. Festive Parties
   • Luxurious sneakers + Dress pants + Polo
   • Colors: Red, deep blue, bronze
   • Accessories: Leather strap, clutch

V. Expert Advice

"Don't chase quantity, invest in quality" - that's the sharing from fashion expert Nguyen Minh Anh. According to him, everyone should own 3-4 quality sneakers instead of 10-15 cheap pairs.

End of 2025, Myshoes.vn brings the special "Year-End Comfort" promotion with up to 30% discount on premium sneaker lines. Specifically, we commit:
• Authentic 24-month warranty
• Size exchange within 30 days
• Free style consultation

Come to Myshoes.vn to find your perfect companion in these busy year-end days!`,
        "4": `I. Winter 2025: Harsh Weather and Warm Shoe Needs

According to forecasts from the Central Meteorological Center, winter 2025 is predicted to be colder and longer than previous years. Temperatures in the North can drop below 10°C, while the Central region is also affected by Northeast monsoon waves. This is the time to prepare warm shoes to protect your feet - the most sensitive part to low temperatures.

II. Modern Heat Retention Technology in Winter Shoes

1. Heat Retention Technology
   • Silver Ion thermal fiber: Antibacterial and heat retention
   • {{TECH_THINSULATE}}™ lining: 1.5x warmer than regular cotton
   • {{TECH_GORE_TEX}} waterproof membrane: Blocks water, releases moisture

2. Insulating Materials
   • Wool Felt: Natural pressed wool heat retention
   • Shearling Lining: Soft sheepskin lining
   • Memory Foam Insole: Molding thermal cushion

3. Cold-Resistant Design
   • High ankle collar
   • Anti-slip {{PRODUCT_WINTER_GRIP}} sole
   • Watertight seams

III. Top 5 Best Winter Boots 2025

1. {{BRAND_TIMBERLAND}} {{PRODUCT_SIX_INCH_PREMIUM_BOOT}}
   • Temperature tolerance: -20°C
   • Technology: Waterproof leather, {{TECH_PRIMALOFT}} insulation
   • Price: 4,500,000 VND
   • Suitable for: City, light outdoor

2. {{BRAND_DR_MARTENS}} {{PRODUCT_WINTER_GRIP}}
   • Temperature tolerance: -15°C
   • Technology: Thermal sole, fur lining
   • Price: 3,800,000 VND
   • Suitable for: Street style, work

3. {{BRAND_UGG}} {{PRODUCT_CLASSIC_ULTRA_MINI}}
   • Temperature tolerance: -10°C
   • Technology: Twinface sheepskin, {{TECH_TREADLITE}} sole
   • Price: 3,200,000 VND
   • Suitable for: Casual, going out

4. {{BRAND_SOREL}} {{PRODUCT_CARIBOU_BOOT}}
   • Temperature tolerance: -40°C
   • Technology: Waterproof nubuck, felt liner
   • Price: 5,500,000 VND
   • Suitable for: Snow, harsh weather

5. {{BRAND_ECCO}} {{PRODUCT_SOFT_7_WINTER}}
   • Temperature tolerance: -25°C
   • Technology: Yak leather, thermal insole
   • Price: 3,600,000 VND
   • Suitable for: Office, smart casual

IV. Tips for Choosing Warm Shoes by Region

1. North (Hanoi & neighboring provinces)
   • Temperature: 8-15°C, high humidity
   • Priority: Waterproof, good heat retention
   • Style: Mid to high-top boots

2. Central (Da Nang, Hue)
   • Temperature: 15-20°C, lots of rain
   • Priority: Breathable, waterproof
   • Style: Warm sneakers, low-top boots

3. South (Ho Chi Minh City & provinces)
   • Temperature: 20-25°C, chilly at night
   • Priority: Airy, light
   • Style: Thin sneakers, sports shoes

V. Care and Maintenance of Winter Shoes

1. Daily Cleaning
   • Use soft brush to clean mud
   • Air dry naturally, avoid high heat
   • Use waterproof spray periodically

2. Storage When Not in Use
   • Stuff newspaper to maintain shoe shape
   • Store in dry, airy place
   • Avoid direct sunlight

3. "Emergency" for Wet Shoes
   • Remove insoles immediately
   • Stuff with dry newspaper to absorb moisture
   • Dry in shade for 2-3 days

VI. Special "Winter Ready" Promotion

On the occasion of monsoon season, Myshoes.vn launches special promotion:
• 25% off all winter boots
• Free shoe care kit worth 500k
• Free nationwide shipping
• Authentic 2-year warranty

Don't let the cold affect your health and life. Prepare warm shoes starting today! Visit Myshoes.vn or come directly to stores for free consultation and choose your perfect companion this winter.`,
        "5": `I. Latest Collection with Many Colors and Comfortable Technology…

Fall 2025 brings fresh air to the sneaker world with perfect combination of modern technology and fashionable design. Major brands have launched special collections, focusing on waterproof features and smart design suitable for the characteristic cool weather of fall.

II. Fall Sneaker Selection Criteria

When choosing sneakers for fall, consider factors:

• Materials: Choose materials with light water resistance like leather, waterproof-treated suede
• Colors: Warm muted tones like brown, beige, moss green, burgundy
• Warmth: Thin lining that keeps warm but still breathable
• Sole: Good slip resistance for rainy humid days

III. Top Picks Fall Sneakers 2025

1. {{BRAND_NIKE}} {{PRODUCT_AIR_FORCE_1}} "Autumn Pack"
   • Design: Camel brown with gum sole
   • Technology: Visible {{TECH_AIR_MAX}} unit, leather {{TECH_UPPER}}
   • Price: 3,200,000 VND
   • Features: Light waterproof, easy styling

2. {{BRAND_ADIDAS}} {{PRODUCT_STAN_SMITH}} "Wool Edition"
   • Design: {{TECH_UPPER}} made from warm wool blend
   • Technology: {{TECH_CLOUDFOAM}} comfort insole
   • Price: 2,800,000 VND
   • Features: Light, warm, suitable for cool weather

3. {{BRAND_NEW_BALANCE}} {{PRODUCT_NB_574}} "Weatherproof"
   • Design: Waterproof-treated suede and mesh
   • Technology: {{TECH_ENCAP}} {{TECH_MIDSOLE}}, anti-slip sole
   • Price: 2,500,000 VND
   • Features: Durable, suitable for daily work

4. {{BRAND_CONVERSE}} {{PRODUCT_CHUCK_70}} "Shield Canvas"
   • Design: Waterproof canvas, olive color
   • Technology: Thick rubber sole, comfortable insole
   • Price: 1,800,000 VND
   • Features: Affordable, unisex

5. {{BRAND_PUMA}} {{PRODUCT_RS_X_ECHO}}
   • Design: Gray combined with burnt orange
   • Technology: RS cushioning system
   • Price: 2,900,000 VND
   • Features: Comfortable, futuristic design

IV. Styling with Fall Sneakers

• Casual Style: Sneakers + Jeans + Hoodie + Denim jacket
• Smart Casual: Sneakers + Chinos + Shirt + Blazer
• Street Style: Sneakers + Joggers + Graphic tee + Bomber jacket

V. Fall Sneaker Maintenance

• Use waterproof spray before use
• Clean with damp cloth after outdoor use
• Avoid direct sun exposure
• Use shoe tree to maintain shape

Myshoes.vn currently has special promotion for fall sneakers with up to 30% discount. Come to the nearest store or order online to own the most beautiful sneakers this season!`,
      },
    },
    Testimonials: {
      title: "Testimonials",
    },
    Newsletter: {
      title: "Get Offers",
      subtitle: "Subscribe to receive 100K discount code",
      emailPlaceholder: "Your email",
      subscribeButton: "Subscribe",
      emailRequired: "Please enter your email!",
      emailInvalid: "Invalid email!",
      success: "🎉 Subscription successful! 100K discount code has been sent to {email}",
    },
    Footer: {
      companyDescription: "Authentic sports shoe store with diverse world-renowned brands.",
      quickLinks: "Quick Links",
      home: "Home",
      products: "Products",
      about: "About",
      contact: "Contact",
      customerService: "Customer Service",
      returnPolicy: "Return Policy",
      purchaseGuide: "Purchase Guide",
      warranty: "Product Warranty",
      faq: "FAQ",
      contactInfo: "Contact Info",
      address: "123 ABC Street, District 1, Ho Chi Minh City",
      phone: "(028) 1234 5678",
      email: "info{'@'}shoezshop.com",
      hours: "8:00 - 22:00 (Mon - Sun)",
      copyright: "© {year} Shoez Shop. All rights reserved.",
    },
    VideoHero: {
      badge: "New Collection",
      defaultTitle: "SPORTS SHOES",
      defaultDescription: "Choose shoes that match your style",
      defaultCta: "Explore Now",
      hover3D: "✨ Hover to rotate 3D shoe",
    },
    ShoeCustomizer: {
      title: "Design Your Own Shoes",
      subtitle: "Customize colors, materials and create unique shoes for your personal style",
      selectModel: "Select Shoe Model",
      customizeColors: "Customize Colors",
      material: "Material",
      saveDesign: "💾 Save Design",
      useDesign: "USE",
      viewMore: "View More Designs ↓",
      communityDesigns: "Featured Designs from Community",
      saveSuccess: "🎉 Design saved! You can view it in \"My Designs\" section",
      parts: {
        upper: "Upper",
        sole: "Sole",
        laces: "Laces",
        logo: "Logo",
      },
      materials: {
        suede: "Suede",
        leather: "Genuine Leather",
        canvas: "Canvas",
        knit: "Knit",
        mesh: "Mesh",
      },
      mode2D: "2D",
      mode3D: "3D",
    },
  },
  Admin: {
    Dashboard: {
      title: "Dashboard",
      subtitle: "System overview",
      revenue: "Revenue",
      orders: "Orders",
      products: "Products",
      customers: "Customers",
      active: "Active",
      last7DaysRevenue: "Revenue in last 7 days",
      noData: "No data",
      topProducts: "Top selling products",
      recentOrders: "Recent orders",
      orderId: "Order ID",
      customer: "Customer",
      date: "Date",
      total: "Total",
      status: "Status",
      actions: "Actions",
      view: "View",
      retry: "Retry",
      revenueChangeSuffix: "% vs. last month",
      registeredUsers: "Registered users",
      totalRevenueLabel: "Total revenue:",
      soldSuffix: "sold",
    },
    Status: {
      pending: "Pending",
      processing: "Processing",
      confirmed: "Confirmed",
      shipping: "Shipping",
      complete: "Complete",
      completed: "Completed",
      delivered: "Delivered",
      cancelled: "Cancelled",
      canceled: "Canceled",
    },
    Nav: {
      dashboard: "Dashboard",
      products: "Products",
      orders: "Orders",
      customers: "Customers",
      categories: "Categories",
      brands: "Brands",
      analytics: "Analytics",
      settings: "Settings",
      title: "Shoez Admin",
      panel: "Management Panel",
      logoutConfirm: "Are you sure you want to log out?",
      logout: "Log out"
    },
    Header: {
      searchPlaceholder: "Search...",
      notifications: "Notifications",
      clearAll: "Clear all",
      noNotifications: "No notifications",
      timeAgo: {
        justNow: "Just now",
        minutesAgo: "{count} minutes ago",
        hoursAgo: "{count} hours ago",
        daysAgo: "{count} days ago",
      },
      error: {
        markRespondedFailed: "Unable to mark notification as responded. Please try again."
      }
    },
    Categories: {
      title: "Categories",
      subtitle: "Manage your store's product categories",
      searchPlaceholder: "Search by category name...",
      add: "Add category",
      total: "Total categories",
      active: "Active",
      inactive: "Inactive",
      statusActive: "Active",
      statusInactive: "Inactive",
      productsCount: "products",
      edit: "Edit",
      delete: "Delete",
      toggleDeactivate: "Deactivate",
      toggleActivate: "Activate",
      emptyTitle: "No categories yet",
      emptySubtitle: "Add your first category to get started",
      modalEditTitle: "Edit category",
      modalAddTitle: "Add new category",
      nameLabel: "Category name *",
      namePlaceholder: "Enter category name",
      descLabel: "Description",
      descPlaceholder: "Enter category description",
      activeLabel: "Activate category",
      cancel: "Cancel",
      update: "Update",
      create: "Create",
      confirmTitle: "Confirm",
      confirmDeleteMessage: "Are you sure you want to delete this category?",
      actionFailed: "Action failed",
      loadFailed: "Unable to load categories",
      createSuccess: "Category created successfully!",
      updateSuccess: "Category updated successfully!",
      deleteSuccess: "Category deleted successfully!",
      toggleSuccessDeactivate: "Category deactivated!",
      toggleSuccessActivate: "Category activated!"
    },
    Brands: {
      title: "Brands",
      subtitle: "Manage your store's product brands",
      searchPlaceholder: "Search by brand name...",
      add: "Add brand",
      total: "Total brands",
      active: "Active",
      inactive: "Inactive",
      statusActive: "Active",
      statusInactive: "Inactive",
      edit: "Edit",
      delete: "Delete",
      toggleDeactivate: "Deactivate",
      toggleActivate: "Activate",
      emptyTitle: "No brands yet",
      emptySubtitle: "Add your first brand to get started",
      modalEditTitle: "Edit brand",
      modalAddTitle: "Add new brand",
      nameLabel: "Brand name",
      namePlaceholder: "Enter brand name",
      nameRequired: "Brand name is required",
      logoLabel: "Logo",
      logoUploadLabel: "Upload image (optional)",
      logoSelectFile: "Select image file",
      logoOr: "OR",
      logoUrlLabel: "Enter logo URL",
      logoUrlPlaceholder: "https://example.com/logo.png",
      logoRemove: "Remove image",
      descLabel: "Description",
      descPlaceholder: "Enter brand description (optional)",
      activeLabel: "Activate brand",
      cancel: "Cancel",
      update: "Update",
      create: "Create",
      confirmTitle: "Confirm",
      confirmDeleteMessage: "Are you sure you want to delete this brand?",
      actionFailed: "Action failed",
      loadFailed: "Unable to load brands",
      createSuccess: "Brand created successfully!",
      updateSuccess: "Brand updated successfully!",
      deleteSuccess: "Brand deleted successfully!",
      toggleSuccessDeactivate: "Brand deactivated!",
      toggleSuccessActivate: "Brand activated!",
      fileMustBeImage: "File must be an image",
      fileSizeExceeded: "File size must not exceed 5MB",
      noResponseFromServer: "No response from server"
    },
    Products: {
      title: "Product management",
      subtitle: "List of all products",
      addNew: "Add new product",
      filters: {
        searchLabel: "Search",
        searchPlaceholder: "Product name...",
        category: "Category",
        brand: "Brand",
        all: "All",
        status: "Status",
        statusActive: "Active",
        statusInactive: "Inactive",
        statusOOS: "Out of stock",
        sort: "Sort",
        sortCreated: "Created at",
        sortName: "Product name",
        sortPrice: "Price",
        sortStock: "Stock",
        orderLabel: "Order:",
        newest: "Newest",
        oldest: "Oldest",
        ratingFrom: "Rating from:",
        ratingTo: "To:",
        clearRating: "Clear rating filter",
        quick: "Quick:",
        starUnit: "stars",
        quickPresets: {
          range: "{stars} ({min}-{max} {unit})",
        },
      },
      table: {
        product: "Product",
        category: "Category",
        price: "Price",
        discount: "Discount",
        stock: "Stock",
        rating: "Rating",
        status: "Status",
        createdAt: "Created at",
        actions: "Actions",
        imageFallback: "Image",
        noDiscount: "None",
        itemsSuffix: "items",
        reviewsSuffix: "reviews",
        viewDetail: "View detail",
        edit: "Edit",
        delete: "Delete",
      },
      pagination: {
        showing: "Showing",
        ofTotal: "of",
        products: "products",
        perPage: "Per page:",
        prev: "Prev",
        next: "Next",
      },
      confirm: {
        deleteTitle: "Are you sure you want to delete this product?",
        deleteNamed: "Are you sure you want to delete product \"{name}\"? This action cannot be undone.",
        success: "Product deleted successfully!",
        error: "An error occurred while deleting the product",
      },
      rating: {
        notRated: "Not rated",
      },
      statusLabels: {
        inStock: "Active",
        lowStock: "Low stock",
        outOfStock: "Out of stock",
      }
    },
    AddProduct: {
      title: "Add new product",
      form: {
        nameLabel: "Product name *",
        namePlaceholder: "Enter product name",
        brandLabel: "Brand",
        brandPlaceholder: "Nike, Adidas, ...",
        categoryLabel: "Category",
        categoryPlaceholder: "Sneakers, sandals, ...",
        sizesLabel: "Shoe sizes (comma separated)",
        sizesPlaceholder: "39, 40, 41, ...",
        descriptionPlaceholder: "Enter detailed description",
        priceLabel: "Price (VND) *",
        stockLabel: "Stock",
        imagesLabel: "Product images",
        colorsLabel: "Colors (comma separated)",
        colorsPlaceholder: "Red, blue, white, ...",
        submitButton: "Add product",
      },
      messages: {
        success: "✅ Product added successfully!",
        error: "❌ An error occurred while adding product!",
      }
    },
    Orders: {
      title: "Order management",
      subtitle: "List of all orders",
      stats: {
        pending: "Pending",
        confirmed: "Confirmed",
        shipping: "Shipping",
        complete: "Complete",
        cancelled: "Cancelled",
      },
      filters: {
        activeFilters: "Active filters:",
        customer: "Customer",
        status: "Status",
        dateRange: "Date range",
        searchPlaceholder: "Name, email, phone, order id...",
        searchLabel: "Search",
        statusLabel: "Status",
        fromDate: "From",
        toDate: "To",
        apply: "Apply",
        clear: "Clear",
        exportCsv: "Export CSV",
        all: "All",
        pending: "Pending",
        confirmed: "Confirmed",
        shipping: "Shipping",
        delivered: "Delivered",
        complete: "Complete",
        cancelled: "Cancelled",
      },
      empty: {
        title: "No orders found",
        subtitle: "No orders match your filters.",
      },
      table: {
        orderId: "Order ID",
        customer: "Customer",
        phone: "Phone",
        date: "Order date",
        products: "Products",
        status: "Status",
        actions: "Actions",
        itemsSuffix: "items",
        view: "View details",
        confirm: "Confirm order",
        ship: "Start shipping",
        complete: "Complete order",
        cancel: "Cancel order",
        print: "Print order",
      },
      pagination: {
        showing: "Showing",
        to: "to",
        of: "of",
        orders: "orders",
        prev: "Prev",
        next: "Next",
      },
      export: {
        success: "Orders exported successfully!",
        error: "Failed to export orders",
      },
      statusMap: {
        pending: "Pending",
        confirmed: "Confirmed",
        shipping: "Shipping",
        complete: "Complete",
        cancelled: "Cancelled",
      }
    },
    Customers: {
      title: "Customers",
      subtitle: "Manage your store's user accounts",
      searchPlaceholder: "Search by name or email...",
      actions: {
        deleteSelected: "Delete selected",
        lockSelected: "Lock selected",
        unlockSelected: "Unlock selected",
        perPage: "Per page",
      },
      table: {
        fullName: "Full name",
        email: "Email",
        status: "Status",
        role: "Role",
        createdAt: "Created at",
        actions: "Actions",
        loading: "Loading data...",
        noData: "No matching data",
        locked: "Locked",
        active: "Active",
        undo: "Undo",
        delete: "Delete",
        lock: "Lock",
        unlock: "Unlock",
      },
      pagination: {
        page: "Page",
        prev: "Prev",
        next: "Next",
      },
      confirm: {
        cancel: "Cancel",
        confirm: "Confirm",
        deleteUser: "Are you sure you want to delete this user?",
        deleteUsers: "Delete {count} selected users?",
        lockAccount: "Lock this account?",
        unlockAccount: "Unlock this account?",
        lockAccounts: "Lock {count} accounts?",
        unlockAccounts: "Unlock {count} accounts?",
      },
      messages: {
        deleteSuccess: "User deleted successfully!",
        deleteUsersSuccess: "Deleted {count} users successfully!",
        deleteFailed: "Failed to delete user",
        lockSuccess: "Account locked successfully!",
        unlockSuccess: "Account unlocked successfully!",
        lockUsersSuccess: "Locked {count} accounts successfully!",
        unlockUsersSuccess: "Unlocked {count} accounts successfully!",
        lockFailed: "Lock/Unlock failed",
        actionFailed: "Action failed",
      }
    },
    Analytics: {
      title: "Analytics",
      subtitle: "System overview and business performance",
      retry: "Retry",
      topCategoriesTitle: "Top categories",
      topBrandsTitle: "Top brands",
      cards: {
        totalRevenue: "Total revenue",
        revenueChangeSuffix: "% vs. last month",
        totalOrders: "Total orders",
        totalProducts: "Total products",
        active: "Active",
        totalCustomers: "Total customers",
        registeredUsers: "Registered users",
      },
      chart: {
        revenueTitle: "Revenue in past {days} days",
        option7: "7 days",
        option14: "14 days",
        option30: "30 days",
        totalRevenue: "Total revenue:",
      },
      topProducts: {
        title: "Top selling products",
        noData: "No data",
        soldSuffix: "sold",
      },
      statusDistribution: {
        title: "Order status distribution",
      },
      recentOrders: {
        title: "Recent orders",
        empty: "No recent orders",
      },
      table: {
        orderId: "Order ID",
        customer: "Customer",
        date: "Date",
        value: "Value",
      },
      detailedRevenue: {
        title: "Detailed revenue",
        today: "Today",
        thisWeek: "This week",
        thisMonth: "This month",
        thisYear: "This year",
        ordersSuffix: "orders",
      },
      detailedOrders: {
        title: "Orders over time",
        today: "Today",
        thisWeek: "This week",
        thisMonth: "This month",
        total: "Total",
        byStatus: "Breakdown by status:",
      },
      cancellations: {
        title: "Cancellation statistics",
        totalCancelled: "Total cancelled orders",
        cancellationRate: "Cancellation rate",
        lostRevenue: "Lost revenue",
        today: "Today",
        thisWeek: "This week",
        thisMonth: "This month",
      },
      recentCancelled: {
        title: "Recent cancelled orders",
      },
      entities: {
        users: "Users",
        categories: "Categories",
        brands: "Brands",
        products: "Products",
        total: "Total:",
        active: "Active:",
        inactive: "Inactive:",
        newThisMonth: "New this month:",
        newThisWeek: "New this week:",
        admins: "Admins:",
        lowStock: "Low stock:",
        outOfStock: "Out of stock:",
        productsUnit: "products",
      },
      errors: {
        loadFailed: "Unable to load analytics data",
      }
    },
  },
  Orders: {
    Header: {
      title: "My Orders",
      totalOrders: "Total:",
      ordersSuffix: "orders",
      filters: {
        all: "All",
        pending: "Pending",
        confirmed: "Confirmed",
        shipping: "Shipping",
        complete: "Complete",
        cancelled: "Cancelled",
      },
    },
    Empty: {
      titles: {
        all: "No orders yet",
        pending: "No pending orders",
        confirmed: "No confirmed orders",
        shipping: "No orders shipping",
        complete: "No completed orders",
        cancelled: "No cancelled orders",
      },
      descriptions: {
        all: "Start shopping and your first order will appear here.",
        pending: "All your orders have been processed or no orders are in this status.",
        confirmed: "No orders have been confirmed.",
        shipping: "No orders are being shipped.",
        complete: "You don't have any completed orders yet.",
        cancelled: "You haven't cancelled any orders.",
      },
      shopNow: "Shop Now",
      viewAllOrders: "View All Orders",
    },
    StatusBadge: {
      pending: "pending",
      confirmed: "confirmed",
      shipping: "shipping",
      complete: "complete",
      cancelled: "cancelled",
    },
    Card: {
      orderDate: "Order date:",
      shippingAddress: "Shipping address:",
      trackingNumber: "Tracking number:",
      size: "Size:",
      color: "Color:",
      quantity: "Quantity:",
      viewDetail: "View Detail",
      cancelOrder: "Cancel Order",
      reorder: "Reorder",
      paymentMethods: {
        creditCard: "Credit Card",
        cod: "Cash on Delivery",
        bankTransfer: "Bank Transfer",
        momo: "MoMo Wallet",
      },
    },
    ReviewRequest: {
      title: "Review Order",
      subtitle: "Have you received your order?",
      message: "Share your experience to help others make better choices",
      later: "Later",
      reviewNow: "Review Now",
    },
    Layout: {
      cancelOrderWarning: "Cannot cancel this order. The order has been confirmed by admin. Please contact admin to cancel.",
      cancelOrderConfirm: "Are you sure you want to cancel this order?",
      cancelSuccess: "Order cancelled successfully!",
      cancelError: "Unable to cancel order",
      reorderSuccess: "Products have been added to cart!",
    },
    Pagination: {
      previousPage: "Previous page",
      nextPage: "Next page",
      goToPage: "Go to page {page}",
    },
    Loading: {
      text: "Loading orders...",
    },
  },
  Notifications: {
    Bell: {
      title: "Notifications",
      markAllAsRead: "Mark all as read",
      noNotifications: "No notifications",
      viewAll: "View All",
      timeAgo: {
        justNow: "Just now",
        minutesAgo: "{count} minutes ago",
        hoursAgo: "{count} hours ago",
        daysAgo: "{count} days ago",
      },
    },
    Toast: {
      defaultTitle: "Notification",
      orderCode: "Order code:",
    },
  },
  common: {
    and: "and",
  },
  Auth: {
    SocialLogin: {
      orLoginWith: "Or login with",
      loginWithGoogle: "Login with Google",
      loginWithFacebook: "Login with Facebook",
      agreeToTerms: "By logging in, you agree to our",
      termsOfService: "Terms of Service",
      privacyPolicy: "Privacy Policy",
    },
  },
  Cart: {
    Header: {
      title: "Cart",
      continueShopping: "Continue Shopping",
      itemsCount: "items",
    },
    Item: {
      size: "Size:",
      color: "Color:",
    },
    Summary: {
      title: "Order Summary",
      subtotal: "Subtotal",
      shippingFee: "Shipping Fee",
      shippingFree: "Free",
      discount: "Discount",
      total: "Total",
      checkout: "Checkout",
      continueShopping: "← Continue Shopping",
      itemsSuffix: "items",
    },
    Empty: {
      title: "Cart is Empty",
      description: "Add some products to your cart to start shopping",
      shopNow: "Shop Now",
    },
  },
  Contact: {
    zalo: "Contact via Zalo",
    tiktok: "Follow on TikTok",
  },
  Header: {
    home: "Home",
    products: "Products",
    about: "About",
    news: "News",
    contact: "Contact",
    navigation: {
      home: "Home",
      products: "Products",
      about: "About",
      contact: "Contact",
      favourite: "Favourite",
      login: "Login",
      register: "Register",
      profile: "Profile",
      logout: "Logout",
      greeting: "Hello, {name}",
    },
    search: {
      placeholder: "Search...",
    },
  },
  Product: {
    Breadcrumb: {
      home: "Home",
      products: "Products",
    },
    Info: {
      reviews: "reviews",
      save: "Save",
      color: "Color:",
      size: "Size:",
      selectSize: "Select size",
      quantity: "Quantity",
      available: "available",
      addToCart: "Add to Cart",
      buyNow: "Buy Now",
      addToFavourite: "Add to Favourite",
      removeFromFavourite: "Remove from Favourite",
      favourite: "Favourite",
      liked: "Liked",
      features: "Key Features",
      authentic: "100% Authentic, anti-counterfeit verification",
      freeShipping: "Free shipping nationwide for orders over 500k",
      returnPolicy: "7-day return policy if there are manufacturing defects",
      warranty: "6-month manufacturer warranty",
    },
    Tabs: {
      description: "Description",
      specifications: "Specifications",
      reviews: "Reviews",
      descriptionTitle: "Product Description",
      specificationsTitle: "Technical Specifications",
      reviewsTitle: "Customer Reviews",
      brand: "Brand",
      type: "Type",
      color: "Color",
      size: "Size",
      descriptionText: "is one of the premium sports shoe lines from",
      descriptionText2: "offering the perfect combination of fashion style and athletic performance.",
      descriptionText3: "With unique design and premium materials, this product not only ensures maximum comfort when wearing but also creates a distinctive personal style for the user.",
    },
    Reviews: {
      title: "Product Reviews",
      writeReview: "✍️ Write Review",
      filterBy: "Filter by:",
      all: "All",
      sortBy: "Sort:",
      newest: "Newest",
      oldest: "Oldest",
      highestRating: "Highest Rating",
      lowestRating: "Lowest Rating",
      showing: "Showing:",
      reviews: "reviews",
      previous: "← Previous",
      next: "Next →",
      notFound: "No reviews found",
      noReviewsForRating: "No",
      rating: "star reviews",
      noReviewsYet: "No reviews for this product yet",
      writeFirstReview: "Write the first review",
      star: "star",
      verified: "✅ Verified Purchase",
      helpful: "Helpful",
      reply: "Reply",
    },
    ReviewModal: {
      title: "Product Review",
      yourRating: "Your Rating *",
      comment: "Comment *",
      commentPlaceholder: "Share your experience with this product...",
      images: "Images (max 3 images)",
      cancel: "Cancel",
      submit: "Submit Review",
    },
    RelatedProducts: {
      title: "Related Products",
    },
    Detail: {
      notFound: "Product not found",
      backToProducts: "Back to Products",
    },
    ReviewCard: {
      verified: "✅ Verified Purchase",
      helpful: "Helpful",
      reply: "Reply",
    },
    Gallery: {
      thumbnail: "Thumbnail",
    },
  },
  Products: {
    Card: {
      favourite: "Favourite",
      liked: "Liked",
      buyNow: "Buy Now",
    },
    Filters: {
      title: "Filters",
      search: "Search",
      searchPlaceholder: "Product name...",
      brand: "Brand",
      category: "Shoe Type",
      color: "Color",
      size: "Size",
      price: "Price",
      priceFrom: "From",
      priceTo: "To",
      apply: "Apply",
      reset: "Clear Filters",
    },
    Sort: {
      sortBy: "Sort:",
      default: "Default",
      priceAsc: "Price: Low to High",
      priceDesc: "Price: High to Low",
      nameAsc: "Name: A-Z",
      nameDesc: "Name: Z-A",
      viewGrid: "Grid view",
      viewList: "List view",
    },
  },
  Profile: {
    myAccount: "My Account",
    profile: "Profile",
    myOrders: "My Orders",
    Header: {
      title: "My Profile",
      subtitle: "Manage your profile information to secure your account",
      memberSince: "Member since",
    },
    Info: {
      title: "Personal Information",
      fullName: "Full Name",
      fullNamePlaceholder: "Enter full name",
      email: "Email",
      emailPlaceholder: "Enter email",
      phone: "Phone Number",
      phonePlaceholder: "Enter phone number",
      birthday: "Birthday",
      gender: "Gender",
      genderMale: "Male",
      genderFemale: "Female",
      genderOther: "Other",
      address: "Address",
      addressPlaceholder: "Enter address",
      cancel: "Cancel",
      saving: "Saving...",
      saveChanges: "Save Changes",
      messages: {
        updateSuccess: "Profile updated successfully!",
        updateError: "Failed to update profile.",
      },
    },
    Avatar: {
      changePhoto: "Change Photo",
      note: "Note:",
      noteText: "Profile photo should be in JPG, PNG or GIF format. Maximum size 5MB.",
      invalidFormat: "Only image files (JPG, PNG, GIF) are accepted",
      fileSizeExceeded: "File size must not exceed 5MB",
      messages: {
        uploadError: "Failed to update avatar.",
      },
    },
    Password: {
      title: "Change Password",
      currentPassword: "Current Password",
      currentPasswordPlaceholder: "Enter current password",
      newPassword: "New Password",
      newPasswordPlaceholder: "Enter new password",
      confirmPassword: "Confirm New Password",
      confirmPasswordPlaceholder: "Re-enter new password",
      passwordHint: "Password must be at least 8 characters, including uppercase, lowercase and numbers",
      strength: "Password Strength:",
      strengthWeak: "Weak",
      strengthMedium: "Medium",
      strengthStrong: "Strong",
      strengthVeryStrong: "Very Strong",
      securityTips: "Security Tips:",
      tip1: "Use a password at least 8 characters long",
      tip2: "Combine uppercase, lowercase, numbers and special characters",
      tip3: "Don't use personal information as password",
      tip4: "Change password regularly every 3-6 months",
      cancel: "Cancel",
      changing: "Changing password...",
      changePassword: "Change Password",
      errors: {
        currentPasswordRequired: "Please enter current password",
        newPasswordRequired: "Please enter new password",
        newPasswordMinLength: "Password must be at least 8 characters",
        newPasswordSameAsCurrent: "New password cannot be the same as current password",
        confirmPasswordRequired: "Please confirm new password",
        confirmPasswordMismatch: "Password confirmation does not match",
      },
      messages: {
        changeSuccess: "Password updated successfully!",
        genericError: "Failed to update user information.",
      },
    },
  },
  Reviews: {
    Modal: {
      title: "Product Review",
      size: "Size:",
      color: "Color:",
      yourRating: "Your Rating *",
      selectStars: "Please select stars",
      yourComment: "Your Comment *",
      commentPlaceholder: "Share your experience with the product...",
      minChars: "Minimum 10 characters",
      needMoreChars: "Need {count} more characters",
      addMedia: "Add images or videos (optional)",
      selectMedia: "Select images/videos",
      maxFiles: "Maximum 5 files (images/videos)",
      video: "Video",
      cancel: "Cancel",
      submit: "Submit Review",
      uploadError: "Unable to upload images/videos. Please try again.",
      success: "Thank you for your review!",
      submitError: "An error occurred while submitting review",
    },
    List: {
      title: "Customer Reviews",
      noReviews: "No reviews yet",
      customer: "Customer",
      helpful: "Helpful",
      adminResponse: "Admin Response",
      admin: "Admin",
      loadMore: "Load More Reviews",
    },
    PromptBanner: {
      title: "You have {count} products to review!",
      description: "Share your experience to help others choose the right product",
      later: "Later",
      reviewNow: "Review Now",
    },
  },
  Shared: {
    ProductCategory: {
      color: "Color:",
      size: "Size:",
      liked: "Liked",
      favourite: "Favourite",
      buyNow: "Buy Now",
      login: "Login",
      close: "Close",
      addedToCart: "Added \"{productName}\" to cart!",
      loginRequiredFavourite: "You are not logged in. Please login to add products to favourites!",
      loginRequiredBuy: "You are not logged in. Please login to buy products!",
    },
    NotificationBell: {
      title: "Notifications",
      markAllRead: "Mark all as read",
      noNotifications: "No notifications",
      viewAll: "View all notifications",
      justNow: "Just now",
      minutesAgo: "{count} minutes ago",
      hoursAgo: "{count} hours ago",
      daysAgo: "{count} days ago",
      mockOrderTitle: "Order confirmed",
      mockOrderMessage: "Your order #12345 has been confirmed and is being prepared.",
      mockPromotionTitle: "Special promotion",
      mockPromotionMessage: "20% off all Nike shoes. Valid until December 31st.",
      mockSystemTitle: "System update",
      mockSystemMessage: "System will be under maintenance from 2:00 to 4:00 tomorrow.",
    },
    GlobalLoading: {
      loading: "Loading...",
    },
    StarRating: {
      rating: "Rating {rating} out of 5 stars",
      outOf: "out of 5 stars",
    },
    ToastManager: {
      close: "Close",
      success: "Success",
      error: "Error",
      info: "Information",
      warning: "Warning",
    },
    ConfirmModal: {
      title: "Confirm",
      defaultMessage: "Are you sure you want to perform this action?",
      confirm: "Confirm",
      cancel: "Cancel",
    },
    LanguageSwitcher: {
      label: "Language",
      vietnamese: "Vietnamese",
      english: "English",
      japanese: "Japanese",
    },
    Layout: {
      header: {
        home: "Home",
        products: "Products",
        about: "About Us",
        contact: "Contact",
        login: "Login",
        register: "Register",
        greeting: "Hello",
        profile: "Profile",
        logout: "Logout",
      },
      footer: {
        companyDescription: "Authentic sports shoe store with diverse world-famous brands.",
        quickLinks: "Quick Links",
        customerService: "Customer Service",
        returnPolicy: "Return Policy",
        purchaseGuide: "Purchase Guide",
        warranty: "Product Warranty",
        contactInfo: "Contact Information",
        workingHours: "8:00 - 22:00 (Monday - Sunday)",
        copyright: "© 2025 Shoez Shop. All rights reserved.",
      },
    },
    ToastNotification: {
      close: "Close",
    },
    QuantitySelector: {
      decrease: "Decrease quantity",
      increase: "Increase quantity",
      quantity: "Quantity: {quantity}",
    },
    MessengerChatWidget: {
      customerSupport: "Customer Support",
      online: "Online",
      close: "Close",
      messagePlaceholder: "Type a message...",
      sendImage: "Send image",
      openChat: "Open support chat",
      welcomeMessage: "Hello! How can I help you?",
      thankYouMessage: "Thank you! Admin will respond as soon as possible.",
      imageReceived: "Image received.",
    },
  },
  Views: {
    Login: {
      google: "Google",
      facebook: "Facebook",
    },
    Products: {
      title: "All Products",
      found: "Found {count} products",
      noResults: "No products found",
      adjustFilters: "Try adjusting filters to see more products",
      clearFilters: "Clear filters",
      previous: "Previous",
      next: "Next",
      page: "Page {current} / {total}",
    },
    Favourite: {
      emptyTitle: "You have no favorites yet",
      emptyDescription: "Add some products to view them later and buy faster.",
      explore: "Explore products",
      removeFromFavourite: "Remove from favorites",
      noDescription: "No description",
      category: "Category:",
      color: "Color:",
      size: "Size:",
      details: "Details",
    },
    NotFound: {
      title: "Page not found",
      message: "Sorry, the page you are looking for does not exist.",
      backHome: "Back to home",
    },
    VerifyEmail: {
      title: "Verify Email",
      sentTo: "We have sent a verification code to email",
      email: "your email",
      enterCode: "Enter 6-digit verification code",
      checking: "Checking...",
      verifying: "Verifying...",
      verifyButton: "Verify Email",
      noCode: "Didn't receive code?",
      resend: "Resend code",
      resendAfter: "Resend after {seconds}s",
      backToRegister: "Back to",
      register: "Register",
      emailRequired: "Email is required",
      emailInvalid: "Invalid email",
      codeRequired: "Please enter verification code",
      codeLength: "Verification code must be 6 digits",
      codeNumeric: "Verification code must contain only numbers",
      enterAllDigits: "Please enter all 6 digits",
      success: "Verification successful!",
      error: "Verification failed!",
      emailNotFound: "Email not found. Please register again.",
      resendSuccess: "Verification code resent!",
      resendError: "Resend failed!",
      pleaseRegister: "Please register to receive verification code",
    },
    OrderDetail: {
      title: "Your Order",
      thankYou: "Thank you for shopping at Shoez",
      orderId: "Order ID",
      orderDate: "Order Date",
      estimatedDelivery: "Estimated Delivery",
      productsOrdered: "Ordered Products",
      size: "Size:",
      color: "Color:",
      quantity: "Quantity:",
      shippingAddress: "Shipping Address",
      paymentMethod: "Payment Method",
      shippingMethod: "Shipping Method",
      note: "Note:",
      orderSummary: "Order Summary",
      subtotal: "Subtotal",
      shippingFee: "Shipping Fee",
      free: "Free",
      total: "Total",
      orderStatus: "Order Status",
      orderPlaced: "Order Placed",
      confirmed: "Confirmed",
      shipping: "Shipping",
      estimated: "Estimated:",
      inTransit: "Items in transit",
      completed: "Completed",
      reviewProducts: "Review Products",
      reviewDescription: "Share your experience with the products you purchased",
      review: "Review",
      continueShopping: "Continue Shopping",
      viewAllOrders: "View All Orders",
      notFound: "Order not found",
      notFoundMessage: "Order does not exist or you do not have permission to view",
      backToOrders: "Back to order list",
      statusPending: "Pending",
      statusConfirmed: "Confirmed",
      statusShipping: "Shipping",
      statusComplete: "Completed",
      statusCancelled: "Cancelled",
      paymentCOD: "Cash on Delivery",
      paymentCreditCard: "Credit Card",
      paymentMomo: "MoMo",
      paymentCODDesc: "You will pay when receiving the order",
      paymentCardDesc: "Paid by card",
      paymentTransferDesc: "Bank transfer",
      paymentMomoDesc: "Paid via MoMo",
      shippingStandard: "Standard Shipping",
      shippingExpress: "Express Shipping",
      shippingPickup: "Store Pickup",
    },
    Notifications: {
      title: "Notifications",
      subtitle: "Manage all your notifications",
      markAllRead: "Mark all as read",
      deleteAllRead: "Delete all read",
      viewDetails: "View details",
      markAsRead: "Mark as read",
      noNotifications: "No notifications",
      allNotifications: "All your notifications will appear here.",
    },
    Forbidden: {
      title: "Access Denied",
      message: "You do not have permission to access this page",
      help: "Please check your login information or contact the administrator for support.",
      backHome: "Back to home",
      login: "Login",
      reasons: "Possible reasons for this error:",
      notLoggedIn: "Not logged in",
      notLoggedInDesc: "You need to login to access",
      noPermission: "Insufficient permissions",
      noPermissionDesc: "Account does not have access permission",
      sessionExpired: "Session expired",
      sessionExpiredDesc: "Please login again",
      accountLocked: "Account locked",
      accountLockedDesc: "Contact admin to unlock",
      needHelp: "Need help?",
      email: "Email",
      hotline: "Hotline",
    },
    FAQ: {
      title: "Frequently Asked Questions (FAQ)",
      subtitle: "A collection of frequently asked questions to help you quickly find answers.",
      q1: "How to exchange size?",
      a1: "You can contact customer service within 7 days from the date of receipt and follow the exchange instructions. Please keep tags and product condition intact.",
      q2: "How long does delivery take?",
      a2: "Delivery time depends on the area and shipping company, usually 2-5 business days for inner city areas.",
      q3: "Can I return if the product is defective?",
      a3: "Yes. If the product is defective due to manufacturer, please contact customer service and provide evidence (photos/videos). Shoez Shop will guide the exchange/return or warranty process.",
      q4: "How to track my order?",
      a4: "You can check order status in Profile > Orders page or contact hotline for quick support.",
      contactSupport: "Contact Support",
    },
    Warranty: {
      title: "Product Warranty",
      subtitle: "Clear warranty information helps you shop with confidence at Shoez Shop. Here's what you need to know when requesting warranty.",
      termsTitle: "Warranty Period & Conditions",
      termsDesc: "Each product has a different warranty period; check the product page or included warranty card.",
      terms1: "Product within warranty period.",
      terms2: "Manufacturer defect (not applicable for collision, water damage).",
      terms3: "Include invoice or warranty code.",
      notCoveredTitle: "Warranty Not Covered",
      notCovered1: "Misuse, collision, drops.",
      notCovered2: "Product damage due to environmental factors or natural wear.",
      notCovered3: "Missing warranty tag/card or proof of purchase.",
      processTitle: "Warranty Process",
      process1: "Contact customer service or bring product to warranty center.",
      process2: "Staff will check and assess the cause of damage.",
      process3: "Repair or replacement according to policy if eligible.",
      contactWarranty: "Contact Warranty",
    },
    ReturnPolicy: {
      title: "Return Policy",
      subtitle: "We always strive to provide the best shopping experience. Here are the conditions and return process at Shoez Shop.",
      conditionsTitle: "Return Conditions",
      condition1: "Product with intact tags and labels, unused.",
      condition2: "Request within 7 days from receipt date.",
      condition3: "Include invoice or order number for verification.",
      processTitle: "Return Process",
      process1: "Contact customer service with order number and reason.",
      process2: "Return product following Shoez Shop instructions.",
      process3: "Receive, check and proceed with exchange/refund.",
      refundTitle: "Refund & Notes",
      refundDesc: "Refund depending on payment method: 3-14 business days.",
      refundNote: "Return shipping fees will be processed according to policy. Discounted products may not be eligible for return.",
      guideTitle: "Detailed Guide",
      guide1: "Contact customer service via Contact or hotline; provide order number and describe issue.",
      guide2: "Staff will send return instructions and confirm conditions.",
      guide3: "After receiving and checking, Shoez Shop will refund or exchange product as requested.",
      contact: "Contact",
      contactSupport: "Contact Support",
    },
    PurchaseGuide: {
      title: "Purchase Guide",
      subtitle: "Simple and quick shopping steps — follow the guide below to complete your order safely.",
      step1Title: "Choose Product",
      step1Desc: "Select size, color and quantity then add to cart.",
      step2Title: "Payment",
      step2Desc: "Choose suitable payment method: COD, card, bank transfer or e-wallet.",
      step3Title: "Track Order",
      step3Desc: "Track status in Profile page or contact customer service for details.",
      tipsTitle: "Tips",
      tip1: "Check size and product description carefully before buying.",
      tip2: "Save order number for quick lookup.",
      contactSupport: "Contact Support",
    },
  },
  OAuthCallback: {
    processing: "Processing login...",
    close: "Close",
    error: "An error occurred during login",
  },
  CheckoutLayout: {
    supportMoMo: "Need support? Contact MoMo hotline: 1800.1207",
    orderSuccess: "Order placed successfully!",
    thankYou: "Thank you for your order. Your order has been confirmed.",
    orderId: "Order ID:",
  },
  ProductDetailLayout: {
    login: "Login",
    close: "Close",
  },
  OrderDetailModal: {
    close: "Close",
    printOrder: "Print Order",
  },
  ContactTemplate: {
    title: "CONTACT",
    subtitle: "We are always ready to listen and support you. Please contact us for consultation and answers to all your questions.",
    contactInfo: "CONTACT INFORMATION",
    address: "ADDRESS",
    addressLine1: "Floor 6, 266 Doi Can, Hanoi",
    addressLine2: "P. Uoi Can, Phan Ke Binh",
    phone: "PHONE",
    email: "EMAIL",
    emailLabel: "Email",
    emailPlaceholder: "Enter Email *",
    followUs: "FOLLOW US",
    sendMessage: "SEND US A MESSAGE",
    fullName: "Full Name",
    fullNamePlaceholder: "Enter full name *",
    content: "Content",
    messagePlaceholder: "Your message",
    sendButton: "SEND MESSAGE",
    otherBranches: "OTHER BRANCHES",
    location1Name: "Cung the Hao Quan Ngua",
    location1Address: "Group 6B, Luc qua",
    location1City: "Hanoi",
    location2Name: "HO DAM TRON",
    location2Address: "Group 1B",
    location2City: "Hanoi",
    location3Name: "Bao lang Chien thang B-52",
    location3Address: "P. Doi Can",
    location3City: "Hanoi",
    needSupportNow: "NEED SUPPORT NOW?",
    supportTeam: "Our customer service team is always ready to support you 24/7",
    callNow: "CALL NOW",
    sendEmail: "SEND EMAIL",
    thankYouContact: "Thank you for contacting us! We will respond as soon as possible.",
  },
  AboutTemplate: {
    title: "ABOUT DELVOR",
    subtitle: "Premium fashion footwear brand, bringing wonderful shopping experiences and quality products to Vietnamese users",
    mission: "Our Mission",
    missionText: "We are committed to bringing the highest quality shoes, combining trendy design and maximum comfort. Each product is a crystallization of passion and creativity.",
    missionQuote: "Bringing the best shoe shopping experience to Vietnamese people",
    coreValues: "Core Values",
    coreValuesSubtitle: "The golden principles that make Delvor different",
    quality: "Quality",
    qualityText: "Each pair of shoes is manufactured with strict quality control processes, ensuring durability and maximum comfort.",
    design: "Design",
    designText: "The creative design team continuously brings unique, fashionable shoe models that align with global trends.",
    community: "Community",
    communityText: "Building a shoe-loving community, sharing knowledge and spreading passion to all customers.",
    journey: "Development Journey",
    timeline1Title: "Beginning",
    timeline1Text: "Delvor was founded with the mission to bring the first quality shoes to the Vietnamese market.",
    timeline2Title: "Expansion",
    timeline2Text: "Launching online store, bringing products to customers nationwide.",
    timeline3Title: "Breakthrough",
    timeline3Text: "Introducing premium product lines, collaborating with international designers.",
    timeline4Title: "Present",
    timeline4Text: "Becoming one of the most beloved shoe brands with over 50,000 trusted customers.",
    ctaTitle: "Ready to Explore?",
    ctaSubtitle: "Discover our latest shoe collection and find your perfect pair",
    shopNow: "SHOP NOW",
    contact: "CONTACT",
  },
};
