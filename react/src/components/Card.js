import React, { useState, useEffect } from "react";
import AsyncSelect from "react-select/async";
import makeAnimated from 'react-select/animated';
import Select from 'react-select';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import ip from './ip.txt';

const axios = require("axios").default;
// const url = `http://${ipAddr}/allExternals/`;
const animatedComponents = makeAnimated();

function Card() {
  const [SelectedExaminar, setSelectedExaminar] = useState({ value: "", label: "" });
  const [SelectedDate, setSelectedDate] = useState({ value: "", label: "" });
  const [day, setDay] = useState([]);
  const [dates,setDates]=useState([]);
  const [selectedslots,setSelectedslots]=useState(Array(dates.length*15).fill(0));

  const [ipAddr, setIpAddr] = useState('');

  useEffect(() => {
    fetch(ip)
      .then(response => response.text())
      .then(data => setIpAddr(data))
      .catch(error => console.error(error));
  }, []);
  
  const slotOptions = [
    { label: "Select All", value: "all" },
    { value: 0, label: '1st' },
    { value: 1, label: '2nd' },
    { value: 2, label: '3rd' },
    { value: 3, label: '4th' },
    { value: 4, label: '5th' },
    { value: 5, label: '6th' },
    { value: 6, label: '7th' },
    { value: 7, label: '8th' },
    { value: 8, label: '9th' },
    { value: 9, label: '10th' },
    { value: 10, label: '11th' },
    { value: 11, label: '12th' },
    { value: 12, label: '13th' },
    { value: 13, label: '14th' },
    { value: 14, label: '15th' },]



    const loadExaminars = (searchExaminar) => {
      return axios.get(`http://${ipAddr}/allExternals/`).then((res) => {
        let list = [];
        console.log(res.data);
        res.data["externals"].forEach((ex) => list.push({ value: ex, label: ex }));
        return list.filter((d) => d.label.toLowerCase().includes(searchExaminar.toLowerCase()));
      });
    };
  
    const loadDates = (searchDate) => {
      return axios.get(`http://${ipAddr}/allExternals/`).then((res) => {
        const exams = res.data["dates"];
        setDates(exams);
        let list = [];
        exams.forEach((ex) => list.push({ value: ex, label: ex }));
        return list.filter((d) => d.label.toLowerCase().includes(searchDate.toLowerCase()));
      });
    };
  
    const changeExaminar = (value) => {
      setSelectedExaminar(value);
      setSelectedslots(Array(dates.length*15).fill(0));
      setDay([])
    }
  
    const changeDate = (value) => {
      const tmp=dates.indexOf(SelectedDate.value)*15
      let tmplist = [...selectedslots];
      day.forEach((s) =>tmplist[tmp+s.value]=1)
      setSelectedslots(tmplist);
      const tmp2=dates.indexOf(value.value)*15
      console.log(tmp2)
      setSelectedDate(value)
      tmplist=selectedslots.slice(tmp2, tmp2+15)
      let tmplist2=[]
      for(let i in tmplist){
        if(tmplist[i]){
          if(i==0){
            tmplist2.push({ value: 0, label: '1st' })
          }
          else if(i==1){
            tmplist2.push({ value: 1, label: '2nd' })  
          }
          else if(i==2){
            tmplist2.push({ value: 2, label: '3rd' })  
          }
          else{
            let tmp10=parseInt(i)+1
            tmplist2.push({ value: parseInt(i), label: tmp10+'th' })    
          }
        }
      }
  
      setDay(tmplist2)
    }
  
    const handleSubmit = (event) => {
      event.preventDefault()
      const tmp=dates.indexOf(SelectedDate.value)*15
      let tmplist = [...selectedslots];
  
      day.forEach((s) =>tmplist[tmp+s.value]=1)
      setSelectedslots(tmplist);
  
      let res={};
      res[SelectedExaminar.value]=tmplist;
      console.log("Done with temp")
      console.log(tmplist);
      axios.post(`http://${ipAddr}/external/`,res)
      toast("Examiner constraints successfully added!");
    }

    if(ipAddr == '')
    {
      return null
    }
    
  else{
    return (
      <>
        <form className={"Constarints-1"}>
          <div className="divTitle">Examiner's Constraints</div>
  
  
          <label className="divLabel-1">
            Select Examiner <span className="required">*</span>
          </label>
  
          <label className="divLabel-2">
            Choose unavailable day <span className="required">*</span>
          </label>
          <label className="divLabel-3">
            Choose unavailable slot <span className="required">*</span>
          </label>
          <AsyncSelect
            className="dropdown-1"
            cacheOptions
            defaultOptions
            value={SelectedExaminar}
            getOptionLabel={(e) => e.label}
            getOptionValue={(e) => e.value}
            loadOptions={loadExaminars}
            onChange={changeExaminar}
          />
          <AsyncSelect 
            className="dropdown-2" 
            cacheOptions
            defaultOptions
            value={SelectedDate}
            getOptionLabel={(e) => e.label}
            getOptionValue={(e) => e.value}
            loadOptions={loadDates}
            onChange={changeDate}
          />
          <Select  
            className="dropdown-3" 
            components={animatedComponents}
            isMulti
            value={day}
            onChange={selected => {
            selected.find(option => option.value === "all")
              ? setDay(slotOptions.slice(1))
              :setDay(selected)
          }}
            options={slotOptions}
      //       autosize={true}
      //       menuPlacement="auto"
      // menuPosition="fixed"
          />
          <button className="btn-const" onClick={handleSubmit}>Add</button>
          <ToastContainer />
        </form>
      </>
    );
        }
  }
  export default Card;