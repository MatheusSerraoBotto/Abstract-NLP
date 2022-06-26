import { Abstract, AbstractModel } from './abstracts.shema';

/**
 * Class to manipulate Klines
 */
class AbstractUtils {


	async saveAbstract(data: { id: string, title: string, abstract: string, theme: string })
		: Promise<Abstract> {
		const doc = new AbstractModel({
			id: data['id'],
			title: data['title'],
			abstract: data['abstract'],
			theme: data['theme']
		});
		return doc.save().then(function (doc) {
			return doc
		})
	}

	// 	/**
	// 	 * Get all Klines by symbol and timeFrame in MongoDB
	// 	 * @param {string} symbol The pair of coin, e.g, 'BTCUSDT'.
	// 	 * @param {string} timeFrame The time frame, e.g, '1h',
	// 	 * @return {Kline[]} Array of Klines.
	// 	 */
	// 	async getAllKline(symbol: string = enviroment.trading.symbol, timeFrame: string = enviroment.trading.timeFrame, limit?: number)
	// 		: Promise<Klines[]> {
	// 		try {
	// 			let results: Klines[] = []
	// 			if (limit) {
	// 				results = await KlinesModel.find({ symbol, timeFrame }).limit(limit);
	// 			} else {
	// 				results = await KlinesModel.find({ symbol, timeFrame });
	// 			}
	// 			return results;
	// 		} catch (err) {
	// 			throw err;
	// 		}
	// 	}

	// 	async getLastNKline(symbol: string = enviroment.trading.symbol, timeFrame: string = enviroment.trading.timeFrame, limit: number = enviroment.anaylicts.window)
	// 		: Promise<Klines[]> {
	// 		try {
	// 			let results: Klines[] = []
	// 			results = await KlinesModel.find({ symbol, timeFrame }, {}, { sort: { _id: -1 } }).limit(limit);
	// 			return results;
	// 		} catch (err) {
	// 			throw err;
	// 		}
	// 	}

	// 	async getLastKlineFromDb(symbol: string = enviroment.trading.symbol, timeFrame: string = enviroment.trading.timeFrame): Promise<Klines> {
	// 		let res: Klines = await KlinesModel.findOne({ symbol, timeFrame }, {}, { sort: { _id: -1 } }) as Klines
	// 		if (!res) {
	// 			const klines: Klines[] = await getAndSaveKlinesFromBinance(symbol, timeFrame)
	// 			res = klines[klines.length - 1]
	// 		}
	// 		return res
	// 	}


}

export const abstractUtils = new AbstractUtils();

