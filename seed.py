import json
from app import app
from flask_bcrypt import Bcrypt
from model import db, Product, Customer, TopCategory, FeaturedBrands, Payment, Order

bcrypt = Bcrypt(app)

with app.app_context():

    Product.query.delete()
    Customer.query.delete()
    TopCategory.query.delete()
    FeaturedBrands.query.delete()
    Payment.query.delete()
    Order.query.delete()
 

    db.session.commit()

    customer_data = [
        {'id':1, 'firstname':'John', 'lastname':'Peter','phone':'0712675356', 'email':'john@gmail.com', 'password': bcrypt.generate_password_hash('john'), 'is_admin':True},
        {'id':2, 'firstname':'Lucy', 'lastname':'liz','phone':'0765345901', 'email':'lucy@gmail.com', 'password':bcrypt.generate_password_hash('lucy'), 'is_admin':False}
    ]

    for item in customer_data:
        new_customer = Customer(**item)
        db.session.add(new_customer)
    db.session.commit()


    data = [
    { 'id': 1, 'name': 'Apple', 'category': 'Fruits', 'weight': '250g', 'price': '1.99', 'quantity': 10, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_27f437949aa7ff723dcd79d49f33923782d863f53439c2f06ed6acf40188f677.png?w=1024&h=1024' },
    { 'id': 2, 'name': 'Carrot', 'category': 'Fruits','weight': '250g',  'price': '0.99', 'quantity': 15, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_1c53fa7ea665a3ae324e9bf9a2b53744b3d8201d800147b84d2a336561c29548.png?w=1024&h=1024' },
    { 'id': 3, 'name': 'Banana', 'category': 'Fruits', 'weight': '250g', 'price': '0.75', 'quantity': 9, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_cbf23631d5c48d885a437266163f3654474858c647c4b54a11c8b63c95973460.png?w=1024&h=1024' },
    { 'id': 4, 'name': 'Grapes', 'category': 'Fruits', 'weight': '250g', 'price': '2.49', 'quantity': 4, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_da218e2b1d438758b4f64ab4b77da9826c43342d75b6075aa3e9446fa89dd667.png?w=1024&h=1024' },
    { 'id': 5, 'name': 'Strawberry', 'category': 'Fruits', 'weight': '250g', 'price': '1.79', 'quantity': 17, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_523c1556d0274a14d44ca9e70ab8c88b920bfca5ffb78a1f73543a31a650ca3c.png?w=1024&h=1024' },
    { 'id': 6, 'name': 'Cucumber', 'category': 'Fruits', 'weight': '250g', 'price': '0.69', 'quantity': 10, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_da9e584c75ca8dd0ecefef754b36751a0d9b17a93cdfdb370b8746461e80ae5d.png?w=1024&h=1024' },
    { 'id': 7, 'name': 'Pineapple', 'category': 'Fruits', 'weight': '250g', 'price': 'Kshs.2.99', 'quantity': 14, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_01aeaa982b4648323a50e996e27b57fcd9fc626459afaebbd1a4d7721041b54f.png?w=1024&h=1024' },
    { 'id': 8, 'name': 'Tomato', 'category': 'Fruits', 'weight': '250g', 'price': 'Kshs.0.89', 'quantity': 19, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_e723f623853feec4b2f1073cfd08395cfa35460631bfa2981c10d2882d0dc072.png?w=1024&h=1024' },
    { 'id': 9, 'name': 'Mango', 'category': 'Fruits', 'weight': '250g', 'price': 'Kshs.1.99', 'quantity': 12, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_06acb7ca59481e754e20bb0a00afd985ee72de1c6a4fe79ccc6eb4335fe02690.png?w=1024&h=1024' },
    { 'id': 10, 'name': 'Broccoli', 'category': 'Fruits', 'weight': '250g', 'price': '1.49', 'quantity': 4, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_aef2196463e2855ca11ebe2664d85198dc6e5f11696fc2c0bfde6134197b0e57.png?w=1024&h=1024' },
    { 'id': 11, 'name': 'Potato', 'category': 'Fruits', 'weight': '250g', 'price': '0.49', 'quantity': 10, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_a75c1e41b3edfcf8291173100c37bb51a9375fd3f3897fccbb003d9814d300f9.png?w=1024&h=1024' },
    { 'id': 12, 'name': 'Watermelon', 'category': 'Fruits', 'weight': '250g', 'price': '3.99', 'quantity': 8, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_8fcd2ee67aed0f72239189121b54b2b83e984da6c5774737779f56f2cc53cfb7.png?w=1024&h=1024' },
    { 'id': 13, 'name': 'Bell Pepper', 'category': 'Fruits','weight': '250g', 'price': '1.29', 'quantity': 10, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_245f3c90e62f34ff7c326ce580d792539746f3b1b6d42b1cc5871647e8f7a422.png?w=1024&h=1024' },
    { 'id': 14, 'name': 'Blueberries', 'category': 'Fruits', 'weight': '250g', 'price': '2.99', 'quantity': 11, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_5a662f9c1a16a5f0082f60ba0ea65424acda7b77fc124d7da0b2244438fbb408.png?w=1024&h=1024' },
    { 'id': 15, 'name': 'Zucchini', 'category': 'Fruits', 'weight': '250g',  'price': '1.19', 'quantity': 3, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_10bfdba91641bb3c6bb9dfe14b8b8a14e278a3bb7b9ee22148518d71c6c4fd2a.png?w=1024&h=1024' },
    { 'id': 16, 'name': 'Orange', 'category': 'Fruits', 'weight': '250g', 'price': '1.25', 'quantity': 2, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_48dc593109e98207c470d9a9929fe8a3ab9a8172b648f4cc155e51e757286c29.png?w=1024&h=1024' },
    { 'id': 17, 'name': 'Asparagus', 'category': 'Fruits', 'weight': '250g', 'price': '2.49', 'quantity': 10, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_985d9cd75eb658404d96faa47252cde16eeb6a608aafa0ba2fdaaf640e721c35.png?w=1024&h=1024' },
    { 'id': 18, 'name': 'Pear', 'category': 'Fruits', 'weight': '250g', 'price': '1.79', 'quantity': 10, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_3e8cec81d098009281d150897496f9aed81fbe87b013c6a56273e945e34e263c.png?w=1024&h=1024' },
    { 'id': 19, 'name': 'Cabbage', 'category': 'Fruits', 'weight': '250g', 'price': '0.99', 'quantity': 6, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_8a161d392a64f7b9deec8f153abfe453d11d2747c11603ebbcb496ca09d49855.png?w=1024&h=1024' },
    { 'id': 20, 'name': 'Avocado', 'category': 'Fruits', 'weight': '250g', 'price': '2.49', 'quantity': 10, 'imageurl': 'https://qph.cf2.poecdn.net/main-sdxl_2f6ce9d37605eef2dc9d4ed77dd9efca236a065361853e2795e732957fdddc35.png?w=1024&h=1024' },
    { 'id': 21, 'name': 'Del Monte Mixed Berry Juice 1L', 'category': 'Juices', 'weight': '1L', 'price': '1.99', 'quantity': 7, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h55/h2a/17213263544350/38584_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 22, 'name': 'Minute Maid Orange Pulpy Juice 1L', 'category': 'Juices', 'weight': '1L', 'price': '2.99', 'quantity': 21, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/hf6/h86/47857493540894/1700Wx1700H_69002_main.jpg?im=Resize=400' },
    { 'id': 23, 'name': 'Pick N Peel White Grape Juice 1L', 'category': 'Juices', 'weight': '1L', 'price': '3.99', 'quantity': 14, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h16/h80/26449917542430/41076_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 24, 'name': 'Del Monte Cranberry Apple Juice 1L', 'category': 'Juices', 'weight': '1L', 'price': '4.99', 'quantity': 9, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h33/h5e/17213097738270/100298_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 25, 'name': 'Highlands Cordial Tropical Juice 3L', 'category': 'Juices', 'weight': '3L', 'price': '5.99', 'quantity': 5, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/hf6/h26/49865986768926/1700Wx1700H_106817_main.jpg?im=Resize=400' },
    { 'id': 26, 'name': 'Coca Cola Soda 2L', 'category': 'Juices', 'weight': '2L', 'price': '0.99', 'quantity': 11, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/hae/h7c/12462213529630/24181_Main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 27, 'name': 'Sprite Soda 2L', 'category': 'Juices', 'weight': '2L', 'price': '1.99', 'quantity': 4, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h80/ha5/12462215823390/24185_Main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 28, 'name': 'Fanta Orange soda 2L', 'category': 'Juices', 'weight': '2L', 'price': '2.99', 'quantity': 2, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h30/h27/17292082774046/24183_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 29, 'name': 'Coca Cola Soda Assorted 2L x Pack Of 4', 'category': 'Juices', 'weight': '2L', 'price': '3.99', 'quantity': 10, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h2a/h35/12681321807902/134140_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 30, 'name': 'Ribena Blackcurrant Juice 250ml', 'category': 'Juices', 'weight': '250ml', 'price': '0.99', 'quantity': 9, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h4d/h5f/12462624735262/37138_Main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 31, 'name': 'Heineken Premium Quality 0.0 Non Alcoholic Beer 330ml', 'category': 'Juices', 'weight': '330ml', 'price': '1.99', 'quantity': 25, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h2e/h44/27845782503454/148720_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 32, 'name': 'Schweppes Ginger Ale Tonic Water 330Ml', 'category': 'Juices', 'weight': '330ml', 'price': '2.99', 'quantity': 13, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h42/hb6/34849917042718/1700Wx1700H_178181_main.jpg?im=Resize=400' },
    { 'id': 33, 'name': 'Quencher Life Premium Drinking Water 18L', 'category': 'Juices', 'weight': '18L', 'price': '3.99', 'quantity': 7, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h6e/h1c/12462987214878/17397_Main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 34, 'name': 'Waba Mineral Water 20L', 'category': 'Juices', 'weight': '20L', 'price': '4.99', 'quantity': 7, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h4d/h4e/16813704740894/60619_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 35, 'name': 'Aquaclear Drinking Water 300ml', 'category': 'Juices', 'weight': '300ml', 'price': '5.99', 'quantity': 10, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h9b/h35/16890515947550/16142_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 36, 'name': 'Aquamist Lemon Natural Mineral Water 500ml', 'category': 'Juices', 'weight': '500ml', 'price': '6.99', 'quantity': 20, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h58/had/45019205468190/1700Wx1700H_27888_main.jpg?im=Resize=400' },
    { 'id': 37, 'name': 'Red Bull Energy Drink 250ml x 4 Pieces', 'category': 'Juices', 'weight': '250ml', 'price': '7.99', 'quantity': 2, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h47/hea/51240487682078/1700Wx1700H_43217_main.jpg?im=Resize=400'},
    { 'id': 38, 'name': 'Monster Energy Drink 500ml', 'category': 'Juices', 'weight': '500ml', 'price': '8.99', 'quantity': 11, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/hea/h8a/16873019867166/33440_main.jpg_1700Wx1700H?im=Resize=400'},
    { 'id': 39, 'name': 'Tropical Heat Snacks Salted Crisps 50G', 'category': 'Snacks', 'weight': '50G', 'price': '1.99', 'quantity': 10, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/he8/hf6/28550183551006/32275_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 40, 'name': 'Tropical Heat Snacks Waves Crisps Salted 30G', 'category': 'Snacks', 'weight': '30G', 'price': '2.99', 'quantity':3, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h7e/h2c/45843168657438/1700Wx1700H_32296_Main.jpg?im=Resize=400' },
    { 'id': 41, 'name': 'Norda Urban Stix BBQ Crunchy Corn Snacks 40g', 'category': 'Snacks', 'weight': '40g', 'price': '3.99', 'quantity': 4, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h18/h62/12463226093598/47651_Main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 42, 'name': 'Wow Sugared Snacks 250g', 'category': 'Snacks', 'weight': '250g', 'price': '4.99', 'quantity': 6, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/hd3/h34/12462296432670/27607_Main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 43, 'name': 'Tropical Heat Snacks Cheese & Onion Crisps 200G', 'category': 'Snacks', 'weight': '200G', 'price': '5.99', 'quantity': 21, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/hb0/h34/28550185025566/32281_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 44, 'name': 'Tropical Heat Snacks Chilli Lemon Crisps 400G', 'category': 'Snacks', 'weight': '400G', 'price': '6.99', 'quantity': 8, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h8a/he9/28550188433438/32290_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 45, 'name': 'Wow Sugared Snacks 100g', 'category': 'Snacks', 'weight': '100g', 'price': '7.99', 'quantity': 16, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/hd6/h34/12462295449630/27606_Main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 46, 'name': 'Bitez Crunchy Corn Barbeque Sauce Snack 30g', 'category': 'Snacks', 'weight': '30g', 'price': '8.99', 'quantity': 10, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h1e/h83/16872247984158/82805_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 47, 'name': 'Kripsii Snack Salted 100G', 'category': 'Snacks', 'weight': '100G', 'price': '9.99', 'quantity': 19, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h70/h80/33471201574942/34732_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 48, 'name': 'Haldiram\'s Indian Snacks Ratlami Sev 150g', 'category': 'Snacks', 'weight': '150g', 'price': '10.99', 'quantity': 3, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h7c/hbe/27846372622366/2041_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 49, 'name': 'Haldiram’s Indian Snacks Soya Sticks 150g', 'category': 'Snacks', 'weight': '150g', 'price': '11.99', 'quantity': 22, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h9a/hbb/27846364430366/2046_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 50, 'name': 'Haldirams Snacks Khatta Meetha 200G', 'category': 'Snacks', 'weight': '200G', 'price': '12.99', 'quantity': 11, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/he2/h6a/26760646852638/2033_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 51, 'name': 'HALDIRAMS SNACKS ALOO BHUJIA 350G', 'category': 'Snacks', 'weight': '350G', 'price': '13.99', 'quantity': 10, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h88/h7a/26760652423198/2057_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 52, 'name': 'Wots Bharti Ben Kenyan Indian Mix Bhusu Chevda 350g', 'category': 'Snacks', 'weight': '350g', 'price': '14.99', 'quantity': 10, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h91/haf/44987225505822/1700Wx1700H_166706_main.jpg?im=Resize=400' },
    { 'id': 53, 'name': 'Krackles Tangy Tomato Potato Chips 30g', 'category': 'Snacks', 'weight': '30g', 'price': '15.99', 'quantity': 3, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h44/he3/17385156476958/34680_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 54, 'name': 'Krackles Tingly Cheese And Onion Potato Chips 30g', 'category': 'Snacks', 'weight': '30g', 'price': '16.99', 'quantity': 5, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h3c/h13/17385153855518/34682_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 55, 'name': 'Krackles Bang Bang Chilli Potato Chips 30g', 'category': 'Snacks', 'weight': '30g', 'price': '17.99', 'quantity': 10, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/hf1/h91/17385152217118/34679_main.jpg_1700Wx1700H?im=Resize=400' },
    { 'id': 56, 'name': 'Urban Bites Peri-Peri Potato Chips 120g', 'category': 'Snacks', 'weight': '120g', 'price': '18.99', 'quantity': 15, 'imageurl': 'https://cdnprod.mafretailproxy.com/sys-master-root/h64/h6f/32227152363550/177850_main.jpg_1700Wx1700H?im=Resize=400' }
    ]


    for item in data:
        new_product = Product(**item)
        db.session.add(new_product)
    db.session.commit()


    featured_brands = [
        {"id":1, "imageurl":"https://qph.cf2.poecdn.net/main-sdxl_53905d0537125ce219396f7b5fd6cbee8d8b3b96ebe876b8684aa60dba5b9dee.png?w=1024&h=1024", "name":"Fruits and Vegetables"},
        {"id":2, "imageurl":"https://qph.cf2.poecdn.net/main-sdxl_0e846d664a9eea41ec98f7eb4b5ee4334e467ea51448b8cfb5f87f6f30b364bb.png?w=1024&h=1024", "name":"Dairy and Breakfast"},
        {"id":3, "imageurl":"https://qph.cf2.poecdn.net/main-sdxl_8af7b42cdf6446211e009ffff9e9b03959caa6aee196d0d89892a4426b56707c.png?w=1024&h=1024", "name":"Eggs, Fish and Meat"},
        {"id":4, "imageurl":"https://qph.cf2.poecdn.net/main-sdxl_1c33ae4bb7a623264fcdaa43a117aa3990d2df230b6cef33b678ee3df6235140.png?w=1024&h=1024", "name":"Cold drinks and juices"},
        {"id":5, "imageurl":"https://qph.cf2.poecdn.net/main-sdxl_817fe54400afc2221413404a4d0f2a814db2fb22a9e2248f8635646d7a36a00c.png?w=1024&h=1024", "name":"Snacks and Munchies"},
        {"id":6, "imageurl":"https://qph.cf2.poecdn.net/main-sdxl_141c9d38cfad939358c40282c29cb5963505b0e2235dda90b1dac3d46abe9374.png?w=1024&h=1024", "name":"Icy Delights"},
        {"id":7, "imageurl":"https://qph.cf2.poecdn.net/main-sdxl_f61ae215d734387e13e129753471671a10119f1657c87ea22d79ef9043705d4f.png?w=1024&h=1024", "name":"Bath and Body"}
    ]

    for data in featured_brands:
        new_data = FeaturedBrands(**data)
        db.session.add(new_data)
    db.session.commit()


    top_category = [
          {"id":1, "imageurl": "https://qph.cf2.poecdn.net/main-sdxl_53905d0537125ce219396f7b5fd6cbee8d8b3b96ebe876b8684aa60dba5b9dee.png?w=1024&h=1024", "name":"Fruits and Vegetables"},
          {"id":2, "imageurl": "https://qph.cf2.poecdn.net/main-sdxl_0e846d664a9eea41ec98f7eb4b5ee4334e467ea51448b8cfb5f87f6f30b364bb.png?w=1024&h=1024","name":"Dairy and Breakfast"},
          {"id":3, "imageurl": "https://qph.cf2.poecdn.net/main-sdxl_525ab1c0b664b740ad054e39f576197240915f38abca7394fc5398c1340341d3.png?w=1024&h=1024","name":"Eggs, Fish and Meat"},
          {"id":4, "imageurl": "https://qph.cf2.poecdn.net/main-sdxl_1c33ae4bb7a623264fcdaa43a117aa3990d2df230b6cef33b678ee3df6235140.png?w=1024&h=1024","name":"Cold drinks and juices"},
          {"id":5, "imageurl": "https://qph.cf2.poecdn.net/main-sdxl_817fe54400afc2221413404a4d0f2a814db2fb22a9e2248f8635646d7a36a00c.png?w=1024&h=1024","name":"Snacks and Munchies"},
          {"id":6, "imageurl": "https://qph.cf2.poecdn.net/main-sdxl_141c9d38cfad939358c40282c29cb5963505b0e2235dda90b1dac3d46abe9374.png?w=1024&h=1024","name":"Icy Delights"},
          {"id":7, "imageurl": "https://qph.cf2.poecdn.net/main-sdxl_f61ae215d734387e13e129753471671a10119f1657c87ea22d79ef9043705d4f.png?w=1024&h=1024","name":"Bath and Body"}
    ]

    for tops in top_category:
        new_tops = TopCategory(**tops)
        db.session.add(new_tops)
    db.session.commit()

    