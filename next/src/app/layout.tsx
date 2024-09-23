import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Home page",
  description: "Root Page",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="jp">
      <body>
        {children}
      </body>
    </html>
  );
}