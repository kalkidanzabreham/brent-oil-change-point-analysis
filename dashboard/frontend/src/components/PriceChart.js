import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";

export default function PriceChart({ data }) {
  return (
    <LineChart width={900} height={400} data={data}>
      <XAxis dataKey="Date" />
      <YAxis />
      <Tooltip />
      <Line type="monotone" dataKey="Price" />
    </LineChart>
  );
}
