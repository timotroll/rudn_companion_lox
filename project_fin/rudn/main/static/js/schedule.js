const schedule = document.getElementById('ScheduleUl')
const ParaNum = Number(document.getElementById('ParaNum').innerText)
console.log(ParaNum)
console.log(schedule.childNodes)
schedule.childNodes[ParaNum].style.boxShadow = 'rgba(0, 0, 0, 0.16) 0px 1px 10px, rgb(51, 51, 51) 0px 0px 0px 3px'