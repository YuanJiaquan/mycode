# 发送html文件


import smtplib
from email.mime.text import MIMEText
from email.header import Header

con=smtplib.SMTP_SSL('smtp.qq.com','465')
con.login('772878309@qq.com','dziluhwygqbvbcjj')
sender='772878309@qq.com'
receiver=['704046058@qq.com']

# html的文件内容
htmlconnext='''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Unit Test Report</title>
    <meta name="generator" content="HTMLTestRunner 0.8.2"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         { }

/* -- heading ---------------------------------------------------------------------- */
h1 {
	font-size: 16pt;
	color: gray;
}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}

/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}

a.popup_link:hover {
    color: red;
}

.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 500px;
}

}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
}
#result_table {
    width: 80%;
    border-collapse: collapse;
    border: 1px solid #777;
}
#header_row {
    font-weight: bold;
    color: white;
    background-color: #777;
}
#result_table td {
    border: 1px solid #777;
    padding: 2px;
}
#total_row  { font-weight: bold; }
.passClass  { background-color: #6c6; }
.failClass  { background-color: #c60; }
.errorClass { background-color: #c00; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }


/* -- ending ---------------------------------------------------------------------- */
#ending {
}

</style>

</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

<div class='heading'>
<h1>Unit Test Report</h1>
<p class='attribute'><strong>Start Time:</strong> 2020-11-16 21:15:18</p>
<p class='attribute'><strong>Duration:</strong> 0:00:36.322919</p>
<p class='attribute'><strong>Status:</strong> Pass 2</p>

<p class='description'></p>
</div>



<p id='show_detail_line'>Show
<a href='javascript:showCase(0)'>Summary</a>
<a href='javascript:showCase(1)'>Failed</a>
<a href='javascript:showCase(2)'>All</a>
</p>
<table id='result_table'>
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row'>
    <td>Test Group/Test case</td>
    <td>Count</td>
    <td>Pass</td>
    <td>Fail</td>
    <td>Error</td>
    <td>View</td>
</tr>

<tr class='passClass'>
    <td>loginTest.TestCases</td>
    <td>2</td>
    <td>2</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c1',2)">Detail</a></td>
</tr>

<tr id='pt1.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_01</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_02</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='total_row'>
    <td>Total</td>
    <td>2</td>
    <td>2</td>
    <td>0</td>
    <td>0</td>
    <td>&nbsp;</td>
</tr>
</table>

<div id='ending'>&nbsp;</div>

</body>
</html>
'''
# 邮箱正文  文本类型   html
message=MIMEText(_text=htmlconnext,_subtype='html',_charset='utf-8')

# 邮箱头部
# 设置头部 设置标题
message['Subject']=Header('我还是很忧伤，高兴不起来了')
# 发件人
message['From']=Header('秋水1<2804555260@qq.com>')
# 接受人 的信息
message['To']=Header('秋水2')

# 发送邮件
con.sendmail(sender,receiver,message.as_string())






# html会写内容出来  css会把内容摆放整齐  js动态的效果  前端课程  写出一个简单的html的页面
# 了解层级 css  js 加样式  css表达式  元素定位

# 测试报告 unittest生成的测试 html形式  邮件不支持js

