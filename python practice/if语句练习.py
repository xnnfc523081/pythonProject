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