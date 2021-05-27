// // pages/search/search.js
Page({

        /**
         * Page initial data
         */
        data: {
                image: 'sss',
                res: 'ss',
                background: ['blue', 'demo-text-2', 'demo-text-3'],
                indicatorDots: true,
                vertical: false,
                autoplay: true,
                interval: 2000,
                duration: 500,
                imgs :[],
                value: "经过分析，我们有 89.50% 的把握认为这是明万历年代产品。\n 明朝万历年间青花瓷特点是：\n万历是明代十六个皇帝中统治时间最长的一个，在位四十八年，处于晚明衰弱阶段。万历瓷器一般质地粗松，胎体厚重，器身多有变形，欠规整。其青花色调，早、中期呈蓝中泛紫色，晚期灰暗晕散。装饰工艺技法，有镂雕、镂孔、开光、暗刻等；青花纹饰开始采用淡描、铁线描及涂抹手法，此时绘画风格繁缛麻密，幼稚滞拙，具有粗痍的民间艺术风格。晚期画面更不考究，布局繁乱。人物形象比例失当。堂名款自嘉靖始，渐次增多。万历时，民窑器的绘图标记已有仙鹤、灵芝、兰草、盘肠、如意云头之类。以后清代康熙瓷中所采用的图记，盖源于此经过分析，我们有 89.50% 的把握认为这是明万历年代产品。\n 明朝万历年间青花瓷特点是：\n万历是明代十六个皇帝中统治时间最长的一个，在位四十八年，处于晚明衰弱阶段。万历瓷器一般质地粗松，胎体厚重，器身多有变形，欠规整。其青花色调，早、中期呈蓝中泛紫色，晚期灰暗晕散。装饰工艺技法，有镂雕、镂孔、开光、暗刻等；青花纹饰开始采用淡描、铁线描及涂抹手法，此时绘画风格繁缛麻密，幼稚滞拙，具有粗痍的民间艺术风格。晚期画面更不考究，布局繁乱。人物形象比例失当。堂名款自嘉靖始，渐次增多。万历时，民窑器的绘图标记已有仙鹤、灵芝、兰草、盘肠、如意云头之类。以后清代康熙瓷中所采用的图记，盖源于此"
        },

        downloadImage: function (name, im) {
                var that = this;
                var path = '';
                wx.downloadFile({
                        url: "http://192.168.8.101:8000/query/download?name=" + name,
                        success: function (res) {
                                path = res.tempFilePath;
                                im.push(path)
                                console.log(im);
                                that.setData({
                                        imgs: im
                                });
                        }
                })
                return im;
        },

        onLoad: function(){
                var im = []
                im = this.downloadImage("swiper_image_1.png", im);
                im = this.downloadImage("swiper_image_2.png", im);
                im = this.downloadImage("swiper_image_3.png", im);
        },

        selectimage: function(){
                var that = this;
                wx.chooseImage({
                        count: 1,
                        sizeType: 'original',        
                        success: function (res) {
                                that.setData({
                                        image: res.tempFilePaths[0],
                                }),
                                that.image = res.tempFilePaths[0];
                                wx.uploadFile({
                                        url: 'http://192.168.8.101:8000/query/',
                                        filePath: that.image,
                                        name: 'image',
                                        header: {
                                                'content-type': 'application/x-www-form-urlencoded'
                                        },
                                        success: function (res) {
                                                var obj = JSON.parse(res.data);
                                                console.log(obj);
                                                console.log("success");
                                                that.setData({
                                                        value: obj.s
                                                })
                                        },
                                })
                        },
                });

        }



})

