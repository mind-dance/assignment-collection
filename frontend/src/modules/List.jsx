import { useEffect, useState } from "react";
import { Card, Space } from "antd";
import  axios  from "axios";

axios.defaults.baseURL = 'http://localhost:5000';

const List = (props) => {
  const [list, setList] = useState([])
  useEffect(()=>{
    axios.get("/api/read-filenames").then((res) => (
      setList(res.data)
    ))
  }, [])
  
  return (
    <>
      <Space direction="horizontal" size={16}>
        <Card
          title={props.title}
          style={{
            width: 300,
          }}
        >
          {list.map((item, index) => (<p key={index}>{item}</p>))}
        </Card>
      </Space>
    </>
  )
}

export default List