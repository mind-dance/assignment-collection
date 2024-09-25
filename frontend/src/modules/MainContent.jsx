import { useState, useEffect } from "react";
import  axios  from "axios";
import { Layout, Space, Flex, theme } from "antd"
import NavSider from "./NavSider"
import List from "./List.jsx"
const { Content } = Layout;

axios.defaults.baseURL = 'http://localhost:5000';

const MainContent = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();


  return (
    <>
      <Layout
        style={{
          padding: '24px 0',
          background: colorBgContainer,
          borderRadius: borderRadiusLG,
        }}
      >
        <NavSider />
        <Content
          style={{
            padding: '0 24px',
            minHeight: 280,
          }}
        >
          <Flex gap="large" >
            <List title="文件列表"/>
          </Flex>
        </Content>
      </Layout>
    </>
  )
}

export default MainContent