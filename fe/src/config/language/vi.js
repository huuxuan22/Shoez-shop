export default {
  hello: "Xin chào",
  login: "Đăng nhập",
  logout: "Đăng xuất",
  register: "Đăng ký",
  confirmLogout: "Bạn có chắc chắn muốn đăng xuất?",

  Login: {
    welcome: "Chào mừng",
    subtitle: "Đăng nhập để trải nghiệm dịch vụ",
    emailLabel: "Email",
    emailPlaceholder: "Nhập email",
    passwordLabel: "Mật khẩu",
    passwordPlaceholder: "Nhập mật khẩu",
    forgotPassword: "Quên mật khẩu?",
    loginButton: "Đăng nhập",
    orContinueWith: "Hoặc tiếp tục với",
    noAccount: "Chưa có tài khoản?",
    registerLink: "Đăng ký ngay",
    adminLoginLink: "Đăng nhập với tài khoản quản trị",
    validation: {
      emailRequired: "Vui lòng nhập email",
      emailInvalid: "Email không hợp lệ",
      passwordRequired: "Vui lòng nhập mật khẩu",
      passwordMinLength: "Mật khẩu tối thiểu 6 ký tự",
    },
    messages: {
      success: "Đăng nhập thành công!",
      googleSuccess: "Đăng nhập Google thành công!",
      facebookSuccess: "Đăng nhập Facebook thành công!",
      oauthSuccess: "Đăng nhập {provider} thành công!",
      error: "Có lỗi xảy ra khi đăng nhập",
      invalidCredentials: "Sai email hoặc mật khẩu!",
    }
  },

  Register: {
    title: "Đăng ký",
    subtitle: "Tạo tài khoản mới để trải nghiệm",
    fullNameLabel: "Họ và tên",
    fullNamePlaceholder: "Nhập họ và tên",
    emailLabel: "Email",
    emailPlaceholder: "Nhập email",
    passwordLabel: "Mật khẩu",
    passwordPlaceholder: "Nhập mật khẩu",
    phoneLabel: "Số điện thoại",
    phonePlaceholder: "Nhập số điện thoại (VD: 0912345678)",
    registerButton: "Đăng ký",
    hasAccount: "Đã có tài khoản?",
    loginLink: "Đăng nhập ngay",
    validation: {
      fullNameRequired: "Vui lòng nhập họ và tên",
      fullNameMin: "Họ và tên phải có ít nhất 2 ký tự",
      fullNameMax: "Họ và tên không được quá 64 ký tự",
      emailRequired: "Vui lòng nhập email",
      emailInvalid: "Email không hợp lệ",
      emailMin: "Email phải từ 6 đến 64 ký tự",
      emailMax: "Email phải từ 6 đến 64 ký tự",
      passwordRequired: "Vui lòng nhập mật khẩu",
      passwordMin: "Mật khẩu phải có ít nhất 6 ký tự",
      passwordMax: "Mật khẩu không được quá 64 ký tự",
      phoneRequired: "Vui lòng nhập số điện thoại",
      phoneInvalid: "Số điện thoại không hợp lệ (VD: 0912345678 hoặc +84912345678)",
    },
    messages: {
      success: "Đã gửi mã xác thực đến email của bạn!",
      error: "Đăng ký thất bại!",
    }
  },

  AdminLogin: {
    title: "Admin Portal",
    subtitle: "Shoez Management System",
    emailLabel: "Email hoặc Tên đăng nhập",
    emailPlaceholder: "admin@shoez.com",
    passwordLabel: "Mật khẩu",
    loginButton: "Đăng nhập",
    processing: "Đang xử lý...",
    or: "hoặc",
    customerLoginLink: "Đăng nhập với tài khoản khách hàng",
    securityNotice: "Đây là khu vực quản trị hệ thống. Chỉ dành cho người quản lý được ủy quyền. Mọi hành động đều được ghi nhận.",
    copyright: "© 2025 Shoez Shop. All rights reserved.",
    messages: {
      fillAllFields: "Vui lòng nhập đầy đủ thông tin",
      noPermission: "Bạn không có quyền truy cập vào khu vực quản trị",
      success: "Đăng nhập thành công! Đang chuyển hướng...",
      invalidCredentials: "Email hoặc mật khẩu không đúng",
    }
  },

  Navigation: {
    home: "Trang chủ",
    products: "Sản phẩm",
    about: "Về chúng tôi",
    news: "Tin tức",
    contact: "Liên hệ",
  },
  HEROSECTION: {
    badge: "GIẢM GIÁ ĐẾN 50%",
    title1: "SHOEZ",
    title2: "SHOP",
    subtitle: "GIÀY THỂ THAO CHÍNH HÃNG CAO CẤP",
    ctaExplore: "KHÁM PHÁ NGAY",
    ctaViewProducts: "XEM SẢN PHẨM →",
    statsProducts: "SẢN PHẨM",
    statsCustomers: "KHÁCH HÀNG",
    statsSatisfaction: "HÀI LÒNG",
    bgAlt: "Nền giày thể thao cao cấp",
  },

  Home: {
    FeaturedProducts: {
      title: "Sản phẩm nổi bật",
      subtitle: "Những đôi giày được yêu thích nhất",
      loading: "Đang tải sản phẩm...",
      error: "Có lỗi xảy ra khi tải sản phẩm:",
      retry: "Thử lại",
      menShoes: "Giày nam",
      womenShoes: "Giày nữ",
      sale: "🔥 Sale",
      topRated: "⭐ Đánh giá cao",
      viewAll: "Xem tất cả",
      empty: "Không có sản phẩm nào để hiển thị.",
      errorLoad: "Có lỗi xảy ra khi tải dữ liệu sản phẩm",
    },
    BrandSection: {
      title: "Thương hiệu",
      empty: "Chưa có thương hiệu nào",
      officialPartner: "Đối tác chính thức",
      authentic: "Hàng chính hãng 100%",
      globalWarranty: "Bảo hành toàn cầu",
    },
    NewsSection: {
      title: "TIN TỨC SHOEZ.VN",
      hashtag: "#BLOG",
      brandName: "Myshoes.vn",
      articles: {
        "1": {
          title: 'GIÀY CHẠY BỘ NÀO ĐANG LÀ "CHIẾC VƯƠNG MIỆN" CỦA DÂN RUNNER 2025?',
          excerpt: 'Lời Mở Đầu: Đỉnh Cao Của Công Nghệ Giày Chạy 2025…',
        },
        "2": {
          title: 'Đừng Hỏi Vì Sao Tôi Chỉ Mang Giày Chính Hãng – Câu Trả Lời Nằm Ở Cảm Giác Khi Xỏ Chân Vào',
          excerpt: 'Tôi đã từng là một "thợ săn sale" giày fake…',
        },
        "3": {
          title: 'Gợi ý 5 đôi sneaker tiện lợi và êm chân phù hợp cuối năm 2025',
          excerpt: 'Cuối năm luôn là thời điểm lý tưởng để sắm sửa…',
        },
        "4": {
          title: 'Gió Lạnh Về Rồi, Bạn Đã Có Giày Ấm Chưa?',
          excerpt: 'Mở đầu Khi những cơn gió lạnh đầu mùa bắt đầu len lỏi…',
        },
        "5": {
          title: 'Top mẫu sneaker đáng sắm mùa thu 2025',
          excerpt: 'BST mới nhất với nhiều màu sắc và công nghệ êm ái…',
        },
        "6": {
          title: 'Cách chọn size giày online: mẹo từ chuyên gia',
          excerpt: 'Hướng dẫn đo chuẩn, tránh đổi trả phiền phức.',
        },
      },
    },
    NewsDetail: {
      back: "Quay lại",
      tableOfContents: "Mục lục",
      relatedImages: "Hình ảnh liên quan",
      image: "Hình ảnh",
      imageIndex: "Hình ảnh {index}",
      imageForSection: "Hình ảnh cho {section}",
      share: "Chia sẻ:",
      comments: "Bình luận",
      enterComment: "Nhập bình luận của bạn...",
      submitComment: "Gửi bình luận",
      guest: "Khách",
      noComments: "Chưa có bình luận nào.",
      relatedArticles: "Bài viết liên quan",
      articleNotFound: "Bài báo không tồn tại.",
      linkCopied: "Đã copy liên kết bài viết!",
      author: "Tác giả: Myshoes Team",
      views: "lượt xem",
      articleContent: {
        "1": `I. Lời Mở Đầu: Đỉnh Cao Của Công Nghệ Giày Chạy 2025

Năm 2025 đánh dấu một bước ngoặt lớn trong ngành công nghiệp giày chạy bộ. Không chỉ là những cải tiến nhỏ lẻ, chúng ta đang chứng kiến một cuộc cách mạng thực sự về công nghệ và vật liệu. Các thương hiệu lớn đã đầu tư hàng triệu đô la vào nghiên cứu và phát triển, mang đến những sản phẩm không chỉ giúp cải thiện thành tích mà còn bảo vệ sức khỏe của runner.

Thị trường giày chạy bộ năm 2025 chứng kiến sự cạnh tranh khốc liệt giữa các ông lớn như {{BRAND_NIKE}}, {{BRAND_ADIDAS}}, {{BRAND_NEW_BALANCE}} và {{BRAND_ASICS}}. Mỗi hãng đều mang đến những công nghệ độc quyền, từ hệ thống đệm siêu nhẹ cho đến cảm biến thông minh tích hợp. Người tiêu dùng giờ đây không chỉ tìm kiếm một đôi giày êm ái, mà còn cần một "trợ thủ đắc lực" có thể đồng hành trong mọi hành trình chinh phục.

II. Công Nghệ Mới Đột Phá

{{TECH_CARBON_FIBER_PLATE}} - Tấm carbon không còn là độc quyền của giày {{TECH_RACING_SHOES}}: Năm 2025 chứng kiến sự phổ biến của tấm carbon trong cả giày {{TECH_TRAINING_SHOES}}. Công nghệ này giúp tăng hiệu suất đẩy về phía trước lên đến 4%, đồng thời giảm thiểu chấn thương cho cơ bắp.

Foam Revolution - Cuộc cách mạng về chất liệu đệm: Các hãng đã phát triển những loại foam mới với độ đàn hồi vượt trội. {{BRAND_NIKE}} với {{TECH_ZOOM_X}}, {{BRAND_ADIDAS}} với {{TECH_LIGHTSTRIKE_PRO}}, và {{BRAND_NEW_BALANCE}} với {{TECH_FUELCELL}} đều cho thấy sự cải tiến đáng kể về độ bền và khả năng phục hồi.

Sustainable Materials - Vật liệu bền vững: Xu hướng xanh hóa ngành giày thể thao tiếp tục được đẩy mạnh. Hơn 50% giày chạy bộ năm 2025 sử dụng vật liệu tái chế, từ lưới {{TECH_UPPER}} làm từ chai nhựa tái chế đến {{TECH_MIDSOLE}} làm từ ngô và các nguyên liệu sinh học.

Smart Integration - Cảm biến thông minh: Nhiều mẫu giày cao cấp nay được tích hợp cảm biến theo dõi nhịp chân, lực tiếp đất và form chạy. Dữ liệu được đồng bộ hóa với ứng dụng di động, giúp runner phân tích và cải thiện kỹ thuật.

III. Top 5 Mẫu Giày Đáng Chú Ý Nhất 2025

1. {{BRAND_NIKE}} {{PRODUCT_ALPHAFLY_3}} - "Siêu Phẩm Tốc Độ"
   • Đệm {{TECH_ZOOM_X}} cải tiến với độ dày tối ưu
   • Tấm carbon hình cánh cung độc quyền
   • Trọng lượng chỉ 180g cho size US 9
   • Phù hợp: {{TECH_MARATHON}}, tập luyện tốc độ

2. {{BRAND_ADIDAS}} {{PRODUCT_ADIZERO_PRIME_X_2}}
   • Công nghệ {{TECH_LIGHTSTRIKE_PRO}} kép
   • Độ dày {{TECH_MIDSOLE}} 50mm - giới hạn kỹ thuật
   • Thiết kế {{TECH_ENERGY_RODS}} linh hoạt
   • Phù hợp: Runner kinh nghiệm tìm kiếm cảm giác mới lạ

3. {{BRAND_NEW_BALANCE}} {{PRODUCT_FUELCELL_SUPERCOMP_ELITE_V4}}
   • {{TECH_FUELCELL}} foam với công thức mới
   • Hệ thống tấm carbon năng lượng kép
   • {{TECH_UPPER}} {{TECH_ENGINEERED_MESH}} siêu nhẹ
   • Phù hợp: Cân bằng giữa tốc độ và sự ổn định

4. {{BRAND_ASICS}} {{PRODUCT_METASPEED_SKY}}
   • {{TECH_FLYTEFOAM_BLAST_TURBO}} cao cấp
   • Công nghệ {{TECH_GUIDESOLE}} giảm tiêu hao năng lượng
   • Thiết kế riêng cho runner có nhịp bước cao
   • Phù hợp: Runner chuyên nghiệp thi đấu

5. {{BRAND_SAUCONY}} {{PRODUCT_ENDORPHIN_PRO_4}}
   • {{TECH_PWRRUN_HG}} foam đệm siêu nhẹ
   • {{TECH_SPEEDROLL}} technology tạo lực đẩy
   • Formfit {{TECH_UPPER}} ôm chân hoàn hảo
   • Phù hợp: Đa dạng từ beginner đến pro

IV. Tiêu Chí Lựa Chọn Giày Phù Hợp

Để chọn được đôi giày "vương miện" cho riêng mình, runner cần xem xét các yếu tố:

• Loại hình chạy: {{TECH_ROAD_RUNNING}}, {{TECH_TRAIL_RUNNING}} hay {{TECH_TRACK}}?
• Khoảng cách: 5K, 10K, bán marathon hay full marathon?
• Dáng chạy: {{TECH_NEUTRAL}}, {{TECH_OVERPRONATION}} hay {{TECH_UNDERPRONATION}}?
• Trọng lượng cơ thể: Ảnh hưởng đến độ bền của đệm
• Ngân sách: Từ 2-6 triệu đồng tùy phân khúc
• Địa hình: Bê tông, đường đất hay địa hình phức tạp?

V. Kết Luận: Bứt Phá Mọi Giới Hạn

Năm 2025 thực sự là thời điểm vàng cho cộng đồng runner Việt Nam. Với sự đa dạng về công nghệ và mẫu mã, mỗi người chạy đều có thể tìm thấy "chiếc vương miện" phù hợp cho đôi chân của mình. Quan trọng nhất, hãy lắng nghe cơ thể và chọn giày không chỉ dựa trên công nghệ, mà còn dựa trên cảm giác thoải mái khi xỏ vào.

Hãy nhớ: Đôi giày tốt nhất không phải là đôi đắt nhất, mà là đôi phù hợp nhất với bạn. Đến với Myshoes.vn, chúng tôi cam kết mang đến những trải nghiệm mua sắm tốt nhất và tư vấn chuyên nghiệp nhất để bạn tìm được người bạn đồng hành hoàn hảo trên mọi cung đường.`,
        "2": `I. Hành Trình Từ "Thợ Săn Sale" Đến Người Tiêu Dùng Thông Thái

Cách đây 5 năm, tôi từng là một "thợ săn sale" chính hiệu. Mục tiêu của tôi luôn là tìm kiếm những đôi giày có giá rẻ nhất, bất kể đó là hàng chính hãng hay replica. Tôi tự hào về khả năng tìm được những đôi giày "giống 99%" với giá chỉ bằng 1/3, 1/4 so với hàng thật. Nhưng rồi một sự kiện đã thay đổi hoàn toàn quan điểm của tôi.

Đó là vào một ngày mưa, khi tôi đang đi chiếc giày fake mua được với giá 400k, đế giày bất ngờ bong ra khiến tôi trượt ngã và chấn thương mắt cá chân. 2 tuần nằm bất động và chi phí y tế gấp 10 lần số tiền tôi "tiết kiệm" được đã dạy cho tôi một bài học đắt giá.

II. Sự Khác Biệt Không Thể Phủ Nhận

1. Chất Liệu: Từ Những Điều Nhỏ Nhất
   • {{TECH_UPPER}}: Hàng chính hãng sử dụng {{TECH_ENGINEERED_MESH}} cao cấp, có độ co giãn và thông thoáng được tính toán kỹ lưỡng. Hàng fake thường dùng vải thường, dễ rách và gây hầm nóng.
   • Đệm: Công nghệ foam độc quyền như {{TECH_BOOST}}, {{TECH_ZOOM_X}}, {{TECH_REACT}} chỉ có ở hàng thật. Hàng fake sử dụng foam rẻ tiền, nhanh xẹp và không có độ đàn hồi.
   • Keo dán: Hàng thật sử dụng keo công nghiệp chuyên dụng, chịu được nhiệt độ và lực kéo cao. Hàng fake dùng keo thường, dễ bong tróc.

2. Công Nghệ Sản Xuất
   • Quy trình {{TECH_QC}} ({{TECH_QUALITY_CONTROL}}) nghiêm ngặt
   • Máy móc công nghệ cao từ Đức, Nhật
   • Đội ngũ kỹ sư giàu kinh nghiệm
   • Kiểm tra từng công đoạn sản xuất

3. Trải Nghiệm Sử Dụng
   • Độ ôm chân hoàn hảo
   • Phân phối lực đồng đều
   • Độ bền vượt trội (trung bình 800-1000km)
   • Bảo hành chính hãng 2 năm

III. Những Hệ Lụy Khi Sử Dụng Giày Fake

1. Nguy Cơ Sức Khỏe
   • Chấn thương khớp gối, mắt cá chân
   • Đau lưng, đau cột sống
   • Viêm cân gan chân
   • Biến dạng dáng đi

2. Thiệt Hại Kinh Tế
   • Tuổi thọ thấp, phải thay thường xuyên
   • Chi phí y tế khi xảy ra chấn thương
   • Không có giá trị bán lại

3. Vấn Đề Môi Trường
   • Sử dụng hóa chất độc hại
   • Quy trình sản xuất không kiểm soát
   • Nhanh chóng trở thành rác thải

IV. Làm Sao Phân Biệt Hàng Thật - Hàng Fake?

1. Kiểm Tra Bao Bì
   • Hộp cứng cáp, in ấn sắc nét
   • Mã QR, serial number
   • Tem chống hàng giả

2. Quan Sát Chi Tiết
   • Đường may tỉ mỉ, đều đặn
   • Logo in rõ ràng, không nhòe
   • Màu sắc đồng nhất, không lỗi

3. Cảm Nhận Khi Sử Dụng
   • Nhẹ và êm ngay lần đầu đi
   • Không có mùi hóa chất
   • Độ đàn hồi tốt

V. Lời Khuyên Chân Thành

Sau 3 năm chỉ sử dụng giày chính hãng, tôi nhận ra rằng: "Đắt một lần nhưng chất lượng mãi mãi". Mỗi buổi sáng xỏ đôi giày chính hãng vào, tôi cảm nhận được sự tin tưởng và an tâm. Không còn lo lắng về việc đế bong khi đang chạy, không còn sợ chấn thương bất ngờ.

Đặc biệt, với chính sách bảo hành của Myshoes.vn, tôi hoàn toàn yên tâm về chất lượng. Đội ngũ tư vấn chuyên nghiệp giúp tôi chọn được đôi giày phù hợp nhất với nhu cầu và túi tiền.

Hãy đầu tư cho đôi chân của bạn - nơi nâng đỡ toàn bộ cơ thể. Đừng để những khoản tiết kiệm trước mắt khiến bạn phải trả giá đắt về sau.`,
        "3": `I. Xu Hướng Sneaker Cuối Năm 2025: Tiện Lợi & Đa Năng

Cuối năm luôn là thời điểm bận rộn với hàng loạt sự kiện: tiệc tùng, du lịch, mua sắm và các buổi họp mặt. Một đôi sneaker êm ái, linh hoạt trở thành vật bất ly thân của mọi tín đồ thời trang. Năm 2025 chứng kiến sự lên ngôi của những mẫu sneaker "all-in-one" - có thể phối đồ từ casual đến semi-formal, từ văn phòng đến các buổi tiệc cuối năm.

Theo khảo sát mới nhất từ Myshoes.vn, 85% khách hàng tìm kiếm sneaker cuối năm ưu tiên 3 yếu tố: comfort tối đa, dễ phối đồ và giá cả hợp lý. Dưới đây là 5 cái tên nổi bật nhất đáp ứng đầy đủ các tiêu chí này.

II. Top 5 Sneaker Đáng Đồng Tiền Bát Gạo

1. {{BRAND_NIKE}} {{PRODUCT_AIR_FORCE_1}} '07 Premium
   • Ưu điểm: Thiết kế classic không bao giờ lỗi thời
   • Công nghệ: {{TECH_AIR_SOLE}} unit toàn bộ đế
   • Chất liệu: Leather cao cấp, dễ vệ sinh
   • Phối đồ: Quần jeans, jogger, hay cả suit
   • Giá: 2,500,000 VND
   • Đánh giá: 9.5/10 - "Basic nhưng không bao giờ nhàm chán"

2. {{BRAND_ADIDAS}} {{PRODUCT_ULTRABOOST_LIGHT}}
   • Ưu điểm: Êm ái nhất trong phân khúc
   • Công nghệ: {{TECH_BOOST}} foam mới nhẹ hơn 30%
   • Chất liệu: {{TECH_PRIMAKNIT}}+ co giãn 4 chiều
   • Phối đồ: Sporty chic, streetwear
   • Giá: 4,200,000 VND
   • Đánh giá: 9.8/10 - "Như đi trên mây cả ngày"

3. {{BRAND_NEW_BALANCE}} {{PRODUCT_NB_990V6}}
   • Ưu điểm: Support tuyệt vời cho bàn chân
   • Công nghệ: {{TECH_FUELCELL}} {{TECH_MIDSOLE}} kết hợp {{TECH_ENCAP}}
   • Chất liệu: Pigskin suede và mesh cao cấp
   • Phối đồ: Smart casual, business casual
   • Giá: 5,500,000 VND
   • Đánh giá: 9.2/10 - "Đẳng cấp và thoải mái"

4. {{BRAND_VEJA}} {{PRODUCT_CAMPO_LEATHER}}
   • Ưu điểm: Thân thiện môi trường, thiết kế tối giản
   • Công nghệ: Đệm {{TECH_L_FOAM}} từ ngô tái chế
   • Chất liệu: Leather chrome-free
   • Phối đồ: Minimalist, sustainable fashion
   • Giá: 2,800,000 VND
   • Đánh giá: 8.8/10 - "Style có trách nhiệm"

5. {{BRAND_CONVERSE}} {{PRODUCT_CHUCK_70}} Vintage Canvas
   • Ưu điểm: Giá cả phải chăng, đa dạng màu sắc
   • Công nghệ: Đế cao su cổ điển, bền bỉ
   • Chất liệu: Canvas 12oz cao cấp
   • Phối đồ: Streetwear, retro style
   • Giá: 1,500,000 VND
   • Đánh giá: 9.0/10 - "Icon không tuổi"

III. Bí Quyết Chọn Sneaker Theo Nhu Cầu

1. Dân Văn Phòng
   • Ưu tiên: Màu trung tính (trắng, đen, be)
   • Kiểu dáng: Gọn gàng, không quá thể thao
   • Comfort: Quan trọng hàng đầu

2. Giới Trẻ Năng Động
   • Ưu tiên: Màu sắc trẻ trung, thiết kế mới lạ
   • Tính năng: Nhẹ, linh hoạt
   • Ngân sách: Linh hoạt 1-3 triệu

3. Người Trung Niên
   • Ưu tiên: Êm ái, support tốt
   • Thiết kế: Đơn giản, dễ phối đồ
   • Thương hiệu: Uy tín, bền bỉ

IV. Cách Phối Đồ Thông Minh Với Sneaker

1. Smart Casual Cuối Năm
   • Sneaker trắng + Quần chinos + Áo sơ mi
   • Thêm blazer cho các sự kiện quan trọng
   • Phụ kiện: Tất cổ thấp, đồng hồ leather

2. Streetwear Năng Động
   • Sneaker màu + Quần jogger + Hoodie
   • Layer với áo khoác denim hoặc bomber
   • Phụ kiện: Mũ bucket, backpack

3. Tiệc Tùng Festive
   • Sneaker sang trọng + Quần âu + Áo polo
   • Màu sắc: Đỏ, xanh đậm, vàng đồng
   • Phụ kiện: Dây da, ví cầm tay

V. Lời Khuyên Từ Chuyên Gia

"Đừng chạy theo số lượng, hãy đầu tư vào chất lượng" - đó là chia sẻ từ chuyên gia thời trang Nguyễn Minh Anh. Theo anh, mỗi người nên sở hữu 3-4 đôi sneaker chất lượng thay vì 10-15 đôi giá rẻ.

Cuối năm 2025, Myshoes.vn mang đến chương trình khuyến mãi đặc biệt "Year-End Comfort" với ưu đãi lên đến 30% cho các dòng sneaker cao cấp. Đặc biệt, chúng tôi cam kết:
• Bảo hành chính hãng 24 tháng
• Đổi size trong 30 ngày
• Tư vấn style miễn phí

Hãy đến với Myshoes.vn để tìm cho mình người bạn đồng hành hoàn hảo trong những ngày cuối năm bận rộn!`,
        "4": `I. Mùa Đông 2025: Thời Tiết Khắc Nghiệt Và Nhu Cầu Giày Ấm

Theo dự báo từ Trung tâm Khí tượng Thủy văn Trung ương, mùa đông năm 2025 được dự báo sẽ lạnh hơn và kéo dài hơn so với các năm trước. Nhiệt độ tại miền Bắc có thể xuống dưới 10 độ C, trong khi miền Trung cũng chịu ảnh hưởng của các đợt gió mùa Đông Bắc. Đây chính là thời điểm cần chuẩn bị những đôi giày ấm áp để bảo vệ đôi chân - bộ phận nhạy cảm nhất với nhiệt độ thấp.

II. Công Nghệ Giữ Nhiệt Hiện Đại Trong Giày Mùa Đông

1. Công Nghệ Heat Retention
   • Sợi nhiệt Silver Ion: Kháng khuẩn và giữ nhiệt
   • Lớp lót {{TECH_THINSULATE}}™: Giữ ấm gấp 1.5 lần bông thường
   • Màng chống thấm {{TECH_GORE_TEX}}: Ngăn nước, thoát hơi ẩm

2. Vật Liệu Cách Nhiệt
   • Wool Felt: Len ép giữ nhiệt tự nhiên
   • Shearling Lining: Lớp lót lông cừu mềm mại
   • Memory Foam Insole: Đệm nhiệt định hình

3. Thiết Kế Chống Lạnh
   • Cổ giày cao ôm mắt cá
   • Đế chống trượt {{PRODUCT_WINTER_GRIP}}
   • Đường may kín nước

III. Top 5 Giày Ấm Đáng Mua Nhất Mùa Đông 2025

1. {{BRAND_TIMBERLAND}} {{PRODUCT_SIX_INCH_PREMIUM_BOOT}}
   • Nhiệt độ chịu được: -20°C
   • Công nghệ: Waterproof leather, {{TECH_PRIMALOFT}} insulation
   • Giá: 4,500,000 VND
   • Phù hợp: Thành phố, dã ngoại nhẹ

2. {{BRAND_DR_MARTENS}} {{PRODUCT_WINTER_GRIP}}
   • Nhiệt độ chịu được: -15°C
   • Công nghệ: Thermal sole, fur lining
   • Giá: 3,800,000 VND
   • Phù hợp: Street style, đi làm

3. {{BRAND_UGG}} {{PRODUCT_CLASSIC_ULTRA_MINI}}
   • Nhiệt độ chịu được: -10°C
   • Công nghệ: Twinface sheepskin, {{TECH_TREADLITE}} sole
   • Giá: 3,200,000 VND
   • Phù hợp: Casual, đi chơi

4. {{BRAND_SOREL}} {{PRODUCT_CARIBOU_BOOT}}
   • Nhiệt độ chịu được: -40°C
   • Công nghệ: Waterproof nubuck, felt liner
   • Giá: 5,500,000 VND
   • Phù hợp: Tuyết, thời tiết khắc nghiệt

5. {{BRAND_ECCO}} {{PRODUCT_SOFT_7_WINTER}}
   • Nhiệt độ chịu được: -25°C
   • Công nghệ: Yak leather, thermal insole
   • Giá: 3,600,000 VND
   • Phù hợp: Văn phòng, smart casual

IV. Bí Quyết Chọn Giày Ấm Theo Vùng Miền

1. Miền Bắc (Hà Nội & các tỉnh lân cận)
   • Nhiệt độ: 8-15°C, độ ẩm cao
   • Ưu tiên: Chống thấm, giữ nhiệt tốt
   • Kiểu dáng: Boot cổ trung đến cao

2. Miền Trung (Đà Nẵng, Huế)
   • Nhiệt độ: 15-20°C, mưa nhiều
   • Ưu tiên: Thoáng khí, chống thấm
   • Kiểu dáng: Sneaker ấm, boot cổ thấp

3. Miền Nam (TP.HCM & các tỉnh)
   • Nhiệt độ: 20-25°C, se lạnh về đêm
   • Ưu tiên: Thoáng mát, nhẹ nhàng
   • Kiểu dáng: Sneaker mỏng, giày thể thao

V. Chăm Sóc Và Bảo Quản Giày Mùa Đông

1. Vệ Sinh Hàng Ngày
   • Dùng bàn chải mềm làm sạch bùn đất
   • Lau khô tự nhiên, tránh nhiệt cao
   • Sử dụng waterproof spray định kỳ

2. Bảo Quản Khi Không Sử Dụng
   • Nhét giấy báo giữ form giày
   • Để nơi khô ráo, thoáng mát
   • Tránh ánh nắng trực tiếp

3. "Cấp Cứu" Giày Bị Ướt
   • Tháo ngay lót giày ra ngoài
   • Nhét báo khô để hút ẩm
   • Phơi trong bóng râm 2-3 ngày

VI. Chương Trình Khuyến Mãi Đặc Biệt "Winter Ready"

Nhân dịp gió mùa về, Myshoes.vn triển khai chương trình ưu đãi đặc biệt:
• Giảm 25% toàn bộ giày boot mùa đông
• Tặng bộ chăm sóc giày trị giá 500k
• Miễn phí giao hàng toàn quốc
• Bảo hành 2 năm chính hãng

Đừng để cái lạnh làm ảnh hưởng đến sức khỏe và cuộc sống của bạn. Hãy chuẩn bị ngay những đôi giày ấm áp từ hôm nay! Ghé thăm Myshoes.vn hoặc đến trực tiếp các cửa hàng để được tư vấn miễn phí và chọn cho mình người bạn đồng hành hoàn hảo trong mùa đông này.`,
        "5": `I. BST Mới Nhất Với Nhiều Màu Sắc Và Công Nghệ Êm Ái…

Mùa thu 2025 mang đến làn gió mới cho thế giới sneaker với sự kết hợp hoàn hảo giữa công nghệ hiện đại và thiết kế thời trang. Các thương hiệu lớn đã cho ra mắt những bộ sưu tập đặc biệt, tập trung vào tính năng chống thấm nước và thiết kế thông minh phù hợp với thời tiết se lạnh đặc trưng của mùa thu.

II. Tiêu Chí Lựa Chọn Sneaker Mùa Thu

Khi lựa chọn sneaker cho mùa thu, cần cân nhắc các yếu tố:

• Chất liệu: Nên chọn những chất liệu có khả năng chống nước nhẹ như leather, suede được xử lý waterproof
• Màu sắc: Tông màu trầm ấm như nâu, be, xanh rêu, burgundy
• Độ ấm: Có lớp lót mỏng giữ ấm nhưng vẫn thoáng khí
• Đế: Chống trượt tốt cho những ngày mưa ẩm

III. Top Picks Sneaker Mùa Thu 2025

1. {{BRAND_NIKE}} {{PRODUCT_AIR_FORCE_1}} "Autumn Pack"
   • Thiết kế: Màu nâu camel kết hợp gum sole
   • Công nghệ: {{TECH_AIR_MAX}} unit visible, leather {{TECH_UPPER}}
   • Giá: 3,200,000 VND
   • Đặc điểm: Chống nước nhẹ, phối đồ dễ dàng

2. {{BRAND_ADIDAS}} {{PRODUCT_STAN_SMITH}} "Wool Edition"
   • Thiết kế: {{TECH_UPPER}} làm từ wool blend ấm áp
   • Công nghệ: {{TECH_CLOUDFOAM}} comfort insole
   • Giá: 2,800,000 VND
   • Đặc điểm: Nhẹ, ấm, phù hợp tiết trời se lạnh

3. {{BRAND_NEW_BALANCE}} {{PRODUCT_NB_574}} "Weatherproof"
   • Thiết kế: Suede và mesh có xử lý chống nước
   • Công nghệ: {{TECH_ENCAP}} {{TECH_MIDSOLE}}, đế chống trượt
   • Giá: 2,500,000 VND
   • Đặc điểm: Bền bỉ, phù hợp đi làm hàng ngày

4. {{BRAND_CONVERSE}} {{PRODUCT_CHUCK_70}} "Shield Canvas"
   • Thiết kế: Canvas chống nước, màu olive
   • Công nghệ: Đế cao su dày, lót êm
   • Giá: 1,800,000 VND
   • Đặc điểm: Giá cả phải chăng, unisex

5. {{BRAND_PUMA}} {{PRODUCT_RS_X_ECHO}}
   • Thiết kế: Màu xám kết hợp cam burnt
   • Công nghệ: RS cushioning system
   • Giá: 2,900,000 VND
   • Đặc điểm: Êm ái, thiết kế futuristict

IV. Cách Phối Đồ Với Sneaker Mùa Thu

• Casual Style: Sneaker + Quần jeans + Áo hoodie + Áo khoác denim
• Smart Casual: Sneaker + Quần chinos + Áo sơ mi + Blazer
• Street Style: Sneaker + Quần jogger + Áo graphic tee + Bomber jacket

V. Bảo Quản Sneaker Mùa Thu

• Sử dụng waterproof spray trước khi dùng
• Vệ sinh bằng khăn ẩm sau khi đi ngoài trời
• Tránh phơi trực tiếp dưới nắng gắt
• Sử dụng shoe tree để giữ form

Myshoes.vn hiện đang có chương trình ưu đãi đặc biệt cho các mẫu sneaker mùa thu với mức giảm lên đến 30%. Đến ngay cửa hàng gần nhất hoặc đặt hàng online để sở hữu những đôi sneaker đẹp nhất mùa này!`,
      },
    },
    Testimonials: {
      title: "Đánh giá",
    },
    Newsletter: {
      title: "Nhận ưu đãi",
      subtitle: "Đăng ký để nhận mã giảm giá 100K",
      emailPlaceholder: "Email của bạn",
      subscribeButton: "Đăng ký",
      emailRequired: "Vui lòng nhập email!",
      emailInvalid: "Email không hợp lệ!",
      success: "🎉 Đăng ký thành công! Mã giảm giá 100K đã được gửi đến {email}",
    },
    Footer: {
      companyDescription: "Cửa hàng giày thể thao chính hãng với đa dạng thương hiệu nổi tiếng thế giới.",
      quickLinks: "Liên kết nhanh",
      home: "Trang chủ",
      products: "Sản phẩm",
      about: "Về chúng tôi",
      contact: "Liên hệ",
      customerService: "Hỗ trợ khách hàng",
      returnPolicy: "Chính sách đổi trả",
      purchaseGuide: "Hướng dẫn mua hàng",
      warranty: "Bảo hành sản phẩm",
      faq: "FAQ",
      contactInfo: "Thông tin liên hệ",
      address: "123 Đường ABC, Quận 1, TP.HCM",
      phone: "(028) 1234 5678",
      email: "info{'@'}shoezshop.com",
      hours: "8:00 - 22:00 (Thứ 2 - Chủ nhật)",
      copyright: "© {year} Shoez Shop. All rights reserved.",
    },
    VideoHero: {
      badge: "Bộ sưu tập mới",
      defaultTitle: "GIÀY THỂ THAO",
      defaultDescription: "Chọn giày phù hợp với phong cách của bạn",
      defaultCta: "Khám phá ngay",
      hover3D: "✨ Di chuột để xoay giày 3D",
    },
    ShoeCustomizer: {
      title: "Thiết kế giày của riêng bạn",
      subtitle: "Tùy chỉnh màu sắc, chất liệu và tạo đôi giày độc nhất cho phong cách cá nhân",
      selectModel: "Chọn kiểu giày",
      customizeColors: "Tùy chỉnh màu sắc",
      material: "Chất liệu",
      saveDesign: "💾 Lưu thiết kế",
      useDesign: "SỬ DỤNG",
      viewMore: "Xem thêm thiết kế ↓",
      communityDesigns: "Thiết kế nổi bật từ cộng đồng",
      saveSuccess: "🎉 Thiết kế đã được lưu! Bạn có thể xem trong mục \"Thiết kế của tôi\"",
      parts: {
        upper: "Thân giày",
        sole: "Đế giày",
        laces: "Dây giày",
        logo: "Logo",
      },
      materials: {
        suede: "Da lộn",
        leather: "Da thật",
        canvas: "Vải canvas",
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
      subtitle: "Tổng quan về hệ thống",
      revenue: "Doanh thu",
      orders: "Đơn hàng",
      products: "Sản phẩm",
      customers: "Khách hàng",
      active: "Đang hoạt động",
      last7DaysRevenue: "Doanh thu 7 ngày qua",
      noData: "Chưa có dữ liệu",
      topProducts: "Sản phẩm bán chạy",
      recentOrders: "Đơn hàng gần đây",
      orderId: "Mã đơn",
      customer: "Khách hàng",
      date: "Ngày",
      total: "Tổng tiền",
      status: "Trạng thái",
      actions: "Hành động",
      view: "Xem",
      retry: "Thử lại",
      revenueChangeSuffix: "% từ tháng trước",
      registeredUsers: "Người dùng đã đăng ký",
      totalRevenueLabel: "Tổng doanh thu:",
      soldSuffix: "đã bán",
    },
    Status: {
      pending: "Chờ xử lý",
      processing: "Đang xử lý",
      confirmed: "Đã xác nhận",
      shipping: "Đang giao",
      complete: "Hoàn thành",
      completed: "Hoàn thành",
      delivered: "Đã giao",
      cancelled: "Đã hủy",
      canceled: "Đã hủy",
    },
    Nav: {
      dashboard: "Dashboard",
      products: "Sản phẩm",
      orders: "Đơn hàng",
      customers: "Khách hàng",
      categories: "Danh mục",
      brands: "Thương hiệu",
      analytics: "Thống kê",
      settings: "Cài đặt",
      title: "Shoez Admin",
      panel: "Management Panel",
      logoutConfirm: "Bạn có chắc chắn muốn đăng xuất?",
      logout: "Đăng xuất"
    },
    Header: {
      searchPlaceholder: "Tìm kiếm...",
      notifications: "Thông báo",
      clearAll: "Xóa tất cả",
      noNotifications: "Không có thông báo",
      timeAgo: {
        justNow: "Vừa xong",
        minutesAgo: "{count} phút trước",
        hoursAgo: "{count} giờ trước",
        daysAgo: "{count} ngày trước",
      },
      error: {
        markRespondedFailed: "Không thể đánh dấu thông báo là đã phản hồi. Vui lòng thử lại."
      }
    },
    Categories: {
      title: "Danh mục",
      subtitle: "Quản lý danh mục sản phẩm của cửa hàng",
      searchPlaceholder: "Tìm theo tên danh mục...",
      add: "Thêm danh mục",
      total: "Tổng danh mục",
      active: "Đang hoạt động",
      inactive: "Đã vô hiệu hóa",
      statusActive: "Hoạt động",
      statusInactive: "Vô hiệu hóa",
      productsCount: "sản phẩm",
      edit: "Sửa",
      delete: "Xoá",
      toggleDeactivate: "Vô hiệu hóa",
      toggleActivate: "Kích hoạt",
      emptyTitle: "Chưa có danh mục nào",
      emptySubtitle: "Thêm danh mục đầu tiên để bắt đầu",
      modalEditTitle: "Sửa danh mục",
      modalAddTitle: "Thêm danh mục mới",
      nameLabel: "Tên danh mục *",
      namePlaceholder: "Nhập tên danh mục",
      descLabel: "Mô tả",
      descPlaceholder: "Nhập mô tả danh mục",
      activeLabel: "Kích hoạt danh mục",
      cancel: "Huỷ",
      update: "Cập nhật",
      create: "Thêm mới",
      confirmTitle: "Xác nhận",
      confirmDeleteMessage: "Bạn có chắc muốn xoá danh mục này?",
      actionFailed: "Thao tác thất bại",
      loadFailed: "Không thể tải danh sách danh mục",
      createSuccess: "Thêm danh mục thành công!",
      updateSuccess: "Cập nhật danh mục thành công!",
      deleteSuccess: "Đã xoá danh mục thành công!",
      toggleSuccessDeactivate: "Đã vô hiệu hóa danh mục!",
      toggleSuccessActivate: "Đã kích hoạt danh mục!"
    },
    Brands: {
      title: "Thương hiệu",
      subtitle: "Quản lý thương hiệu sản phẩm của cửa hàng",
      searchPlaceholder: "Tìm theo tên thương hiệu...",
      add: "Thêm thương hiệu",
      total: "Tổng thương hiệu",
      active: "Đang hoạt động",
      inactive: "Đã vô hiệu hóa",
      statusActive: "Hoạt động",
      statusInactive: "Vô hiệu hóa",
      edit: "Sửa",
      delete: "Xoá",
      toggleDeactivate: "Vô hiệu hóa",
      toggleActivate: "Kích hoạt",
      emptyTitle: "Chưa có thương hiệu nào",
      emptySubtitle: "Thêm thương hiệu đầu tiên để bắt đầu",
      modalEditTitle: "Sửa thương hiệu",
      modalAddTitle: "Thêm thương hiệu mới",
      nameLabel: "Tên thương hiệu",
      namePlaceholder: "Nhập tên thương hiệu",
      nameRequired: "Tên thương hiệu là bắt buộc",
      logoLabel: "Logo",
      logoUploadLabel: "Upload ảnh (tùy chọn)",
      logoSelectFile: "Chọn file ảnh",
      logoOr: "HOẶC",
      logoUrlLabel: "Nhập URL logo",
      logoUrlPlaceholder: "https://example.com/logo.png",
      logoRemove: "Xóa ảnh",
      descLabel: "Mô tả",
      descPlaceholder: "Nhập mô tả thương hiệu (tùy chọn)",
      activeLabel: "Kích hoạt thương hiệu",
      cancel: "Huỷ",
      update: "Cập nhật",
      create: "Thêm mới",
      confirmTitle: "Xác nhận",
      confirmDeleteMessage: "Bạn có chắc muốn xoá thương hiệu này?",
      actionFailed: "Thao tác thất bại",
      loadFailed: "Không thể tải danh sách thương hiệu",
      createSuccess: "Thêm thương hiệu thành công!",
      updateSuccess: "Cập nhật thương hiệu thành công!",
      deleteSuccess: "Đã xoá thương hiệu thành công!",
      toggleSuccessDeactivate: "Đã vô hiệu hóa thương hiệu!",
      toggleSuccessActivate: "Đã kích hoạt thương hiệu!",
      fileMustBeImage: "File phải là hình ảnh",
      fileSizeExceeded: "Kích thước file không được vượt quá 5MB",
      noResponseFromServer: "Không nhận được phản hồi từ server"
    },
    Products: {
      title: "Quản lý sản phẩm",
      subtitle: "Danh sách tất cả sản phẩm",
      addNew: "Thêm sản phẩm mới",
      filters: {
        searchLabel: "Tìm kiếm",
        searchPlaceholder: "Tên sản phẩm...",
        category: "Danh mục",
        brand: "Thương hiệu",
        all: "Tất cả",
        status: "Trạng thái",
        statusActive: "Đang bán",
        statusInactive: "Ngừng bán",
        statusOOS: "Hết hàng",
        sort: "Sắp xếp",
        sortCreated: "Ngày tạo",
        sortName: "Tên sản phẩm",
        sortPrice: "Giá",
        sortStock: "Số lượng",
        orderLabel: "Thứ tự:",
        newest: "Mới nhất",
        oldest: "Cũ nhất",
        ratingFrom: "Đánh giá từ:",
        ratingTo: "Đến:",
        clearRating: "Xóa filter đánh giá",
        quick: "Nhanh:",
      },
      table: {
        product: "Sản phẩm",
        category: "Danh mục",
        price: "Giá",
        discount: "Giảm giá",
        stock: "Tồn kho",
        rating: "Đánh giá",
        status: "Trạng thái",
        createdAt: "Ngày tạo",
        actions: "Hành động",
        imageFallback: "Ảnh",
        noDiscount: "Không",
        itemsSuffix: "sản phẩm",
        reviewsSuffix: "đánh giá",
        viewDetail: "Xem chi tiết",
        edit: "Chỉnh sửa",
        delete: "Xóa",
      },
      pagination: {
        showing: "Hiển thị",
        ofTotal: "trong tổng số",
        products: "sản phẩm",
        perPage: "Hiển thị:",
        prev: "Trước",
        next: "Sau",
      },
      confirm: {
        deleteTitle: "Bạn có chắc chắn muốn xóa sản phẩm này?",
        deleteNamed: "Bạn có chắc chắn muốn xóa sản phẩm \"{name}\"? Hành động này không thể hoàn tác.",
        success: "Xóa sản phẩm thành công!",
        error: "Có lỗi xảy ra khi xóa sản phẩm",
      },
      rating: {
        notRated: "Chưa đánh giá",
      }
    },
    AddProduct: {
      title: "Thêm sản phẩm mới",
      form: {
        nameLabel: "Tên sản phẩm *",
        namePlaceholder: "Nhập tên sản phẩm",
        brandLabel: "Thương hiệu",
        brandPlaceholder: "Nike, Adidas, ...",
        categoryLabel: "Danh mục",
        categoryPlaceholder: "Giày thể thao, dép, ...",
        sizesLabel: "Size giày (cách nhau bởi dấu phẩy)",
        sizesPlaceholder: "39, 40, 41, ...",
        descriptionPlaceholder: "Nhập mô tả chi tiết",
        priceLabel: "Giá (VNĐ) *",
        stockLabel: "Số lượng",
        imagesLabel: "Ảnh sản phẩm",
        colorsLabel: "Màu sắc (cách nhau bởi dấu phẩy)",
        colorsPlaceholder: "Đỏ, xanh, trắng, ...",
        submitButton: "Thêm sản phẩm",
      },
      messages: {
        success: "✅ Thêm sản phẩm thành công!",
        error: "❌ Có lỗi xảy ra khi thêm sản phẩm!",
      }
    },
    Orders: {
      title: "Quản lý đơn hàng",
      subtitle: "Danh sách tất cả đơn hàng",
      stats: {
        pending: "Chờ xử lý",
        confirmed: "Đã xác nhận",
        shipping: "Đang giao",
        complete: "Hoàn thành",
        cancelled: "Đã hủy",
      },
      filters: {
        activeFilters: "Bộ lọc đang áp dụng:",
        customer: "Khách hàng",
        status: "Trạng thái",
        dateRange: "Khoảng ngày",
        searchPlaceholder: "Tên, email, SĐT, mã đơn...",
        searchLabel: "Tìm kiếm",
        statusLabel: "Trạng thái",
        fromDate: "Từ ngày",
        toDate: "Đến ngày",
        apply: "Lọc",
        clear: "Xóa",
        exportCsv: "Xuất CSV",
        all: "Tất cả",
        pending: "Chờ xác nhận",
        confirmed: "Đã xác nhận",
        shipping: "Đang giao",
        delivered: "Đã nhận",
        complete: "Hoàn thành",
        cancelled: "Đã hủy",
      },
      empty: {
        title: "Không tìm thấy đơn hàng",
        subtitle: "Không có đơn hàng nào phù hợp với tiêu chí lọc của bạn.",
      },
      table: {
        orderId: "Mã đơn",
        customer: "Khách hàng",
        phone: "Số điện thoại",
        date: "Ngày đặt",
        products: "Sản phẩm",
        status: "Trạng thái",
        actions: "Hành động",
        itemsSuffix: "sản phẩm",
        view: "Xem chi tiết",
        confirm: "Xác nhận đơn hàng",
        ship: "Bắt đầu giao hàng",
        complete: "Hoàn thành đơn hàng",
        cancel: "Hủy đơn",
        print: "In đơn hàng",
      },
      pagination: {
        showing: "Hiển thị",
        to: "đến",
        of: "trong",
        orders: "đơn hàng",
        prev: "Trước",
        next: "Sau",
      },
      export: {
        success: "Xuất đơn hàng thành công!",
        error: "Có lỗi xảy ra khi xuất đơn hàng",
      },
      statusMap: {
        pending: "Chờ xác nhận",
        confirmed: "Đã xác nhận",
        shipping: "Đang giao",
        complete: "Hoàn thành",
        cancelled: "Đã hủy",
      }
    },
    Customers: {
      title: "Khách hàng",
      subtitle: "Quản lý tài khoản người dùng của cửa hàng",
      searchPlaceholder: "Tìm theo tên hoặc email...",
      actions: {
        deleteSelected: "Xoá đã chọn",
        lockSelected: "Khoá đã chọn",
        unlockSelected: "Mở khoá đã chọn",
        perPage: "Hiển thị",
      },
      table: {
        fullName: "Họ tên",
        email: "Email",
        status: "Trạng thái",
        role: "Vai trò",
        createdAt: "Ngày tạo",
        actions: "Thao tác",
        loading: "Đang tải dữ liệu...",
        noData: "Không có dữ liệu phù hợp",
        locked: "Đã khoá",
        active: "Hoạt động",
        undo: "Hoàn tác",
        delete: "Xoá",
        lock: "Khoá",
        unlock: "Mở khoá",
      },
      pagination: {
        page: "Trang",
        prev: "Trước",
        next: "Sau",
      },
      confirm: {
        cancel: "Huỷ",
        confirm: "Xác nhận",
        deleteUser: "Bạn có chắc muốn xoá người dùng này?",
        deleteUsers: "Xoá {count} người dùng đã chọn?",
        lockAccount: "Khoá tài khoản này?",
        unlockAccount: "Mở khoá tài khoản này?",
        lockAccounts: "Khoá {count} tài khoản?",
        unlockAccounts: "Mở khoá {count} tài khoản?",
      },
      messages: {
        deleteSuccess: "Đã xoá người dùng thành công!",
        deleteUsersSuccess: "Đã xoá {count} người dùng thành công!",
        deleteFailed: "Xoá người dùng thất bại",
        lockSuccess: "Đã khoá tài khoản thành công!",
        unlockSuccess: "Đã mở khoá tài khoản thành công!",
        lockUsersSuccess: "Đã khoá {count} tài khoản thành công!",
        unlockUsersSuccess: "Đã mở khoá {count} tài khoản thành công!",
        lockFailed: "Khoá/Mở khoá thất bại",
        actionFailed: "Thao tác thất bại",
      }
    },
    Analytics: {
      title: "Thống kê & Phân tích",
      subtitle: "Tổng quan về hệ thống và hiệu suất kinh doanh",
      retry: "Thử lại",
      cards: {
        totalRevenue: "Tổng doanh thu",
        revenueChangeSuffix: "% so với tháng trước",
        totalOrders: "Tổng đơn hàng",
        totalProducts: "Tổng sản phẩm",
        active: "Đang hoạt động",
        totalCustomers: "Tổng khách hàng",
        registeredUsers: "Người dùng đã đăng ký",
      },
      chart: {
        revenueTitle: "Doanh thu {days} ngày qua",
        option7: "7 ngày",
        option14: "14 ngày",
        option30: "30 ngày",
        totalRevenue: "Tổng doanh thu:",
      },
      topProducts: {
        title: "Sản phẩm bán chạy",
        noData: "Chưa có dữ liệu",
        soldSuffix: "đã bán",
      },
      statusDistribution: {
        title: "Phân bổ đơn hàng theo trạng thái",
      },
      recentOrders: {
        title: "Đơn hàng gần đây",
        empty: "Chưa có đơn hàng",
      },
      table: {
        orderId: "Mã đơn",
        customer: "Khách hàng",
        date: "Ngày",
        value: "Giá trị",
      },
      detailedRevenue: {
        title: "Doanh thu chi tiết",
        today: "Hôm nay",
        thisWeek: "Tuần này",
        thisMonth: "Tháng này",
        thisYear: "Năm này",
        ordersSuffix: "đơn",
      },
      detailedOrders: {
        title: "Đơn hàng theo thời gian",
        today: "Hôm nay",
        thisWeek: "Tuần này",
        thisMonth: "Tháng này",
        total: "Tổng cộng",
        byStatus: "Phân bổ theo trạng thái:",
      },
      cancellations: {
        title: "Thống kê hủy hàng",
        totalCancelled: "Tổng đơn hủy",
        cancellationRate: "Tỷ lệ hủy",
        lostRevenue: "Doanh thu mất",
        today: "Hôm nay",
        thisWeek: "Tuần này",
        thisMonth: "Tháng này",
      },
      recentCancelled: {
        title: "Đơn hàng hủy gần đây",
      },
      entities: {
        users: "Người dùng",
        categories: "Danh mục",
        brands: "Thương hiệu",
        products: "Sản phẩm",
        total: "Tổng số:",
        active: "Đang hoạt động:",
        inactive: "Ngừng hoạt động:",
        newThisMonth: "Mới trong tháng:",
        newThisWeek: "Mới trong tuần:",
        admins: "Quản trị viên:",
        lowStock: "Tồn kho thấp:",
        outOfStock: "Hết hàng:",
        productsUnit: "sản phẩm",
      },
      errors: {
        loadFailed: "Không thể tải dữ liệu thống kê",
      }
    },
  },
  Orders: {
    Header: {
      title: "Đơn hàng của tôi",
      totalOrders: "Tổng số:",
      ordersSuffix: "đơn hàng",
      filters: {
        all: "Tất cả",
        pending: "Chờ xác nhận",
        confirmed: "Đã xác nhận",
        shipping: "Đang giao",
        complete: "Hoàn thành",
        cancelled: "Đã hủy",
      },
    },
    Empty: {
      titles: {
        all: "Chưa có đơn hàng nào",
        pending: "Không có đơn hàng chờ xác nhận",
        confirmed: "Không có đơn hàng đã xác nhận",
        shipping: "Không có đơn hàng đang giao",
        complete: "Không có đơn hàng hoàn thành",
        cancelled: "Không có đơn hàng đã hủy",
      },
      descriptions: {
        all: "Hãy bắt đầu mua sắm và đơn hàng đầu tiên của bạn sẽ xuất hiện ở đây.",
        pending: "Tất cả đơn hàng của bạn đã được xử lý hoặc chưa có đơn hàng nào ở trạng thái này.",
        confirmed: "Không có đơn hàng nào đã được xác nhận.",
        shipping: "Không có đơn hàng nào đang được giao.",
        complete: "Bạn chưa có đơn hàng nào đã hoàn thành.",
        cancelled: "Bạn chưa hủy đơn hàng nào.",
      },
      shopNow: "Mua sắm ngay",
      viewAllOrders: "Xem tất cả đơn hàng",
    },
    StatusBadge: {
      pending: "chờ xác nhận",
      confirmed: "đã xác nhận",
      shipping: "đang giao hàng",
      complete: "hoàn thành",
      cancelled: "đã hủy",
    },
    Card: {
      orderDate: "Đặt ngày:",
      shippingAddress: "Địa chỉ giao hàng:",
      trackingNumber: "Mã theo dõi:",
      size: "Size:",
      color: "Màu:",
      quantity: "Số lượng:",
      viewDetail: "Xem chi tiết",
      cancelOrder: "Hủy đơn hàng",
      reorder: "Mua lại",
      paymentMethods: {
        creditCard: "Thẻ tín dụng",
        cod: "Thanh toán khi nhận hàng",
        bankTransfer: "Chuyển khoản ngân hàng",
        momo: "Ví MoMo",
      },
    },
    ReviewRequest: {
      title: "Đánh giá đơn hàng",
      subtitle: "Bạn đã nhận được hàng?",
      message: "Chia sẻ trải nghiệm của bạn để giúp người khác lựa chọn tốt hơn",
      later: "Để sau",
      reviewNow: "Đánh giá ngay",
    },
    Layout: {
      cancelOrderWarning: "Không thể hủy đơn hàng này. Đơn hàng đã được xác nhận bởi admin. Vui lòng liên hệ admin để hủy.",
      cancelOrderConfirm: "Bạn có chắc chắn muốn hủy đơn hàng này?",
      cancelSuccess: "Đơn hàng đã được hủy thành công!",
      cancelError: "Không thể hủy đơn hàng",
      reorderSuccess: "Sản phẩm đã được thêm vào giỏ hàng!",
    },
    Pagination: {
      previousPage: "Trang trước",
      nextPage: "Trang sau",
      goToPage: "Đi đến trang {page}",
    },
    Loading: {
      text: "Đang tải đơn hàng...",
    },
  },
  Notifications: {
    Bell: {
      title: "Thông báo",
      markAllAsRead: "Đánh dấu đã đọc",
      noNotifications: "Không có thông báo",
      viewAll: "Xem tất cả",
      timeAgo: {
        justNow: "Vừa xong",
        minutesAgo: "{count} phút trước",
        hoursAgo: "{count} giờ trước",
        daysAgo: "{count} ngày trước",
      },
    },
    Toast: {
      defaultTitle: "Thông báo",
      orderCode: "Mã đơn:",
    },
  },
  common: {
    and: "và",
  },
  Auth: {
    SocialLogin: {
      orLoginWith: "Hoặc đăng nhập với",
      loginWithGoogle: "Đăng nhập với Google",
      loginWithFacebook: "Đăng nhập với Facebook",
      agreeToTerms: "Khi đăng nhập, bạn đồng ý với",
      termsOfService: "Điều khoản sử dụng",
      privacyPolicy: "Chính sách bảo mật",
    },
  },
  Cart: {
    Header: {
      title: "Giỏ hàng",
      continueShopping: "Tiếp tục mua sắm",
      itemsCount: "sản phẩm",
    },
    Item: {
      size: "Size:",
      color: "Màu:",
    },
    Summary: {
      title: "Tóm tắt đơn hàng",
      subtotal: "Tạm tính",
      shippingFee: "Phí vận chuyển",
      shippingFree: "Miễn phí",
      discount: "Giảm giá",
      total: "Tổng cộng",
      checkout: "Thanh toán",
      continueShopping: "← Tiếp tục mua sắm",
      itemsSuffix: "sản phẩm",
    },
    Empty: {
      title: "Giỏ hàng trống",
      description: "Hãy thêm một vài sản phẩm vào giỏ hàng để bắt đầu mua sắm",
      shopNow: "Mua sắm ngay",
    },
  },
  Contact: {
    zalo: "Liên hệ qua Zalo",
    tiktok: "Theo dõi TikTok",
  },
  Header: {
    home: "Trang chủ",
    products: "Sản phẩm",
    about: "Về chúng tôi",
    news: "Tin tức",
    contact: "Liên hệ",
    navigation: {
      home: "Trang chủ",
      products: "Sản phẩm",
      about: "Về chúng tôi",
      contact: "Liên hệ",
      favourite: "Yêu thích",
      login: "Đăng nhập",
      register: "Đăng ký",
      profile: "Hồ sơ",
      logout: "Đăng xuất",
      greeting: "Xin chào, {name}",
    },
    search: {
      placeholder: "Tìm kiếm...",
    },
  },
  Product: {
    Breadcrumb: {
      home: "Trang chủ",
      products: "Sản phẩm",
    },
    Info: {
      reviews: "đánh giá",
      save: "Tiết kiệm",
      color: "Màu sắc:",
      size: "Size:",
      selectSize: "Chọn size",
      quantity: "Số lượng",
      available: "sản phẩm có sẵn",
      addToCart: "Thêm vào giỏ hàng",
      buyNow: "Mua ngay",
      addToFavourite: "Thêm vào yêu thích",
      removeFromFavourite: "Xóa khỏi yêu thích",
    },
    Gallery: {
      thumbnail: "Hình thu nhỏ",
    },
  },
  Products: {
    Card: {
      favourite: "Yêu thích",
      liked: "Đã thích",
      buyNow: "Mua ngay",
    },
    Filters: {
      title: "Bộ lọc",
      search: "Tìm kiếm",
      searchPlaceholder: "Tên sản phẩm...",
      brand: "Thương hiệu",
      category: "Loại giày",
      color: "Màu sắc",
      size: "Size",
      price: "Giá",
      priceFrom: "Từ",
      priceTo: "Đến",
      apply: "Áp dụng",
      reset: "Xóa bộ lọc",
    },
    Sort: {
      sortBy: "Sắp xếp:",
      default: "Mặc định",
      priceAsc: "Giá: Thấp đến cao",
      priceDesc: "Giá: Cao đến thấp",
      nameAsc: "Tên: A-Z",
      nameDesc: "Tên: Z-A",
      viewGrid: "Xem dạng lưới",
      viewList: "Xem dạng danh sách",
    },
  },
  Profile: {
    myAccount: "Tài khoản của tôi",
    profile: "Hồ sơ cá nhân",
    myOrders: "Đơn hàng của tôi",
    Header: {
      title: "Hồ sơ của tôi",
      subtitle: "Quản lý thông tin hồ sơ để bảo mật tài khoản",
      memberSince: "Thành viên từ",
    },
    Info: {
      title: "Thông tin cá nhân",
      fullName: "Họ và tên",
      fullNamePlaceholder: "Nhập họ và tên",
      email: "Email",
      emailPlaceholder: "Nhập email",
      phone: "Số điện thoại",
      phonePlaceholder: "Nhập số điện thoại",
      birthday: "Ngày sinh",
      gender: "Giới tính",
      genderMale: "Nam",
      genderFemale: "Nữ",
      genderOther: "Khác",
      address: "Địa chỉ",
      addressPlaceholder: "Nhập địa chỉ",
      cancel: "Hủy",
      saving: "Đang lưu...",
      saveChanges: "Lưu thay đổi",
    },
    Avatar: {
      changePhoto: "Đổi ảnh",
      note: "Lưu ý:",
      noteText: "Ảnh đại diện nên có định dạng JPG, PNG hoặc GIF. Kích thước tối đa 5MB.",
      invalidFormat: "Chỉ chấp nhận file ảnh (JPG, PNG, GIF)",
      fileSizeExceeded: "Kích thước file không được vượt quá 5MB",
    },
    Password: {
      title: "Đổi mật khẩu",
      currentPassword: "Mật khẩu hiện tại",
      currentPasswordPlaceholder: "Nhập mật khẩu hiện tại",
      newPassword: "Mật khẩu mới",
      newPasswordPlaceholder: "Nhập mật khẩu mới",
      confirmPassword: "Xác nhận mật khẩu mới",
      confirmPasswordPlaceholder: "Nhập lại mật khẩu mới",
      passwordHint: "Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường và số",
      strength: "Độ mạnh mật khẩu:",
      strengthWeak: "Yếu",
      strengthMedium: "Trung bình",
      strengthStrong: "Mạnh",
      strengthVeryStrong: "Rất mạnh",
      securityTips: "Mẹo bảo mật:",
      tip1: "Sử dụng mật khẩu dài ít nhất 8 ký tự",
      tip2: "Kết hợp chữ hoa, chữ thường, số và ký tự đặc biệt",
      tip3: "Không sử dụng thông tin cá nhân làm mật khẩu",
      tip4: "Đổi mật khẩu định kỳ 3-6 tháng một lần",
      cancel: "Hủy",
      changing: "Đang đổi mật khẩu...",
      changePassword: "Đổi mật khẩu",
      errors: {
        currentPasswordRequired: "Vui lòng nhập mật khẩu hiện tại",
        newPasswordRequired: "Vui lòng nhập mật khẩu mới",
        newPasswordMinLength: "Mật khẩu phải có ít nhất 8 ký tự",
        newPasswordSameAsCurrent: "Mật khẩu mới không được trùng với mật khẩu hiện tại",
        confirmPasswordRequired: "Vui lòng xác nhận mật khẩu mới",
        confirmPasswordMismatch: "Mật khẩu xác nhận không khớp",
      },
    },
  },
  Reviews: {
    Modal: {
      title: "Đánh giá sản phẩm",
      size: "Size:",
      color: "Màu:",
      yourRating: "Đánh giá của bạn *",
      selectStars: "Vui lòng chọn số sao",
      yourComment: "Nhận xét của bạn *",
      commentPlaceholder: "Chia sẻ trải nghiệm của bạn về sản phẩm...",
      minChars: "Tối thiểu 10 ký tự",
      needMoreChars: "Cần ít nhất {count} ký tự nữa",
      addMedia: "Thêm hình ảnh hoặc video (tùy chọn)",
      selectMedia: "Chọn ảnh/video",
      maxFiles: "Tối đa 5 tệp (ảnh/video)",
      video: "Video",
      cancel: "Hủy",
      submit: "Gửi đánh giá",
      uploadError: "Không thể upload ảnh/video. Vui lòng thử lại.",
      success: "Cảm ơn bạn đã đánh giá!",
      submitError: "Có lỗi xảy ra khi gửi đánh giá",
    },
    List: {
      title: "Đánh giá từ khách hàng",
      noReviews: "Chưa có đánh giá nào",
      customer: "Khách hàng",
      helpful: "Hữu ích",
      adminResponse: "Phản hồi từ Admin",
      admin: "Admin",
      loadMore: "Xem thêm đánh giá",
    },
    PromptBanner: {
      title: "Bạn có {count} sản phẩm chưa đánh giá!",
      description: "Hãy chia sẻ trải nghiệm của bạn để giúp người khác lựa chọn đúng sản phẩm",
      later: "Để sau",
      reviewNow: "Đánh giá ngay",
    },
  },
  Shared: {
    ProductCategory: {
      color: "Màu:",
      size: "Size:",
      liked: "Đã thích",
      favourite: "Yêu thích",
      buyNow: "Mua ngay",
      login: "Đăng nhập",
      close: "Đóng",
      addedToCart: "Đã thêm \"{productName}\" vào giỏ hàng!",
      loginRequiredFavourite: "Bạn chưa đăng nhập. Vui lòng đăng nhập để thêm sản phẩm vào yêu thích!",
      loginRequiredBuy: "Bạn chưa đăng nhập. Vui lòng đăng nhập để mua sản phẩm!",
    },
    NotificationBell: {
      title: "Thông báo",
      markAllRead: "Đánh dấu đã đọc tất cả",
      noNotifications: "Không có thông báo",
      viewAll: "Xem tất cả thông báo",
      justNow: "Vừa xong",
      minutesAgo: "{count} phút trước",
      hoursAgo: "{count} giờ trước",
      daysAgo: "{count} ngày trước",
      mockOrderTitle: "Đơn hàng đã được xác nhận",
      mockOrderMessage: "Đơn hàng #12345 của bạn đã được xác nhận và đang được chuẩn bị.",
      mockPromotionTitle: "Khuyến mãi đặc biệt",
      mockPromotionMessage: "Giảm 20% cho tất cả giày Nike. Áp dụng đến hết ngày 31/12.",
      mockSystemTitle: "Cập nhật hệ thống",
      mockSystemMessage: "Hệ thống sẽ bảo trì từ 2:00 đến 4:00 ngày mai.",
    },
    GlobalLoading: {
      loading: "Đang tải...",
    },
    StarRating: {
      rating: "Đánh giá {rating} trên 5 sao",
      outOf: "trên 5 sao",
    },
    ToastManager: {
      close: "Đóng",
      success: "Thành công",
      error: "Lỗi",
      info: "Thông tin",
      warning: "Cảnh báo",
    },
    ConfirmModal: {
      title: "Xác nhận",
      defaultMessage: "Bạn có chắc chắn muốn thực hiện hành động này?",
      confirm: "Xác nhận",
      cancel: "Hủy",
    },
    LanguageSwitcher: {
      label: "Ngôn ngữ",
      vietnamese: "Tiếng Việt",
      english: "English",
      japanese: "日本語",
    },
    Layout: {
      header: {
        home: "Trang chủ",
        products: "Sản phẩm",
        about: "Về chúng tôi",
        contact: "Liên hệ",
        login: "Đăng nhập",
        register: "Đăng ký",
        greeting: "Xin chào",
        profile: "Hồ sơ",
        logout: "Đăng xuất",
      },
      footer: {
        companyDescription: "Cửa hàng giày thể thao chính hãng với đa dạng thương hiệu nổi tiếng thế giới.",
        quickLinks: "Liên kết nhanh",
        customerService: "Hỗ trợ khách hàng",
        returnPolicy: "Chính sách đổi trả",
        purchaseGuide: "Hướng dẫn mua hàng",
        warranty: "Bảo hành sản phẩm",
        contactInfo: "Thông tin liên hệ",
        workingHours: "8:00 - 22:00 (Thứ 2 - Chủ nhật)",
        copyright: "© 2025 Shoez Shop. Tất cả quyền được bảo lưu.",
      },
    },
    ToastNotification: {
      close: "Đóng",
    },
    QuantitySelector: {
      decrease: "Giảm số lượng",
      increase: "Tăng số lượng",
      quantity: "Số lượng: {quantity}",
    },
    MessengerChatWidget: {
      customerSupport: "Hỗ trợ khách hàng",
      online: "Online",
      close: "Đóng",
      messagePlaceholder: "Nhập tin nhắn...",
      sendImage: "Gửi ảnh",
      openChat: "Mở chat hỗ trợ",
      welcomeMessage: "Xin chào! Mình có thể hỗ trợ gì cho bạn?",
      thankYouMessage: "Cảm ơn bạn! Admin sẽ phản hồi sớm nhất.",
      imageReceived: "Đã nhận được hình ảnh của bạn.",
    },
  },
  Views: {
    Login: {
      google: "Google",
      facebook: "Facebook",
    },
    Products: {
      title: "Tất cả sản phẩm",
      found: "Tìm thấy {count} sản phẩm",
      noResults: "Không tìm thấy sản phẩm",
      adjustFilters: "Thử điều chỉnh bộ lọc để xem thêm sản phẩm",
      clearFilters: "Xóa bộ lọc",
      previous: "Trước",
      next: "Sau",
      page: "Trang {current} / {total}",
    },
    Favourite: {
      emptyTitle: "Bạn chưa có sản phẩm yêu thích",
      emptyDescription: "Hãy thêm vài sản phẩm để tiện xem lại và mua nhanh hơn.",
      explore: "Khám phá sản phẩm",
      removeFromFavourite: "Xóa khỏi yêu thích",
      noDescription: "Chưa có mô tả",
      category: "Loại:",
      color: "Màu:",
      size: "Size:",
      details: "Chi tiết",
    },
    NotFound: {
      title: "Trang không tồn tại",
      message: "Xin lỗi, trang bạn tìm kiếm không tồn tại.",
      backHome: "Về trang chủ",
    },
    VerifyEmail: {
      title: "Xác thực Email",
      sentTo: "Chúng tôi đã gửi mã xác thực đến email",
      email: "email của bạn",
      enterCode: "Nhập mã xác thực 6 chữ số",
      checking: "Đang kiểm tra...",
      verifying: "Đang xác thực...",
      verifyButton: "Xác thực Email",
      noCode: "Chưa nhận được mã?",
      resend: "Gửi lại mã",
      resendAfter: "Gửi lại sau {seconds}s",
      backToRegister: "Quay lại",
      register: "Đăng ký",
      emailRequired: "Email là bắt buộc",
      emailInvalid: "Email không hợp lệ",
      codeRequired: "Vui lòng nhập mã xác thực",
      codeLength: "Mã xác thực phải có 6 chữ số",
      codeNumeric: "Mã xác thực chỉ chứa số",
      enterAllDigits: "Vui lòng nhập đủ 6 chữ số",
      success: "Xác thực thành công!",
      error: "Xác thực thất bại!",
      emailNotFound: "Không tìm thấy email. Vui lòng đăng ký lại.",
      resendSuccess: "Đã gửi lại mã xác thực!",
      resendError: "Gửi lại mã thất bại!",
      pleaseRegister: "Vui lòng đăng ký để nhận mã xác thực",
    },
    PaymentDemo: {
      badge: "🧪 DEMO MODE - Thanh toán thử nghiệm",
      title: "Thanh toán MoMo",
      subtitle: "Trang thanh toán demo - Không thực sự trừ tiền",
      orderIdLabel: "Mã đơn hàng:",
      amountLabel: "Số tiền:",
      transactionIdLabel: "Transaction ID:",
      phoneLabel: "Số điện thoại MoMo",
      phonePlaceholder: "0123456789",
      passwordLabel: "Mật khẩu (Demo)",
      passwordPlaceholder: "Nhập bất kỳ (demo)",
      otpTitle: "Xác thực OTP",
      otpInstruction: "Mã OTP đã được gửi tới số điện thoại MoMo của bạn (demo). Vui lòng nhập mã gồm 6 chữ số để hoàn tất giao dịch.",
      otpInputLabel: "Nhập mã OTP",
      otpPlaceholder: "••••••",
      otpDemoCodeMessage: "Mã OTP demo mặc định: {code}",
      infoNoteLabel: "Lưu ý:",
      infoNoteText: "Đây là chế độ demo. Không có giao dịch thực tế nào được thực hiện. Bạn có thể test cả trường hợp thanh toán thành công và thất bại.",
      buttons: {
        continue: "✅ Tiếp tục & Nhập OTP (Demo)",
        processing: "Đang xử lý...",
        confirm: "🔐 Xác nhận OTP",
        back: "Quay lại",
        cancel: "Hủy bỏ",
      },
      otpErrors: {
        incomplete: "Vui lòng nhập đầy đủ 6 chữ số OTP",
        incorrect: "Mã OTP không chính xác. Vui lòng thử lại.",
      },
      toasts: {
        noOrder: "Không tìm thấy thông tin đơn hàng",
        invalidPhone: "Vui lòng nhập số điện thoại MoMo hợp lệ",
        missingPassword: "Vui lòng nhập mật khẩu demo",
        otpSent: "Mã OTP demo đã được gửi về SMS. Vui lòng nhập mã để tiếp tục.",
        otpInvalid: "Mã OTP không hợp lệ (demo)",
        success: "Thanh toán thành công! (Demo)",
        failure: "Thanh toán thất bại! (Demo)",
        genericError: "Có lỗi xảy ra",
        processError: "Có lỗi xảy ra khi xử lý thanh toán demo",
      },
      PaymentSuccess: {
        title: "Thanh toán thành công!",
        description: "Đơn hàng của bạn đã được thanh toán thành công.",
        orderIdLabel: "Mã đơn hàng",
        actions: {
          viewOrder: "Xem đơn hàng",
          goHome: "Về trang chủ",
        },
      },
      PaymentCancel: {
        title: "Thanh toán đã bị hủy",
        description: "Bạn đã hủy quá trình thanh toán. Đơn hàng vẫn được lưu và bạn có thể thanh toán lại sau.",
        orderIdLabel: "Mã đơn hàng",
        actions: {
          retry: "Thử thanh toán lại",
          viewOrder: "Xem đơn hàng",
          goHome: "Về trang chủ",
        },
      },
    },
    OrderDetail: {
      title: "Đơn hàng của bạn",
      thankYou: "Cảm ơn bạn đã mua hàng tại Shoez",
      orderId: "Mã đơn hàng",
      orderDate: "Ngày đặt",
      estimatedDelivery: "Dự kiến giao",
      productsOrdered: "Sản phẩm đã đặt",
      size: "Size:",
      color: "Màu:",
      quantity: "Số lượng:",
      shippingAddress: "Địa chỉ giao hàng",
      paymentMethod: "Phương thức thanh toán",
      shippingMethod: "Phương thức vận chuyển",
      note: "Ghi chú:",
      orderSummary: "Tóm tắt đơn hàng",
      subtotal: "Tạm tính",
      shippingFee: "Phí vận chuyển",
      free: "Miễn phí",
      total: "Tổng cộng",
      orderStatus: "Trạng thái đơn hàng",
      orderPlaced: "Đơn hàng đã được đặt",
      confirmed: "Đã xác nhận",
      shipping: "Đang giao hàng",
      estimated: "Dự kiến:",
      inTransit: "Hàng đang được vận chuyển",
      completed: "Hoàn thành",
      reviewProducts: "Đánh giá sản phẩm",
      reviewDescription: "Chia sẻ trải nghiệm của bạn về sản phẩm đã mua",
      review: "Đánh giá",
      continueShopping: "Tiếp tục mua sắm",
      viewAllOrders: "Xem tất cả đơn hàng",
      notFound: "Không tìm thấy đơn hàng",
      notFoundMessage: "Đơn hàng không tồn tại hoặc bạn không có quyền xem",
      backToOrders: "Quay lại danh sách đơn hàng",
      statusPending: "Chờ xác nhận",
      statusConfirmed: "Đã xác nhận",
      statusShipping: "Đang giao",
      statusComplete: "Hoàn thành",
      statusCancelled: "Đã hủy",
      paymentCOD: "Thanh toán khi nhận hàng",
      paymentCreditCard: "Thẻ tín dụng",
      paymentTransfer: "Chuyển khoản ngân hàng",
      paymentMomo: "MoMo",
      paymentShopeePay: "ShopeePay",
      paymentZalopay: "ZaloPay",
      paymentCODDesc: "Bạn sẽ thanh toán khi nhận hàng",
      paymentCardDesc: "Đã thanh toán bằng thẻ",
      paymentTransferDesc: "Đã chuyển khoản ngân hàng",
      paymentMomoDesc: "Đã thanh toán qua MoMo",
      paymentShopeePayDesc: "Đã thanh toán qua ShopeePay",
      paymentZalopayDesc: "Đã thanh toán qua ZaloPay",
      shippingStandard: "Giao hàng tiêu chuẩn",
      shippingExpress: "Giao hàng nhanh",
      shippingPickup: "Nhận tại cửa hàng",
    },
    Notifications: {
      title: "Thông báo",
      subtitle: "Quản lý tất cả thông báo của bạn",
      markAllRead: "Đánh dấu đã đọc tất cả",
      deleteAllRead: "Xóa tất cả đã đọc",
      viewDetails: "Xem chi tiết",
      markAsRead: "Đánh dấu đã đọc",
      noNotifications: "Không có thông báo",
      allNotifications: "Tất cả thông báo của bạn sẽ xuất hiện ở đây.",
    },
    Forbidden: {
      title: "Truy cập bị từ chối",
      message: "Bạn không có quyền truy cập vào trang này",
      help: "Vui lòng kiểm tra lại thông tin đăng nhập hoặc liên hệ với quản trị viên để được hỗ trợ.",
      backHome: "Về trang chủ",
      login: "Đăng nhập",
      reasons: "Lý do có thể gây ra lỗi này:",
      notLoggedIn: "Chưa đăng nhập",
      notLoggedInDesc: "Bạn cần đăng nhập để truy cập",
      noPermission: "Không đủ quyền",
      noPermissionDesc: "Tài khoản không có quyền truy cập",
      sessionExpired: "Phiên đăng nhập hết hạn",
      sessionExpiredDesc: "Vui lòng đăng nhập lại",
      accountLocked: "Tài khoản bị khóa",
      accountLockedDesc: "Liên hệ admin để mở khóa",
      needHelp: "Cần hỗ trợ?",
      email: "Email",
      hotline: "Hotline",
    },
    FAQ: {
      title: "Câu hỏi thường gặp (FAQ)",
      subtitle: "Tổng hợp các câu hỏi thường gặp giúp bạn nhanh chóng tìm được câu trả lời.",
      q1: "Làm thế nào để đổi size?",
      a1: "Bạn có thể liên hệ CSKH trong vòng 7 ngày kể từ ngày nhận hàng và làm theo hướng dẫn đổi trả. Vui lòng giữ nguyên tem mác và tình trạng sản phẩm.",
      q2: "Thời gian giao hàng mất bao lâu?",
      a2: "Thời gian giao hàng phụ thuộc vào khu vực và đơn vị vận chuyển, thông thường 2–5 ngày làm việc cho khu vực nội thành.",
      q3: "Tôi có thể trả hàng nếu sản phẩm lỗi?",
      a3: "Có. Nếu sản phẩm lỗi do nhà sản xuất, vui lòng liên hệ CSKH và gửi bằng chứng (ảnh/ video). Shoez Shop sẽ hướng dẫn quy trình đổi trả hoặc bảo hành.",
      q4: "Làm sao để theo dõi đơn hàng?",
      a4: "Bạn có thể kiểm tra trạng thái đơn trong trang Hồ sơ > Đơn hàng hoặc liên hệ hotline để được hỗ trợ nhanh.",
      contactSupport: "Liên hệ hỗ trợ",
    },
    Warranty: {
      title: "Bảo hành sản phẩm",
      subtitle: "Thông tin bảo hành rõ ràng giúp bạn yên tâm khi mua sắm tại Shoez Shop. Dưới đây là những điều cần biết khi yêu cầu bảo hành.",
      termsTitle: "Thời hạn & Điều kiện",
      termsDesc: "Mỗi sản phẩm có thời hạn bảo hành khác nhau; kiểm tra trang sản phẩm hoặc phiếu bảo hành kèm theo.",
      terms1: "Sản phẩm trong thời hạn bảo hành.",
      terms2: "Lỗi do nhà sản xuất (không áp dụng do va chạm, ngấm nước).",
      terms3: "Kèm hóa đơn hoặc mã bảo hành.",
      notCoveredTitle: "Trường hợp không được bảo hành",
      notCovered1: "Sử dụng sai cách, va chạm, rơi vỡ.",
      notCovered2: "Sản phẩm hỏng do tác động môi trường hoặc hao mòn tự nhiên.",
      notCovered3: "Thiếu tem/phiếu bảo hành hoặc chứng từ mua hàng.",
      processTitle: "Quy trình bảo hành",
      process1: "Liên hệ CSKH hoặc mang sản phẩm tới trung tâm bảo hành.",
      process2: "Nhân viên kiểm tra và đánh giá nguyên nhân hỏng hóc.",
      process3: "Sửa chữa hoặc thay thế theo chính sách nếu đủ điều kiện.",
      contactWarranty: "Liên hệ bảo hành",
    },
    ReturnPolicy: {
      title: "Chính sách đổi trả",
      subtitle: "Chúng tôi luôn nỗ lực để đem lại trải nghiệm mua sắm tốt nhất. Dưới đây là các điều kiện và quy trình đổi trả tại Shoez Shop.",
      conditionsTitle: "Điều kiện đổi trả",
      condition1: "Sản phẩm còn nguyên tem, mác, chưa qua sử dụng.",
      condition2: "Yêu cầu trong vòng 7 ngày kể từ ngày nhận hàng.",
      condition3: "Kèm hóa đơn hoặc mã đơn hàng để đối chiếu.",
      processTitle: "Quy trình đổi trả",
      process1: "Liên hệ CSKH với mã đơn hàng và lý do.",
      process2: "Gửi trả hàng theo hướng dẫn của Shoez Shop.",
      process3: "Nhận hàng, kiểm tra và tiến hành đổi/hoàn tiền.",
      refundTitle: "Hoàn tiền & Lưu ý",
      refundDesc: "Hoàn tiền tùy phương thức thanh toán: 3–14 ngày làm việc.",
      refundNote: "Phí vận chuyển đổi trả sẽ được xử lý theo chính sách. Sản phẩm giảm giá có thể không áp dụng đổi trả.",
      guideTitle: "Hướng dẫn chi tiết",
      guide1: "Liên hệ chăm sóc khách hàng qua Liên hệ hoặc hotline; cung cấp mã đơn hàng và mô tả lỗi.",
      guide2: "Nhân viên sẽ gửi hướng dẫn gửi trả và xác nhận điều kiện.",
      guide3: "Sau khi nhận hàng và kiểm tra, Shoez Shop sẽ hoàn tiền hoặc đổi sản phẩm theo yêu cầu.",
      contact: "Liên hệ",
      contactSupport: "Liên hệ hỗ trợ",
    },
    PurchaseGuide: {
      title: "Hướng dẫn mua hàng",
      subtitle: "Các bước mua hàng đơn giản, nhanh chóng — theo dõi hướng dẫn bên dưới để hoàn tất đơn hàng một cách an toàn.",
      step1Title: "Chọn sản phẩm",
      step1Desc: "Chọn size, màu và số lượng rồi thêm vào giỏ hàng.",
      step2Title: "Thanh toán",
      step2Desc: "Chọn phương thức thanh toán phù hợp: COD, thẻ, chuyển khoản hoặc ví điện tử.",
      step3Title: "Theo dõi đơn hàng",
      step3Desc: "Theo dõi trạng thái trong trang Hồ sơ hoặc liên hệ CSKH để biết chi tiết.",
      tipsTitle: "Mẹo",
      tip1: "Kiểm tra kỹ size và mô tả sản phẩm trước khi mua.",
      tip2: "Lưu lại mã đơn hàng để tra cứu nhanh.",
      contactSupport: "Liên hệ hỗ trợ",
    },
    Checkout: {
      header: {
        title: "Thanh toán",
        subtitle: "Hoàn tất đơn hàng của bạn"
      },
      steps: {
        shipping: "Giao hàng",
        payment: "Thanh toán",
        review: "Xác nhận"
      },
      shipping: {
        title: "Thông tin giao hàng",
        fields: {
          fullName: {
            label: "Họ và tên *",
            placeholder: "Nhập họ và tên"
          },
          phone: {
            label: "Số điện thoại *",
            placeholder: "Nhập số điện thoại"
          },
          email: {
            label: "Email *",
            placeholder: "Nhập email"
          },
          address: {
            label: "Địa chỉ *",
            placeholder: "Nhập địa chỉ chi tiết"
          },
          city: {
            label: "Tỉnh/Thành phố *",
            placeholder: "Nhập tỉnh/thành phố"
          },
          district: {
            label: "Quận/Huyện *",
            placeholder: "Nhập quận/huyện"
          },
          ward: {
            label: "Phường/Xã *",
            placeholder: "Nhập phường/xã"
          }
        },
        methodTitle: "Phương thức giao hàng",
        methods: {
          standard: {
            label: "Giao hàng tiêu chuẩn",
            description: "Nhận hàng trong 3-5 ngày",
            price: "30.000đ"
          },
          express: {
            label: "Giao hàng nhanh",
            description: "Nhận hàng trong 1-2 ngày",
            price: "50.000đ"
          },
          pickup: {
            label: "Nhận tại cửa hàng",
            description: "Nhận hàng trực tiếp",
            price: "Miễn phí"
          }
        },
        noteLabel: "Ghi chú (tuỳ chọn)",
        notePlaceholder: "Ghi chú cho đơn hàng..."
      },
      payment: {
        title: "Phương thức thanh toán",
        options: {
          cod: {
            label: "Thanh toán khi nhận hàng (COD)",
            description: "Trả tiền mặt khi nhận hàng"
          },
          creditCard: {
            label: "Thẻ tín dụng/Ghi nợ",
            description: "Thanh toán an toàn bằng thẻ Visa, MasterCard"
          },
          bankTransfer: {
            label: "Chuyển khoản ngân hàng",
            description: "Chuyển khoản trực tiếp tới tài khoản ngân hàng"
          },
          momo: {
            label: "Ví MoMo",
            description: "Thanh toán nhanh qua ví MoMo"
          },
          shopeePay: {
            label: "ShopeePay",
            description: "Thanh toán nhanh qua ví ShopeePay"
          },
          zaloPay: {
            label: "ZaloPay",
            description: "Thanh toán nhanh qua ví ZaloPay"
          }
        },
        creditCardForm: {
          numberLabel: "Số thẻ",
          numberPlaceholder: "1234 5678 9012 3456",
          nameLabel: "Tên chủ thẻ",
          namePlaceholder: "NGUYEN VAN A",
          expiryLabel: "Ngày hết hạn",
          expiryPlaceholder: "MM/YY",
          cvvLabel: "CVV",
          cvvPlaceholder: "123"
        },
        momo: {
          headerTitle: "Ví điện tử MoMo",
          headerDescription: "Thanh toán nhanh chóng và an toàn",
          phoneLabel: "Số điện thoại MoMo *",
          phonePlaceholder: "Nhập số điện thoại đã đăng ký MoMo",
          phoneHint: "Số điện thoại phải có 10 chữ số và đã đăng ký ví MoMo",
          qrPending: "Mã QR sẽ được tạo sau",
          qrInstructionPending: "QR sẽ hiển thị sau khi nhập số điện thoại",
          qrTitle: "Hoặc quét mã QR để thanh toán",
          qrDescription: "Mở ứng dụng MoMo và quét mã QR phía trên",
          phoneVerified: "✓ Số điện thoại đã được xác nhận",
          instructionsTitle: "Hướng dẫn thanh toán",
          instructions: {
            step1: "Nhập số điện thoại đã đăng ký ví MoMo",
            step2: "Quét mã QR trong ứng dụng MoMo hoặc xác nhận trên điện thoại",
            step3: "Xác nhận thanh toán trên ứng dụng MoMo",
            step4: "Chờ xác nhận thanh toán"
          },
          securityTitle: "Thanh toán an toàn với MoMo",
          securityDescription: "Thông tin thanh toán của bạn được mã hóa. Chúng tôi không lưu trữ số điện thoại hay thông tin ví của bạn."
        },
        shopeePay: {
          headerTitle: "Ví ShopeePay",
          headerDescription: "Thanh toán nhanh chóng và an toàn",
          phoneLabel: "Số điện thoại ShopeePay *",
          phonePlaceholder: "Nhập số điện thoại đã đăng ký ShopeePay",
          phoneHint: "Số điện thoại phải có 10 chữ số và đã đăng ký ShopeePay",
          instructionsTitle: "Hướng dẫn thanh toán",
          instructions: {
            step1: "Nhập số điện thoại đã đăng ký ví ShopeePay",
            step2: "Xác nhận thanh toán trên ứng dụng ShopeePay",
            step3: "Chờ xác nhận thanh toán"
          },
          securityTitle: "Thanh toán an toàn với ShopeePay",
          securityDescription: "Thông tin thanh toán của bạn được mã hóa. Chúng tôi không lưu trữ số điện thoại hay thông tin ví của bạn."
        },
        zaloPay: {
          headerTitle: "Ví ZaloPay",
          headerDescription: "Thanh toán nhanh chóng và an toàn",
          phoneLabel: "Số điện thoại ZaloPay *",
          phonePlaceholder: "Nhập số điện thoại đã đăng ký ZaloPay",
          phoneHint: "Số điện thoại phải có 10 chữ số và đã đăng ký ZaloPay",
          instructionsTitle: "Hướng dẫn thanh toán",
          instructions: {
            step1: "Nhập số điện thoại đã đăng ký ví ZaloPay",
            step2: "Xác nhận thanh toán trên ứng dụng ZaloPay",
            step3: "Chờ xác nhận thanh toán"
          },
          securityTitle: "Thanh toán an toàn với ZaloPay",
          securityDescription: "Thông tin thanh toán của bạn được mã hóa. Chúng tôi không lưu trữ số điện thoại hay thông tin ví của bạn."
        },
        securityNotice: "Thông tin thẻ của bạn được bảo mật và mã hóa. Chúng tôi không lưu trữ thông tin thẻ của bạn.",
        securityBadge: "Thanh toán an toàn & bảo mật"
      },
      summary: {
        title: "Tóm tắt đơn hàng",
        sizePrefix: "Size",
        quantityPrefix: "SL:",
        subtotal: "Tạm tính",
        shippingFee: "Phí vận chuyển",
        freeShipping: "Miễn phí",
        total: "Tổng cộng",
        previousStep: "Quay lại bước trước"
      },
      actions: {
        nextToPayment: "Tiếp tục thanh toán",
        nextToReview: "Tiếp tục xác nhận",
        placeOrder: "Đặt hàng",
        continue: "Tiếp tục"
      },
      toasts: {
        fillShipping: "Vui lòng điền đầy đủ thông tin giao hàng",
        invalidMomoPhone: "Vui lòng nhập số điện thoại MoMo hợp lệ (10 chữ số)",
        invalidShopeePayPhone: "Vui lòng nhập số điện thoại ShopeePay hợp lệ (10 chữ số)",
        invalidZaloPayPhone: "Vui lòng nhập số điện thoại ZaloPay hợp lệ (10 chữ số)",
        loginRequired: "Vui lòng đăng nhập để đặt hàng",
        creatingMomoPayment: "Đang tạo yêu cầu thanh toán MoMo...",
        createPaymentError: "Có lỗi xảy ra khi tạo yêu cầu thanh toán. Đơn hàng đã được tạo.",
        placeOrderError: "Có lỗi xảy ra khi đặt hàng. Vui lòng thử lại."
      },
      successModal: {
        totalLabel: "Tổng thanh toán",
        deliveryEstimateLabel: "Dự kiến giao hàng",
        continueShopping: "Tiếp tục mua sắm",
        viewOrder: "Xem đơn hàng"
      }
    },
  },
  OAuthCallback: {
    processing: "Đang xử lý đăng nhập...",
    close: "Đóng",
    error: "Có lỗi xảy ra khi đăng nhập",
  },
  CheckoutLayout: {
    supportMoMo: "Cần hỗ trợ? Liên hệ hotline MoMo: 1800.1207",
    orderSuccess: "Đặt hàng thành công!",
    thankYou: "Cảm ơn bạn đã đặt hàng. Đơn hàng của bạn đã được xác nhận.",
    orderId: "Mã đơn hàng:",
  },
  ProductDetailLayout: {
    login: "Đăng nhập",
    close: "Đóng",
  },
  OrderDetailModal: {
    close: "Đóng",
    printOrder: "In đơn hàng",
  },
  ContactTemplate: {
    title: "LIÊN HỆ",
    subtitle: "Chúng tôi luôn sẵn sàng lắng nghe và hỗ trợ bạn. Hãy liên hệ với chúng tôi để được tư vấn và giải đáp mọi thắc mắc.",
    contactInfo: "THÔNG TIN LIÊN HỆ",
    address: "ĐỊA CHỈ",
    addressLine1: "Tầng 6, 266 Đội Cần, Hà Nội",
    addressLine2: "P. Uối Cần, Phân Kế Bình",
    phone: "ĐIỆN THOẠI",
    email: "EMAIL",
    emailLabel: "Email",
    emailPlaceholder: "Nhập Email *",
    followUs: "THEO DÕI CHÚNG TÔI",
    sendMessage: "GỬI TIN NHẮN CHO CHÚNG TÔI",
    fullName: "Họ tên",
    fullNamePlaceholder: "Nhập họ tên *",
    content: "Nội dung",
    messagePlaceholder: "Lời nhắn",
    sendButton: "GỬI TIN NHẮN",
    otherBranches: "CÁC CHI NHÁNH KHÁC",
    location1Name: "Cung thể Hạo Quận Ngựa",
    location1Address: "Tổ 6B, Lúc quá",
    location1City: "Hà Nội",
    location2Name: "HỒ DÂM TRÒN",
    location2Address: "Tổ 1B",
    location2City: "Hà Nội",
    location3Name: "Bảo lạng Chiến thăng B-52",
    location3Address: "P. Đội Cần",
    location3City: "Hà Nội",
    needSupportNow: "CẦN HỖ TRỢ NGAY?",
    supportTeam: "Đội ngũ chăm sóc khách hàng của chúng tôi luôn sẵn sàng hỗ trợ bạn 24/7",
    callNow: "GỌI NGAY",
    sendEmail: "GỬI EMAIL",
    thankYouContact: "Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi sớm nhất có thể.",
  },
  AboutTemplate: {
    title: "VỀ DELVOR",
    subtitle: "Thương hiệu giày thời trang cao cấp, mang đến những trải nghiệm mua sắm tuyệt vời và sản phẩm chất lượng cho người dùng Việt Nam",
    mission: "Sứ Mệnh Của Chúng Tôi",
    missionText: "Chúng tôi cam kết mang đến những đôi giày chất lượng nhất, kết hợp giữa thiết kế thời thượng và sự thoải mái tối đa. Mỗi sản phẩm là sự kết tinh của đam mê và sáng tạo.",
    missionQuote: "Mang đến trải nghiệm mua sắm giày dép tuyệt vời nhất cho người Việt",
    coreValues: "Giá Trị Cốt Lõi",
    coreValuesSubtitle: "Những nguyên tắc vàng tạo nên sự khác biệt của Delvor",
    quality: "Chất Lượng",
    qualityText: "Mỗi đôi giày được sản xuất với quy trình kiểm soát chất lượng nghiêm ngặt, đảm bảo độ bền và sự thoải mái tối đa.",
    design: "Thiết Kế",
    designText: "Đội ngũ thiết kế sáng tạo không ngừng, mang đến những mẫu giày độc đáo, hợp thời trang và phù hợp với xu hướng toàn cầu.",
    community: "Cộng Đồng",
    communityText: "Xây dựng cộng đồng yêu giày, chia sẻ kiến thức và lan tỏa đam mê đến mọi khách hàng.",
    journey: "Hành Trình Phát Triển",
    timeline1Title: "Khởi Đầu",
    timeline1Text: "Delvor được thành lập với sứ mệnh mang đến những đôi giày chất lượng đầu tiên cho thị trường Việt Nam.",
    timeline2Title: "Mở Rộng",
    timeline2Text: "Ra mắt cửa hàng trực tuyến, mang sản phẩm đến với khách hàng trên toàn quốc.",
    timeline3Title: "Đột Phá",
    timeline3Text: "Giới thiệu dòng sản phẩm cao cấp, hợp tác với các nhà thiết kế quốc tế.",
    timeline4Title: "Hiện Tại",
    timeline4Text: "Trở thành một trong những thương hiệu giày được yêu thích nhất với hơn 50,000 khách hàng tin dùng.",
    ctaTitle: "Sẵn Sàng Khám Phá?",
    ctaSubtitle: "Khám phá bộ sưu tập giày mới nhất của chúng tôi và tìm cho mình đôi giày hoàn hảo",
    shopNow: "MUA SẮM NGAY",
    contact: "LIÊN HỆ",
  },
};
