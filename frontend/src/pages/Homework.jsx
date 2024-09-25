import React from "react"
import NavBar from "../modules/NavBar.jsx"
import NavLine from '../modules/NavLine.jsx'
import MainContent from '../modules/MainContent.jsx'
// import NavSider from "../modules/NavSider.jsx"
const Homework = () => {
    return(
        <>
        <NavBar />
        {/* 展示所有文件，已提交名单，未提交名单。 */}
        <NavLine gps={["项目","作业7274"]}/>
        {/* <NavSider /> */}
        <MainContent />
        </>
    )
}

export default Homework