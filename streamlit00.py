import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import time


st.markdown('### 三次方计算器 :sunglasses:')
x = st.slider('输入一个数字')
st.write(x, '的三次方为：', x**3)
st.markdown('> \int_0^1 Streamlit挺好用 :+1:')
st.markdown('Streamlit is **_really_ cool**.')
st.latex("\sum_{i=1}^{n}")
st.latex("\int_{i=1}^{n} x^2 dx")
st.markdown('$\int_{i=1}^{n} x^2 dx$,$\sum_{x=1}^{n} 3x^2$')
st.markdown('$\int_{i=1}^{n} x^2 dx$')




arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)




# 展示文本；文本直接使用Markdown语法
st.markdown("# Streamlit示例")
st.markdown("""
            - 这是
            - 一个
            - 无序列表
            """)

# 展示pandas数据框
st.dataframe(pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"]))

# 展示matplotlib绘图
arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)
plt.title("matplotlib plot")
st.pyplot()

# 加入交互控件，如输入框
number = st.number_input("Insert a number", 123)
st.write("输入的数字是：", number)


# 绘制1000个点的坐标
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.01)

# status_text.text('老虎，老虎')
st.balloons()


st.markdown('Streamlit is **_really_ cool**.')
# 展示文本；文本直接使用Markdown语法
st.markdown("# Streamlit示例")
st.markdown("""
<font size=5 >5号字</font>
            """)
st.markdown("Streamlit示例")
st.markdown("<font size=2 >2号字</font>")
st.markdown("\<font color=#FF0000>'红色'\<font>")

original_title = '<p style="font-family:Courier; color:Blue; font-size: 40px;">$$\int_{0}{\infty} f(x)dx$$ Original image 广州城市理工学院</p>'
st.markdown(original_title, unsafe_allow_html=True)
original_title = '<p style="font-size: 80px;">广州城市理工学院</p>'
st.markdown(original_title, unsafe_allow_html=True)

st.latex(r'''\Huge 
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


st.latex(r'''\huge 
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


st.latex(r'''\Large 
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.latex(r'''\large 
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


st.latex('\displaystyle\sum_{i=1}^n')



original_title = '''<p style="font-size: 40px;">
"<font size=100 >CSDN中的blog默认字号为3号字，字号数值可设为1~7，默认字体为微软雅黑。其它颜色值可参考 CSDN-markdown编辑器语法——字体、字号与颜色
字体、字号以及颜色可在<font ……中同时设置，如可对文字“微软雅黑字体”设置格式：</font>"
1224235235
<font color=#FF0000>
<font size=1>
1机器人工程专业
<font size=2>
2机器人工程专业
<font size=3>
3机器人工程专业
<font size=4>
4机器人工程专业
<font size=6>
5机器人工程专业
latex("\sum_{i=1}^{n}")
<font size=7>
6机器人工程专业
<font size=8>
7机器人工程专业
<font size=9>
8机器人工程专业
"$$\int_{-\pi}{\pi} f(x) dx$$"
'$\int_{i=1}^{n} x^2 dx$,$\sum_{x=1}^{n} 3x^2$'
</p>
'''


st.markdown(original_title, unsafe_allow_html=True)
formlue='''
<font color=#FF0000>
$\int_{i=1}^{n} x^2 dx$,$\sum_{x=1}^{n} 3x^2$
机器人工程专业
'''
st.markdown(formlue)


st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")
