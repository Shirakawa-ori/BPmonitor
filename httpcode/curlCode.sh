#!/bin/bash 

#报警函数
function Semail(){
mailCODE=$1;
mailURL=$2;
getdate=`date`;
#构造报警信息
mail_smg=`echo -e '<br/>Chack HTTP\n<br/>date:'${getdate}'\n<br/>URL:'${mailURL}'\n<br/>HttpCode:'${mailCODE}`;
#调用报警
python sendmail.py "${mail_smg}"
}

#检测传入参数
URL=$1
echo '********************'
if [ ! -n $URL ];then
  echo "URL is NULL";
  exit 0;
else
  echo "URL is ${URL}";
fi

#获取http响应代码 
HTTP_CODE=`curl -o /dev/null -s -w "%{http_code}" "${URL}"`;

#返回不是200 报警
if [ $HTTP_CODE != 200 ];then
    echo "HTTP_CODE: ${HTTP_CODE}";
    echo $HTTP_CODE;
    Semail $HTTP_CODE $URL;
#返回200
else
    echo 'status 200 HTTP OK!';
    echo '********************'
    exit 0;
fi
