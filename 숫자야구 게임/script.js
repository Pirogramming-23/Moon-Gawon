// @ts-nocheck
//TODO: 숫자 비교 스트라이크 볼 처리

const answer=["1","2","3"];
function check_numbers(){
    const number1 = document.getElementById("number1").value;
    const number2 = document.getElementById("number2").value;
    const number3 = document.getElementById("number3").value;

    document.getElementById("number1").value ="";
    document.getElementById("number2").value ="";
    document.getElementById("number3").value ="";
    let strike = 0;
    let ball = 0;

    //TODO: input값이 비워져 있을떄 초기화
    if (!number1 || !number2 || !number3){
        console.log("초기화");
        document.getElementById("number1").value ="";
        document.getElementById("number2").value ="";
        document.getElementById("number3").value ="";
        return;
    }

    //TODO: 결과값을 만들어서 ball인지, strike인지 출력
    //TODO: answer와 input값 비교하기
    const input=[number1,number2,number3];
    
    for(let i=0;i<3;i++){
        console.log(`비교 중: answer[${i}] = ${answer[i]}, input[${i}] = ${input[i]}`);
        if(answer[i]===input[i]){
            strike++;
        }
        else if(answer.includes(input[i])){
            ball++;
        }
    }
    let result =`${input.join("")}=`;
    if(strike===0 && ball===0){
        result+=`0`;
    }
    else if(strike>0){
        result+=`${strike}`;
    }
    else if(ball>0){
        result+=`${ball}`;
    }
    const results= document.getElementById("results");
    results.innerHTML += result+ `<br>`;


}
