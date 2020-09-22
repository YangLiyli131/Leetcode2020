class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        dict = {}
        food_list = []
        all_orders = []
        for o in orders:
            order_id = o[1]
            if int(order_id) not in all_orders:
                all_orders.append(int(order_id))
            food = o[2]
            if food not in food_list:
                food_list.append(food)
            if order_id not in dict:
                temp = []
                temp.append(food)
                dict[order_id] = temp
            else:
                temp = dict[order_id]
                temp.append(food)
                dict[order_id] = temp
        food_list.sort()
        all_orders.sort()
        res = []
        for row in all_orders:
            cur = []
            cur.append(str(row))
            foods = dict[str(row)]
            for i in range(len(food_list)):
                cur.append(0)
            for f in foods:
                cur[food_list.index(f)+1] += 1
            for c in range(len(cur)):
                cur[c] = str(cur[c])
            res.append(cur)
        header = food_list
        header.insert(0, 'Table')
        res.insert(0,header)
        return res
        
        