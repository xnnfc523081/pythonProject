# 题目描述
# 你是一家餐厅的收银系统程序员，需要编写一个程序来计算顾客的消费金额。
# 程序要求：
# 输入顾客的消费总额
# 输入顾客是否是会员（是/否）
# 输入是否使用优惠券（是/否）
# 输入就餐人数
# 根据以下规则计算最终价格：
# 优惠规则：
# 会员折扣
# 普通会员：9折
# 高级会员：8折
# 优惠券折扣：
# 满100减20元优惠券
# 满200减50元优惠券
# 人数优惠：
# 3人及以上就餐：总价95折
# 5人及以上就餐：总价9折
# 特殊规则：
# 所有优惠可以叠加使用
# 优惠顺序：先计算人数优惠，再计算会员折扣，最后减去优惠券金额
# 如果同时满足多个优惠券条件，只能选择其中一种使用
# 输出要求：
# 显示详细的价格构成
# 显示每一步优惠后的金额
# 显示最终应付金额

# 示例输出
# text
# 请输入消费总额：300
# 是否是会员（是/否）：是
# 会员等级（普通/高级）：高级
# 是否使用优惠券（是/否）：是
# 优惠券类型（满100减20/满200减50）：满200减50
# 就餐人数：4
#
# 价格明细：
# 原始消费：300元
# 人数优惠（4人95折）：285元
# 会员折扣（高级会员8折）：228元
# 优惠券减免（满200减50）：178元
# 最终应付金额：178元
cost = float(input("请输入消费总额："))
member = input("是否是会员(是/否)：")
if member == "是":
        grade = input("会员等级（普通/高级）：")
discount = int(input("优惠券类型（1：满100减20/2：满200减50）："))
people = int(input("就餐人数："))
print(f"价格明细：\n原始消费：{cost}元")
if people < 3:
    print(f"无人数优惠：{cost}元")
    if member == "是":
        if grade == "普通":
            print(f"会员折扣（普通会员9折）：{cost * 0.9} 元")
            if discount == 1 and 100 <= cost * 0.9 <200:
                print(f"优惠券减免（满100减20）：{cost * 0.9 - 20}元")
                final_1 = cost * 0.9 - 20
                print(f"最终应付金额：{final_1}元")
            elif discount == 2 and 200 <= cost * 0.9:
                print(f"优惠券减免（满200减50）：{cost * 0.9 -50}元")
                final_2 = cost * 0.9 - 50
                print(f"最终应付的金额：{final_2}元")
            else:
                print(f"消费不满100，无优惠券减免：{cost * 0.9}元")
                final_3 = cost * 0.9
                print(f"最终应付的金额：{final_3}元")
        else:
            print(f"会员折扣（高级会员8折）：{cost * 0.8}元")
            if discount == 1 and 100 <= cost * 0.8 < 200:
                print(f"优惠券减免（满100减20）：{cost * 0.8 - 20}元")
                final_4 = cost * 0.8 - 20
                print(f"最终应付的金额：{final_4}元")
            elif discount == 2 and 200 <= cost * 0.8:
                print(f"优惠券减免（满200减50）：{cost * 0.8 -50}元")
                final_5 = cost * 0.8 - 50
                print(f"最终应付的金额：{final_5}元")
            else:
                print(f"消费不满100，无优惠券减免：{cost * 0.8}元")
                final_6 = cost * 0.8
                print(f"最终应付的金额：{final_6}元")
    else:
        print(f"无会员优惠:{cost}元")
        if discount == 1 and 100 <= cost < 200:
            print(f"优惠券减免（满100减20）：{cost - 20}元")
            final_7 = cost - 20
            print(f"最终应付金额：{final_7}元")
        elif discount == 2 and 200 <= cost:
            print(f"优惠券减免（满200减50）：{cost - 50}元")
            final_8 = cost - 50
            print(f"最终应付的金额：{final_8}元")
        else:
            print(f"消费不满100，无优惠券减免：{cost}元")
            final_9 = cost
            print(f"最终应付的金额：{final_9}元")
