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
    {text:"中国政法大学法学院教授罗翔说，每当自己陷入职业的虚无与犬儒，<br>都会想起江平手书的那四个大字：法治天下。",author:"《悼法学泰斗江平：呐喊者转身，金石留此声》",link:"https://hhhhalcyon.github.io/article/2024/01"}
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