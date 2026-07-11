# 欢迎光临寒舍

!!! info "公告"

    持续施工中👨‍💻……

---


<div class="quote-card">
    <div class="quote-mark">“</div>
    <a id="quote-link"><div id="quote-text">可以有不说出来的真话。但绝对不能讲假话。 </div></a>
    <div class="quote-author">——黄文俞</div>
</div>

<script>
const quotes = [
    {text:"可以有不说出来的真话。但绝对不能讲假话。",author:"黄文俞",link:"https://hhhhalcyon.github.io/article/2023/02/#_4"},
    {text:"那么如果有人说：“这是值得沉思的啊！”<br>那么我说：“你沉思过了没有？”<br>我仿佛又听到轮船的汽笛悠然长鸣……",author:"木心",link:"https://hhhhalcyon.github.io/article/2026/07/#_2"},
    {text:"请把全宇宙的声音设想成五彩缤纷的碎片，<br>试着像孩子一样坐在地上寻找并且适度地丢弃",author:"酒恩",link:"https://hhhhalcyon.github.io/article/2026/09"},
    {text:"中国政法大学法学院教授罗翔说，每当自己陷入职业的虚无与犬儒，<br>都会想起江平手书的那四个大字：法治天下。",author:"中国新闻网",link:"https://hhhhalcyon.github.io/article/2024/01"},
    {text:"每个作家必须正视这一新的现实，<br>超越语言的垃圾，恢复汉语的丰富、敏锐与新鲜，<br>重新为世界命名。",author:"北岛",link:"https://hhhhalcyon.github.io/article/2026/11"},
    {text:"大冰直播间里真正值得注视的<br>不是坐在屏幕前侃侃而谈的大冰，<br>而是深夜涌进他直播间的数万名沉默的人。",author:"《南方人物周刊》",link:"https://hhhhalcyon.github.io/article/2026/03"}
];

let index = 0;

setInterval(()=>{
    const box=document.getElementById("quote-text");
    const link=document.getElementById("quote-link");
    const author=document.querySelector(".quote-author");
    box.style.opacity=0;
    author.style.opacity=0;
    setTimeout(()=>{
        index=(index+1)%quotes.length;
        box.innerHTML=quotes[index].text;
        link.href=quotes[index].link;
        author.innerHTML="—— "+quotes[index].author;
        box.style.opacity=1;
        author.style.opacity=1;
    },600);
},4000);

</script>


## 最近更新

- [南洋寻踪：郁达夫之死](https://hhhhalcyon.github.io/article/2026/10)
- [再见《南方周末》｜1984年，他们要去创造一个时代](https://hhhhalcyon.github.io/article/2023/02)
- [「20代最重要的事之一是隔绝噪音。」](https://hhhhalcyon.github.io/article/2026/09)
- [在法兰西公学院的阳台上，望见不妥协的灵魂](article/2026/05.md)
- [北岛在2011年香港书展的演讲：古老的敌意](article/2026/11.md)


## 全体目录

### 文章2023

- [新年献词丨每一次的拥抱都以松手告终](article/2023/01.md)
- [再见保尔：左方和他的《南方周末》时代](article/2023/02.md)

### 文章2024

- [悼法学泰斗江平：呐喊者转身，金石留此声](article/2024/01.md)
- [回顾20篇江平媒体专访，尺度之大，宛若梦中](article/2024/02.md)

### 文章2025

- [在怀疑的时代依然需要信仰](article/2025/01.md)
- [在乡野中阅读生命/郭于华（摘记）](article/2025/02.md)
- [倾听底层·我们如何讲述苦难/郭于华（摘记）](article/2025/03.md)

### 文章2026

- [俞吾金：决定论与自由意志关系新探](article/2026/01.md)
- [浙大删除部分相关内容，知名考古学家消失后受审](article/2026/02.md)
- [大冰的口碑逆转与千万人的情感刚需](article/2026/03.md)
- [吴敬琏：我真不明白，国家养那些只会“整词儿”的专家有什么用？](article/2026/04.md)
- [在法兰西公学院的阳台上，望见不妥协的灵魂](article/2026/05.md)
- [何欢欢：文科贵“养”，“用”在一时](article/2026/06.md)
- [木心忆茅盾书屋：塔下读书处](article/2026/07.md)
- [“好像路都被堵住了” 如何托住休学的孩子？](article/2026/08.md)
- [20代最重要的事之一是隔绝噪音。](article/2026/09.md)
- [南洋寻踪：郁达夫之死](article/2026/10.md)
- [北岛在2011年香港书展的演讲：古老的敌意](article/2026/11.md)

### 原创