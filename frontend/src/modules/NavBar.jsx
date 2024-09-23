import React from 'react';
import { LaptopOutlined, NotificationOutlined, UserOutlined } from '@ant-design/icons';
import { Breadcrumb, Layout, Menu, theme } from 'antd';
const { Header, Content, Footer, Sider } = Layout;

const items1 = ['1', '2', '3'].map((key) => ({
  key,
  label: `nav ${key}`,
}));


<Header
  style={{
    display: 'flex',
    alignItems: 'center',
  }}
>
  <div className="demo-logo" />
  <Menu
    theme="dark"
    mode="horizontal"
    defaultSelectedKeys={['2']}
    items={items1}
    style={{
      flex: 1,
      minWidth: 0,
    }}
  />
</Header>