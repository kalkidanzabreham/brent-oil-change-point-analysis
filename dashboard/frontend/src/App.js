import { useEffect, useState } from "react";
import { fetchPrices } from "./services/api";
import PriceChart from "./components/PriceChart";

function App() {
  const [prices, setPrices] = useState([]);

  useEffect(() => {
    fetchPrices().then(setPrices);
  }, []);

  return (
    <div>
      <h1>Brent Oil Price Dashboard</h1>
      <PriceChart data={prices} />
    </div>
  );
}

export default App;
