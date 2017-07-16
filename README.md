# 资源文件嵌入:重要资源的一种保护方式

##把重要的资源文件，转换成bytes数组，在使用的地方转成对应的资源。

###小工具：
    重要的资源文件（举例）:1.png(不限于图片)
  
### 使用方法：
     $: python（2.7） convert.py  -i 1.png  -o  1.png.h
   
### 在使用的地方引用H文件
      NSData *imageData = [NSData dataWithBytes:temp length:sizeof(temp)];（使用中需要考虑内存问题）
      通过NSData 转成对应资源文件
