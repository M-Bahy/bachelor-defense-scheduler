import React, { useState, useEffect } from "react";
import DatePicker from "react-multi-date-picker";
import DatePanel from "react-multi-date-picker/plugins/date_panel";
import { Text, View, FlatList, TouchableOpacity } from "react-native";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import ip from "./ip.txt";

const axios = require("axios").default;

function Form() {
  const [file, setFile] = useState();
  const [dates, setDates] = useState([]);
  const [rooms, setRooms] = useState([]);
  const [room, setRoom] = useState("");

  const [ipAddr, setIpAddr] = useState("");

  useEffect(() => {
    fetch(ip)
      .then((response) => response.text())
      .then((data) => setIpAddr(data))
      .catch((error) => console.error(error));
  }, []);

  const handleChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSumbit = (event) => {
    event.preventDefault();
    const url = "http://127.0.0.1:5000/upload-file/";
    const formData = new FormData();
    formData.append("File", file);
    formData.append("Dates", dates);
    formData.append("Rooms", rooms);
    console.log(formData.get("File"));
    axios.post(url, formData).then((response) => {
      console.log(response.data);
    });
    toast(
      "Data successfully added. You can move to Examiner's Constraints tab!"
    );
  };

  const handleAddRoom = () => {
    const newList = rooms.concat(room);
    setRooms(newList);
    setRoom("");
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      handleAddRoom();
    }
  };

  return (
    <>
      <form className="addForm" onSubmit={handleSumbit}>
        <div className="formTitle">Schedule's Data</div>
        <label className="uploadLabel">
          Upload Excel File <span className="required">*</span>
        </label>
        <label className="info">(.csv)</label>
        <br></br>
        <input
          className="inpt"
          type="file"
          name="file"
          onChange={handleChange}
          accept=".csv"
        />
        <label className="dateLabel">
          Choose Dates <span className="required">*</span>
        </label>
        <div className="datePicker">
          <DatePicker
            multiple
            value={dates}
            onChange={setDates}
            sort
            plugins={[<DatePanel />]}
          ></DatePicker>
        </div>
        <label className="roomLabel">
          Choose Rooms <span className="required">*</span>
        </label>

        <div className="room">
          <div>
            <input
              type="text"
              value={room}
              onChange={(event) => {
                setRoom(event.target.value);
              }}
              onKeyPress={(event) => {
                if (event.key === "Enter") {
                  event.preventDefault();
                  handleAddRoom();
                }
              }}
            />
            <button type="button" onClick={handleAddRoom}>
              Add
            </button>
          </div>

          <div style={{ display: "flex", marginTop: "5px" }}>
            <FlatList
              data={rooms}
              keyExtractor={(item, index) => index.toString()}
              contentContainerStyle={{
                justifyContent: "flex-start",
                flexDirection: "row",
                flexWrap: "wrap",
                paddingHorizontal: 10,
              }}
              renderItem={({ item }) => (
                <TouchableOpacity style={{ padding: 10 }}>
                  <Text
                    style={{
                      backgroundColor: "#edf4fa",
                      fontSize: 15,
                      padding: 6,
                      borderRadius: 7,
                    }}
                  >
                    {item}
                  </Text>
                </TouchableOpacity>
              )}
            />
          </div>
        </div>
        <button className="btn" onClick={handleSumbit}>
          Submit
        </button>
        <ToastContainer />
      </form>
    </>
  );
}

export default Form;
