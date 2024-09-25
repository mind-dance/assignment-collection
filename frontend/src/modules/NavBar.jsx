import { Layout, Menu } from 'antd';
const { Header } = Layout;

const navFeat = ["项目", "信息", "设置"].map((item, index) => ({key: index, label: item }));

const NavBar = () => {
  return (
    <Layout>
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
          defaultSelectedKeys={['1']}
          items={navFeat}
          style={{
            flex: 1,
            minWidth: 0,
          }}
        />
      </Header>
    </Layout>
  )
}

export default NavBar;