import React, { useEffect, useState } from "react";
import Navbar from "../../Components/Navbar";
import "./style.css";
import HorizontalList from "../../Components/HorizontalFlatList";
import tmdb from "../../data/tmdb";

function Dashboard() {

  const [ movieList, setMovieList ] = useState([]);

  useEffect(() => {
    const allMovieList = async () => {
      let list = await tmdb.getHomeList();
      setMovieList(list)
    }

    allMovieList();
  }, [])

  return (
    <>
      <Navbar />
      <HorizontalList />
    </>
  );
}

export default Dashboard;
