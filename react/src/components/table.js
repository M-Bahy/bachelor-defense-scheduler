import React, { useState, useEffect } from 'react';
import axios from 'axios';
import LoadingScreen from 'react-loading-screen';
import spinner from './download.gif';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './table.css';
import ip from './ip.txt';



function Table() {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [showButton, setShowButton] = useState(true);
  const [downButton, setDownButton] = useState(false);
  const [loadingTime, setLoadingTime] = useState(null);
  const [intervalId, setIntervalId] = useState(null);

  const [ipAddr, setIpAddr] = useState('');
  const [download, setDownload] = useState('');


  useEffect(() => {
    fetch(ip)
      .then(response => response.text())
      .then(data => setIpAddr(data))
      .catch(error => console.error(error));
  }, []);


  const checkIterations = () => {
    axios
      .get(`http://${ipAddr}/get_iterations/`)
      .then((res) => {
        setLoadingTime(res.data.iterations);
        const iterations = parseInt(res.data.iterations);
        console.log("iterations: " + iterations + "%")
        if (iterations >= 99) {
          clearInterval(intervalId);
        }
      })
      .catch((error) => {
        console.error('Failed to get iterations:', error);
      });
  };

  const onGenerate = () => {
    setIsLoading(true);
    setShowButton(false);
    setDownButton(true);
    const newIntervalId = setInterval(checkIterations, 30000);
    setIntervalId(newIntervalId);
    axios
      .post(`http://${ipAddr}/generate/`)
      .then((res) => {
        console.log(res.data[0]);
        setData(res.data[0]);
        setIsLoading(false);
        console.log(newIntervalId)
        clearInterval(newIntervalId);
        setDownload(`http://${ipAddr}/downloadFile/`)
      })
      .catch((error) => {
        clearInterval(newIntervalId);
        setLoadingTime("Failed to generate: " + error);
        console.error('Failed to generate:', error);
      });
  };

  const handleSubmit = (event) => {
    toast('CSV file is downloading !!!');
  };


  return (
    <div>
      {isLoading ? (
        <>
        {/* {checkIterations} */}
         {/* <button className="btn-const1" onClick={checkIterations}>
              check iterations remaining
            </button>
          <p> This might take a while ~{loadingTime} mins</p> */}
          <LoadingScreen
            loading={true}
            logoSrc={spinner}
            text={`This might take a while ~${loadingTime ?? '0.0'}%`}
            // textStyle={{ fontSize: "2px", color: "gray" }}
          />
        </>
      ) : (
        <>
          {showButton && (
            <button className="btn-const1" onClick={onGenerate}>
              Generate Solution 
            </button>
          )}

          {downButton && (
            <>
              <form action={download}>
                <input
                  onClick={handleSubmit}
                  className="btn-const2"
                  type="submit"
                  value="Download Solution"
                />
              </form>

              {data && (
                <table className="ArchiveTable">
                  <thead>
                    <tr>
                      <th>Examiner</th>
                      <th>Supervisor</th>
                      <th>Student</th>
                      <th>Student Name</th>
                      <th>Student Email</th>
                      <th>Topic</th>
                      <th>Time</th>
                      <th>Room</th>
                      <th>Color</th>
                    </tr>
                  </thead>
                  <tbody>
                    {data.map((data, index) => (
                      <tr key={index}>
                        <td>{data.Examiner}</td>
                        <td>{data.Supervisor}</td>
                        <td>{data.Student}</td>
                        <td>{data.Studentname}</td>
                        <td>{data.Studentemail}</td>
                        <td>{data.Topic}</td>
                        <td>{data.Time}</td>
                        <td>{data.Room}</td>
                        <td>{data.Color}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}

              <ToastContainer />
            </>
          )}
        </>
      )}
    </div>
  );
};

export default Table;