if 3 <= people <5:
    print(f"人数优惠（{people}人95折）：{cost * 0.95}元")
    if member == "是":
        if grade == "普通":
            print(f"会员折扣（普通会员9折）：{cost * 0.95 *0.9} 元")
            if discount == 1 and 100 <= cost * 0.9 * 0.95 <200:
                print(f"优惠券减免（满100减20）：{cost * 0.9 * 0.95 - 20}元")
                final_A = cost * 0.9 * 0.95 - 20
                print(f"最终应付金额：{final_A}元")
            elif discount == 2 and 200 <= cost * 0.9 * 0.95:
                print(f"优惠券减免（满200减50）：{cost * 0.9 * 0.95 -50}元")
                final_B = cost * 0.9 * 0.95 - 50
                print(f"最终应付的金额：{final_B}元")
            else:
                print(f"消费不满100，无优惠券减免：{cost * 0.9 * 0.95}元")
                final_C = cost * 0.9 * 0.95
                print(f"最终应付的金额：{final_C}元")
        else:
            print(f"会员折扣（高级会员8折）：{cost * 0.8 * 0.95}元")
            if discount == 1 and 100 <= cost * 0.8 * 0.95 < 200:
                print(f"优惠券减免（满100减20）：{cost * 0.8 * 0.95 - 20}元")
                gfinal_1 = cost * 0.8 * 0.95 - 20
                print(f"最终应付的金额：{gfinal_1}元")
            elif discount == 2 and 200 <= cost * 0.8 * 0.95:
                print(f"优惠券减免（满200减50）：{cost * 0.8 * 0.95 -50}元")
                gfinal_2 = cost * 0.8 * 0.95 - 50
                print(f"最终应付的金额：{gfinal_2}元")
            else:
                print(f"消费不满100，无优惠券减免：{cost * 0.8 * 0.95}元")
                gfinal_3 = cost * 0.8 * 0.95
                print(f"最终应付的金额：{gfinal_3}元")
    else:
        print(f"无会员优惠:{cost}元")
        if discount == 1 and 100 <= cost * 0.95 < 200:
            print(f"优惠券减免（满100减20）：{cost * 0.95 - 20}元")
            fal_1 = cost * 0.95 - 20
            print(f"最终应付金额：{fal_1}元")
        elif discount == 2 and 200 <= cost * 0.95:
            print(f"优惠券减免（满200减50）：{cost * 0.95 - 50}元")
            fal_2 = cost * 0.95- 50
            print(f"最终应付的金额：{fal_2}元")
        else:
            print(f"消费不满100，无优惠券减免：{cost * 0.95}元")
            fal_3 = cost * 0.95
            print(f"最终应付的金额：{fal_3}元")
if 5 <= people:
    print(f"人数优惠（{people}人9折）：{cost * 0.9}元")
    if member == "是":
        if grade == "普通":
            print(f"会员折扣（普通会员9折）：{cost * 0.9 *0.9} 元")
            if discount == 1 and 100 <= cost * 0.9 * 0.9 <200:
                print(f"优惠券减免（满100减20）：{cost * 0.9 * 0.9 - 20}元")
                final_a = cost * 0.9 * 0.9 - 20
                print(f"最终应付金额：{final_a}元")
            elif discount == 2 and 200 <= cost * 0.9 * 0.9:
                print(f"优惠券减免（满200减50）：{cost * 0.9 * 0.9 -50}元")
                final_b = cost * 0.9 * 0.9 - 50
                print(f"最终应付的金额：{final_b}元")
            else:
                print(f"消费不满100，无优惠券减免：{cost * 0.9 * 0.9}元")
                final_c = cost * 0.9 * 0.9
                print(f"最终应付的金额：{final_c}元")
        else:
            print(f"会员折扣（高级会员8折）：{cost * 0.8 * 0.9}元")
            if discount == 1 and 100 <= cost * 0.8 * 0.9 < 200:
                print(f"优惠券减免（满100减20）：{cost * 0.8 * 0.9 - 20}元")
                gfinal_4 = cost * 0.8 * 0.9 - 20
                print(f"最终应付的金额：{gfinal_4}元")
            elif discount == 2 and 200 <= cost * 0.8 * 0.9:
                print(f"优惠券减免（满200减50）：{cost * 0.8 * 0.9 -50}元")
                gfinal_5 = cost * 0.8 * 0.9 - 50
                print(f"最终应付的金额：{gfinal_5}元")
            else:
                print(f"消费不满100，无优惠券减免：{cost * 0.8 * 0.9}元")
                gfinal_6 = cost * 0.8 * 0.9
                print(f"最终应付的金额：{gfinal_6}元")
    else:
        print(f"无会员优惠:{cost}元")
        if discount == 1 and 100 <= cost * 0.9 < 200:
            print(f"优惠券减免（满100减20）：{cost * 0.9 - 20}元")
            fal_4 = cost * 0.9 - 20
            print(f"最终应付金额：{fal_4}元")
        elif discount == 2 and 200 <= cost * 0.9:
            print(f"优惠券减免（满200减50）：{cost * 0.9 - 50}元")
            fal_5 = cost * 0.9- 50
            print(f"最终应付的金额：{fal_5}元")
        else:
            print(f"消费不满100，无优惠券减免：{cost * 0.9}元")
            fal_6 = cost * 0.9

            print(f"最终应付的金额：{fal_6}元")
