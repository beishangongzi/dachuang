// pages/search/search.js
Page({

        /**
         * Page initial data
         */
        data: {
                image: 'sss',
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
                                that.image = res.tempFilePaths[0]
                        },
                });



        },

        uploadImage: function(){
                var that = this;
                wx.uploadFile({
                        url: 'http://192.168.8.101:8000/query/',
                        filePath: that.image,
                        name: 'image',
                        header: {
                                'content-type': 'application/x-www-form-urlencoded'
                        },
                        success: function(res){
                                console.log(res)
                        },
                        complete: function(res){
                                console.log(path)
                        }
                })
        }
})