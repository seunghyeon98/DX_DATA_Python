// import logo from "./logo.svg";
import "./App.css";

import mycp from "./mycp";
import Sample from "./Sample";

import EventCmp from "./EventCmp";

function App() {
  return (
    <>
      <mycp album="D" />
      <Sample album="exodus">샘플데이터</Sample>
      <EventCmp />
    </>
  );
}

export default App;
