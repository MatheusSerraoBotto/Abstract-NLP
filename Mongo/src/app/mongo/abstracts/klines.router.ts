// import express from "express";
// import { binanceUtils } from "../../binance/binance.utils";
// import { enviroment } from "../../config/config";
// import { Klines } from "./abstracts.shema";
// import { klinesUtils } from "./klines.utils";

// export const klinesRouter = express.Router();
// const basePath = '/klines'


// klinesRouter.get(`${basePath}`, async (req, res) => {
// 	const symbol = req.query.symbol ? req.query.symbol.toString() : enviroment.trading.symbol
// 	const timeFrame = req.query.timeFrame ? req.query.timeFrame.toString() : enviroment.trading.timeFrame
// 	const klines = await klinesUtils.getAllKline(symbol, timeFrame);
// 	res.json(klines);
// });

// klinesRouter.get(`${basePath}/update`, async (req, res) => {
// 	const symbol = req.query.symbol ? req.query.symbol.toString() : enviroment.trading.symbol
// 	const timeFrame = req.query.timeFrame ? req.query.timeFrame.toString() : enviroment.trading.timeFrame
// 	const limit = req.query.limit ? req.query.limit.toString() : enviroment.trading.limit
// 	const startTime = req.query.startTime ? req.query.startTime.toString() : ''
// 	const klines = await getAndSaveKlinesFromBinance(symbol, timeFrame, limit, startTime)
// 	res.json(klines);
// });

// export const getAndSaveKlinesFromBinance = async (symbol: string = enviroment.trading.symbol, timeFrame: string = enviroment.trading.timeFrame, limit: string = enviroment.trading.limit, endTime: string = '') => {
// 	const klinesRaw: Array<any> = await binanceUtils.getKlines(symbol, limit, timeFrame, endTime);
// 	const klines: Promise<Klines>[] = [];
// 	klinesRaw.forEach((kline: any) => {
// 		let item = klinesUtils.saveKline(symbol, timeFrame, kline)
// 		klines.push(item);
// 	});
// 	let res: any[] = []
// 	await Promise.allSettled(klines).then((result: any[]) => {
// 		res = result.map(e => e.value)
// 	});
// 	return res
// }


